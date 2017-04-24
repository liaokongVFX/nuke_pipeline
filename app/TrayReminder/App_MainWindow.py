# -*- coding:utf-8 -*-
__date__ = '2017/3/31 17:20'
__author__ = 'liaokong'

import sys
import os
import threading
import socket
from types import MethodType

from PyQt4 import QtCore, QtGui

from Ui_mainWindow import Ui_StrackDesktop
from APPListPage import TestPage
import config_page

reload(sys)
sys.setdefaultencoding('utf-8')

dirs = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, dirs)

import plugin.Libs.pymongo as pymongo
import plugin.configure.configure as configure


def implant_method(obj, func, func_name):
	base_class = obj.__class__
	event = MethodType(func, obj, base_class)
	setattr(obj, func_name, event)


def mousePressEvent(obj, event):
	super(obj.__class__, obj).mousePressEvent(event)
	obj.last_clicked_pos = (event.globalPos(), QtCore.QPoint(obj.main_dialog.pos()))


def mouseMoveEvent(obj, event):
	if obj.last_clicked_pos:
		move, begin = obj.last_clicked_pos
		obj.main_dialog.move((event.globalPos() - move) + begin)
	else:
		super(obj.__class__, obj).mouseMoveEvent(event)


def mouseReleaseEvent(obj, event):
	super(obj.__class__, obj).mouseReleaseEvent(event)
	obj.last_clicked_pos = None


class mainWindow(QtGui.QDialog, Ui_StrackDesktop):
	def __init__(self, parent=None):
		super(mainWindow, self).__init__(parent)

		self.setupUi(self)

		self.setFixedSize(465, 850)

		self.user_name = os.path.expanduser('~').split("\\")[-1]
		self.label.setText(self.user_name)

		# 隐藏边框
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		# 添加size grip
		size_grip = QtGui.QSizeGrip(self)
		self.sizegrip_layout.addWidget(size_grip, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)
		# shadow effect
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.shadow = QtGui.QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(15)
		self.shadow.setOffset(0, 0)
		self.main_frame.setGraphicsEffect(self.shadow)

		# 绑定鼠标事件
		self.title_bar_grp.last_clicked_pos = self.user_info_grp.last_clicked_pos = None
		self.title_bar_grp.main_dialog = self.user_info_grp.main_dialog = self
		implant_method(self.title_bar_grp, mousePressEvent, "mousePressEvent")
		implant_method(self.title_bar_grp, mouseMoveEvent, "mouseMoveEvent")
		implant_method(self.title_bar_grp, mouseReleaseEvent, "mouseReleaseEvent")
		implant_method(self.user_info_grp, mousePressEvent, "mousePressEvent")
		implant_method(self.user_info_grp, mouseMoveEvent, "mouseMoveEvent")
		implant_method(self.user_info_grp, mouseReleaseEvent, "mouseReleaseEvent")

		self.create_action()
		self.create_tray()

		self.tray_icon.show()

		# 如果想自己去写用户名和对应的ip可以注释掉这句
		self.getUserIp()

		self.tray_icon.activated.connect(self.tray_double_click)
		self.tray_icon.messageClicked.connect(self.message_clicked)

	def create_tray(self):
		self.tray_menu = QtGui.QMenu(self)
		self.tray_menu.addAction(self.restore_action)
		self.tray_menu.addAction(self.config_action)
		self.tray_menu.addSeparator()
		self.tray_menu.addAction(self.quit_action)

		self.tray_icon = QtGui.QSystemTrayIcon(self)
		self.tray_icon.setIcon(QtGui.QIcon("kl.png"))
		self.tray_icon.setContextMenu(self.tray_menu)

	def create_action(self):
		self.restore_action = QtGui.QAction(u"打开主界面", self, triggered=self.showNormal)
		self.config_action = QtGui.QAction(u"打开配置", self, triggered=self.config_panel)
		self.quit_action = QtGui.QAction(u"退出程序", self, triggered=QtGui.QApplication.quit)

	def config_panel(self):
		"""配置面板"""
		config_widget = config_page.MainUI()
		config_widget.show()
		config_widget.exec_()

	def closeEvent(self, event):
		if self.tray_icon.isVisible():
			self.hide()

	def tray_double_click(self, reason):
		if reason == QtGui.QSystemTrayIcon.DoubleClick:
			self.showNormal()

	def message_clicked(self):
		QtGui.QMessageBox.information(None, u"提示", message_data)

	def getUserIp(self):
		# 获取ip
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		try:
			s.connect(('10.255.255.255', 0))
			current_ip = s.getsockname()[0]
		except:
			current_ip = '127.0.0.1'
		finally:
			s.close()

		# 输出用户名和ip到UserIp数据库中
		configure.connect_mongo_ip.update(
			{"ip": current_ip},
			{"$set": {"ip": current_ip, "user_name": self.user_name}}, upsert=True)


class SimpleServer(object):
	BUFFER_SIZE = 2048 * 100
	message_data = None

	def __init__(self, host="", post=5000):
		self.sock = None
		self.host = host
		self.post = post

	def connect(self):
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.bind((self.host, self.post))
			# 开始监听
			self.sock.listen(5)
		except:
			pass

	def receive(self):
		if self.sock:
			conn, addr = self.sock.accept()
			print u"收到来自%s的连接" % str(addr)
			while 1:
				data = conn.recv(self.BUFFER_SIZE)
				if len(data):
					print u"收到来自%s的信息: %s" % (addr[0], addr)
					global message_data
					message_data = data.decode("utf-8")
					main_window.tray_icon.showMessage(u"注意", message_data)
					conn.sendall(u"I have received the data: %s" % data)
				else:
					print u"socket连接中断。"
					break


def severive():
	HOST = ""
	POST = 5000
	simple = SimpleServer(HOST, POST)
	simple.connect()

	while 1:
		print u"等待连接建立..."
		simple.receive()


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	app.setQuitOnLastWindowClosed(False)

	main_window = mainWindow()
	main_window.show()

	server = threading.Thread(target=severive)
	server.daemon = True
	server.start()

	app.exec_()
