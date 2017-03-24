# -*- coding:utf-8 -*-
__date__ = '2017/3/24 17:57'
__author__ = 'liaokong'

        
import socket
import sys

from PySide import QtGui

from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore

import threading

reload(sys)
sys.setdefaultencoding('utf-8')


class SimpleServer(object):
	BUFFER_SIZE = 2048 * 100

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
					tuopan.tray.showMessage(u"注意", data.decode("utf-8"))
					conn.sendall(u"I have received the data: %s" % data)
				else:
					print u"socket连接中断。"
					break


class TuoPan(QtGui.QWidget):
	def __init__(self, parent=None):
		super(TuoPan, self).__init__(parent)
		# Create a Qt application
		self.setWindowFlags(QtCore.Qt.Window)
		self.setFixedSize(350,800)

		icon = QIcon("jenkins_favicon.png")
		menu = QMenu()
		settingAction = menu.addAction("setting")
		settingAction.triggered.connect(self.setting)
		exitAction = menu.addAction("exit")
		exitAction.triggered.connect(sys.exit)

		self.tray = QSystemTrayIcon()
		self.tray.setIcon(icon)
		self.tray.setContextMenu(menu)
		self.tray.show()
		self.tray.setToolTip("unko!")
		self.tray.activated.connect(self.show_main_window)

	def show_main_window(self,reason):
		if reason in (QtGui.QSystemTrayIcon.Trigger, QtGui.QSystemTrayIcon.DoubleClick):
			self.showNormal()

	def run(self):
		# Enter Qt application main loop
		self.app.exec_()
		sys.exit()

	def setting(self):
		self.dialog = QDialog()
		self.dialog.setWindowTitle("Setting Dialog")
		self.dialog.show()
		self.showMinimized()

	def closeEvent(self, event):
		if self.tray.isVisible():
			self.hide()
			event.ignore()


def severive():
	HOST = ""
	POST = 5000
	simple = SimpleServer(HOST, POST)
	simple.connect()

	while 1:
		print u"等待连接建立..."
		simple.receive()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	tuopan = TuoPan()
	tuopan.show()

	server = threading.Thread(target=severive)
	server.daemon = True
	server.start()

	app.exec_()