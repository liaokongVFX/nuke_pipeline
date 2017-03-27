# -*- coding:utf-8 -*-
__date__ = '2017/3/27 14:25'
__author__ = 'liaokong'

import sys
import os
import json
import glob
from PySide import QtGui
from PySide import QtCore


class TestPage(QtGui.QWidget):
	def __init__(self, parent=None):
		super(TestPage, self).__init__(parent)

		main_layout = QtGui.QVBoxLayout(self)
		self.button_layout = QtGui.QHBoxLayout()
		main_layout.addLayout(self.button_layout)

		self.page_stack = QtGui.QStackedWidget()
		main_layout.addWidget(self.page_stack)

		self.init_page()

	def init_page(self):
		# 从配置文件中获取信息
		conf_path = "F:/work/TD/github/nuke_pipeline/app/TrayReminder/test_code/config.json"
		# fixme 配置文件路径需要自动获取

		if not os.path.isfile(conf_path):
			raise Exception(u"配置文件未找到")

		with open(conf_path) as json_file:
			json_str = json_file.read()
			tool_info_list = json.loads(json_str)

		# 创建页面按钮按钮
		for tool_info_dict in tool_info_list:
			page_name = tool_info_dict.get("name")
			page_tool_list = tool_info_dict.get("tool_list")

			page_button = QtGui.QPushButton(page_name)
			page_button.setObjectName("%s_page_btn" % page_name)
			self.button_layout.addWidget(page_button)

			page_widget = ToolListWgt(page_name)
			self.page_stack.addWidget(page_widget)
			self.init_tool_page(page_widget, page_tool_list)
			page_button.clicked.connect(self.change_page)

	def init_tool_page(self, page_widget, page_tool_list):
		for tool_name in page_tool_list:
			tool_item = ToolItem(tool_name)
			page_widget.addItem(tool_item)

	def change_page(self):
		# 获取当前点击按钮的名字
		current_button = self.sender()
		button_name = current_button.objectName()
		page_name = button_name.replace("_btn", "_wgt")

		# 根据当前widget名字获取当期widget
		current_widget = self.findChild(QtGui.QListWidget, page_name)
		self.page_stack.setCurrentWidget(current_widget)


class ToolListWgt(QtGui.QListWidget):
	def __init__(self, obj_name, parent=None):
		super(ToolListWgt, self).__init__(parent)

		self.setObjectName("%s_page_wgt" % obj_name)
		self.setViewMode(self.IconMode)
		self.setDragEnabled(False)
		self.setDefaultDropAction(QtCore.Qt.MoveAction)
		self.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
		self.setAcceptDrops(True)
		self.setIconSize(QtCore.QSize(60, 60))

		self.itemDoubleClicked.connect(self.execute)

	def execute(self):
		print "hello"

	def dragEnterEvent(self, event):
		event.acceptProposedAction()

	def dragMoveEvent(self, event):
		pass

	def dropEvent(self, event):
		mimeData = event.mimeData()
		if mimeData.hasUrls:
			for url in mimeData.urls():
				# 获取拖入的完整路径
				print url.toLocalFile()
				# 返回值
				# C:/Users/Wanghf/Desktop/plotly-latest.min.js
				# todo: 将拖入的文件在list里面生成成一个带图标的按钮

class ToolItem(QtGui.QListWidgetItem):
	root_path = r"F:\work\TD\github\nuke_pipeline\app\TrayReminder\test_code\tools"

	def __init__(self, tool_name, parent=None):
		super(ToolItem, self).__init__(parent)

		self.setSizeHint(QtCore.QSize(75, 65))

		# 设置按钮名字
		self.setText(tool_name)
		# 根据名字查找按钮图标
		main_icon_path = self.get_icon_path(tool_name)

		# 设置按钮图标
		if os.path.isfile(main_icon_path):
			icon = QtGui.QIcon(main_icon_path)
			self.setIcon(icon)

		# 找到按钮功能
		# self.script_path = self.get_script_path()

		# 添加右键菜单
		#
		# 右键菜单添加删除功能

	@staticmethod
	def get_icon_path(tool_name):
		main_icon_name = "%s_icon.jpg" % tool_name
		main_icon_path = os.path.join(ToolItem.root_path, tool_name, main_icon_name)
		return main_icon_path


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	test_page = TestPage()
	test_page.show()
	app.exec_()
