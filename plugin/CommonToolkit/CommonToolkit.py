# -*- coding:utf-8 -*-
__date__ = '2017/4/5 13:34'
__author__ = 'liaokong'

import sys
import os
import json

from PySide import QtGui
from PySide import QtCore

import nuke
import nukescripts

from ctk_config import config_dir, config_path, write_json, read_json, get_style
from AddPyWin import AddPyWin

reload(sys)
sys.setdefaultencoding('utf-8')


class CommonToolkit(QtGui.QWidget):
	def __init__(self, parent=None):
		super(CommonToolkit, self).__init__(parent)

		self.setContentsMargins(0, 0, 0, 0)

		self.v_layout = QtGui.QVBoxLayout(self)
		self.add_btn = QtGui.QPushButton(self)
		self.add_btn.setText(u"添加预设")
		self.add_btn.setObjectName("add")

		self.py_btn = QtGui.QPushButton(self)
		self.py_btn.setText(u"添加脚本")
		self.py_btn.setObjectName("add_py")

		self.v_layout.addWidget(self.add_btn)
		self.v_layout.addWidget(self.py_btn)
		self.tool_list = ToolsListWidget()
		self.v_layout.addWidget(self.tool_list)
		# self.h_layout = QtGui.QHBoxLayout(self)
		# self.h_layout.setSpacing(0)
		#
		# self.up_btn = QtGui.QPushButton(self)
		# self.up_btn.setObjectName("up")
		#
		# self.down_btn = QtGui.QPushButton(self)
		# self.down_btn.setObjectName("down")
		#
		# self.h_layout.addWidget(self.up_btn)
		# self.h_layout.addWidget(self.down_btn)
		# self.v_layout.addLayout(self.h_layout)

		self.init_tools_list()

		self.add_btn.clicked.connect(self.add_btn_clicked)
		self.py_btn.clicked.connect(self.py_btn_clicked)
		# self.up_btn.clicked.connect(self.up_btn_clicked)
		# self.down_btn.clicked.connect(self.down_btn_clicked)
		self.tool_list.doubleClicked.connect(self.list_double_clicked)

		# 给工具列表开启右键菜单功能
		self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.connect(self, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.item_right_clicked)

		self.setStyleSheet(get_style("style"))

	def item_right_clicked(self, QPos):
		# 右键菜单
		if self.tool_list.currentItem():
			self.list_menu = QtGui.QMenu()
			self.list_menu.setStyleSheet(get_style("menu_style"))
			menu_item = self.list_menu.addAction(u"删除")
			self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.menu_item_clicked)
			parent_position = self.mapToGlobal(QtCore.QPoint(0, 0))
			self.list_menu.move(parent_position + QPos)
			self.list_menu.show()

	def menu_item_clicked(self):
		current_item_name = str(self.tool_list.currentItem().text())

		button = QtGui.QMessageBox.question(self, u"提示",
											u"是否删除%s" % current_item_name,
											QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel,
											QtGui.QMessageBox.Ok)
		if button == QtGui.QMessageBox.Ok:
			# 删除json中对应的内容
			tools_list = read_json()
			current_index = self.tool_list.currentRow()
			toolset_path = tools_list[current_index].get("command")
			os.remove(toolset_path)
			tools_list.pop(current_index)
			write_json(tools_list)

			# 删除要删的item
			self.tool_list.takeItem(self.tool_list.row(self.tool_list.currentItem()))

	def init_tools_list(self):
		if os.path.isdir(config_dir) == False:
			os.mkdir(config_dir)

		if os.path.isfile(config_path) == False:
			with open(config_path, "w") as write_file:
				write_file.write("[]")

		for tool in read_json():
			tool_item = QtGui.QListWidgetItem(tool.get("name"))
			tool_item.setTextAlignment(QtCore.Qt.AlignCenter)
			tool_item.setSizeHint(QtCore.QSize(tool_item.sizeHint().width(), 25))
			self.tool_list.addItem(tool_item)

	def add_btn_clicked(self):
		current_node = nuke.selectedNodes()

		existItem = False

		if len(current_node) > 0:
			if len(current_node) == 1:
				tool_name = nuke.getInput(u'请输入预设名字:', current_node[0].name()[:-1])
			else:
				tool_name = nuke.getInput(u'请输入预设名字:')

			if tool_name:
				if self.tool_list.count() == 0:
					existItem = True

				else:
					for list_num in xrange(self.tool_list.count()):
						if self.tool_list.item(list_num).text() == tool_name:
							QtGui.QMessageBox.information(self, u"提示", u"您选的节点已添加过了，请不要重复添加")
							existItem = False
							break
						else:
							existItem = True

				if existItem:
					tool_item = QtGui.QListWidgetItem(tool_name)
					tool_item.setTextAlignment(QtCore.Qt.AlignCenter)  # 设置item居中
					tool_item.setSizeHint(QtCore.QSize(tool_item.sizeHint().width(), 25))  # 设置item高度
					self.tool_list.addItem(tool_item)

					# 保存成预设文件
					toolset_path = os.path.join(config_dir, "%s.nk" % tool_name)
					nuke.nodeCopy(toolset_path.encode("gbk"))

					# 写入json
					tools_list = read_json()
					current_tool = {"name": tool_name,
									"type": "tool_set",
									"command": toolset_path.replace("\\", "/")}
					tools_list.append(current_tool)
					write_json(tools_list)

		else:
			QtGui.QMessageBox.information(self, u"提示", u"请选择节点")

	# def up_btn_clicked(self):
	# 	current_index = self.tool_list.currentRow()
	# 	current_item = self.tool_list.takeItem(current_index)
	# 	self.tool_list.insertItem(current_index - 1, current_item)
	# 	self.tool_list.setCurrentRow(current_index - 1)
	#
	# 	# 实时保存json
	# 	tools_list = read_json()
	# 	current_tool = tools_list[current_index]
	# 	tools_list.pop(current_index)
	# 	tools_list.insert(current_index - 1, current_tool)
	# 	write_json(tools_list)
	#
	# def down_btn_clicked(self):
	# 	current_index = self.tool_list.currentRow()
	# 	current_item = self.tool_list.takeItem(current_index)
	# 	self.tool_list.insertItem(current_index + 1, current_item)
	# 	self.tool_list.setCurrentRow(current_index + 1)
	#
	# 	# 实时保存json
	# 	tools_list = read_json()
	# 	current_tool = tools_list[current_index]
	# 	tools_list.pop(current_index)
	# 	tools_list.insert(current_index + 1, current_tool)
	# 	write_json(tools_list)

	def py_btn_clicked(self):
		self.add_py_win = AddPyWin()
		self.add_py_win.show()
		self.add_py_win.closed_sig.connect(self.py_win_closed)
		self.add_py_win.exec_()

	def py_win_closed(self):
		if self.add_py_win.sender():
			while (self.tool_list.count() > 0):
				self.tool_list.takeItem(0)

			self.init_tools_list()

	def list_double_clicked(self):
		tools_list = read_json()
		current_index = self.tool_list.currentRow()
		tool_command = tools_list[current_index].get("command")

		if tools_list[current_index].get("type") == "python":
			execfile(tool_command.encode("gbk"))
		else:
			nuke.loadToolset(tool_command)


class ToolsListWidget(QtGui.QListWidget):
	old_item_index = QtCore.Signal(str)
	# drop_item_sig = QtCore.Signal(str)
	old_index = None

	def __init__(self, parent=None):
		super(ToolsListWidget, self).__init__(parent)

		self.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
		self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
		self.setAcceptDrops(True)

	# self.old_item_index.connect(self.old_index_sig)
	# self.drop_item_sig.connect(self.drag_leave_create)

	def dragEnterEvent(self, event):
		"""将所选择的item的index发射出去"""
		super(ToolsListWidget, self).dragEnterEvent(event)

		global old_index
		self.old_index = self.currentRow()

	# self.old_item_index.emit(str(self.currentRow()))

	def dragMoveEvent(self, event):
		"""修改拖拽时的minedata数据"""
		tools_list = read_json()
		event.mimeData().setText(tools_list[self.currentRow()].get("command"))

	# def old_index_sig(self):
	# 	old_index_row = self.sender().currentRow()
	# 	global old_index
	# 	self.old_index = old_index_row

	def dropEvent(self, event):
		"""预设通过拖拽的方式排序"""
		event.setDropAction(QtCore.Qt.MoveAction)
		super(ToolsListWidget, self).dropEvent(event)

		tools_list = read_json()
		change_item = tools_list[self.old_index]
		tools_list.pop(self.old_index)
		tools_list.insert(self.currentRow(), change_item)
		write_json(tools_list)

	# def dragLeaveEvent(self, event):
	# 	self.drop_item_sig.emit(str(self.currentRow()))

	# def drag_leave_create(self):
	# 	"""节点被拖出窗口后创建预设"""
	# 	tools_list = read_json()
	# 	current_index = self.sender().currentRow()
	# 	tool_command = tools_list[current_index].get("command")
	# 	if tools_list[current_index].get("type") == "node":
	# 		nuke.createNode(tool_command)
	# 	elif tools_list[current_index].get("type") == "tool_set":
	# 		nuke.loadToolset(tool_command)


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	ct = CommonToolkit()
	ct.show()
	app.exec_()
