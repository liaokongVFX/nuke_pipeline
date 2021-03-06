# -*- coding:utf-8 -*-
__date__ = '2017/3/8 15:04'
__author__ = 'liaokong'

import sys
import os
import time

from PySide import QtGui
from PySide import QtCore
import nuke

from Ui_projectPanel import Ui_projectPanel

reload(sys)
sys.setdefaultencoding('utf-8')


class projectPanel(QtGui.QDialog, Ui_projectPanel):
	def __init__(self, parent=None):
		super(projectPanel, self).__init__(parent)
		self.setupUi(self)

		self.root_path = "Z:/Plates"
		self.project_root_path = "Y:/Project/"

		# 设置 splitter 中的list默认宽度
		self.splitter.setSizes((10, 10, 125, 275))

		self.setFixedSize(1075, 675)
		self.creat_btn.setFixedSize(215, 27)
		self.import_btn.setFixedSize(215, 27)
		self.open_btn.setFixedSize(215, 27)
		self.open_dir_btn.setFixedSize(215, 27)
		self.category_comb.setFixedSize(105, 27)
		self.lineEdit.setText(self.root_path)

		self.setStyleSheet(self.get_style("style"))

		# 给工程列表添加右键菜单功能
		self.file_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.file_list.customContextMenuRequested.connect(self.file_path_context_menu)

		# project 显示对应的内容
		self.project_list.addItems([x.decode("gbk") for x in os.listdir(self.root_path) if
									os.path.isdir(os.path.join(self.root_path, x)) == True])
		self.project_list.currentItemChanged.connect(self.scene_list_show)
		self.file_list.itemDoubleClicked.connect(self.file_double_clicked)

		self.creat_btn.clicked.connect(self.creat_btn_clicked)
		self.import_btn.clicked.connect(self.import_btn_clicked)
		self.open_btn.clicked.connect(self.open_btn_clicked)
		self.open_dir_btn.clicked.connect(self.open_dir_btn_clicked)

	def scene_list_show(self):
		"""sence栏显示对应的内容"""
		self.scene_list.clear()
		try:
			self.scene_path = os.path.join(self.root_path, self.project_list.currentItem().text())
			self.scene_list.addItems([x.decode("utf8") for x in os.listdir(self.scene_path) if
									  os.path.isdir(os.path.join(self.scene_path, x)) == True])
		except:
			pass
		self.scene_list.currentItemChanged.connect(self.shot_list_show)

	def shot_list_show(self):
		"""shot栏显示对应的内容"""
		self.shot_list.clear()
		try:
			self.shot_path = os.path.join(self.scene_path, self.scene_list.currentItem().text())
			self.shot_list.addItems([x.decode("utf8") for x in os.listdir(self.shot_path) if
									 os.path.isdir(os.path.join(self.shot_path, x)) == True])
		except:
			pass
		self.shot_list.currentItemChanged.connect(self.file_list_show)

	def file_list_show(self):
		"""file栏显示对应的内容"""
		self.file_list.clear()
		try:
			self.file_path = os.path.join(self.project_root_path, self.project_list.currentItem().text(), "Nuke",
										  self.scene_list.currentItem().text(), self.shot_list.currentItem().text(),
										  self.category_comb.currentText())

			month = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07",
						"Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

			file_name_list = []
			file_list = [x for x in os.listdir(self.file_path) if os.path.splitext(x)[1] == ".nk"]

			# 给file list里面显示的名字加上修改的日期显示
			for file_name in file_list:
				(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(
					os.path.join(self.file_path, file_name).replace("\\", "/"))

				modify_time_list = time.ctime(mtime).split(" ")[1:]
				modify_time = "%s/%s/%s %s" % (
					modify_time_list[-1], month[modify_time_list[0]], modify_time_list[1], modify_time_list[2])
				file_name = file_name + ("  %s" % modify_time)
				file_name_list.append(file_name.decode("utf8"))

			self.file_list.addItems(file_name_list)
		except:
			pass

	def creat_btn_clicked(self):
		"""将当前工程保存成nuke文件"""
		self.final_file_path = self.file_path.replace("\\", "/")

		if os.path.exists(self.final_file_path) == False:
			os.makedirs(self.final_file_path)

		self.username = os.getenv('username')
		if self.shot_list.count() != 0:
			self.file_name_list = self.final_file_path.split("/")[2:]
			self.file_name_list.remove(u"Nuke")
			self.file_name = "_".join(self.file_name_list) + "_" + self.username + "_v0101.nk"

		nuke.scriptSaveAs(self.final_file_path + "/" + self.file_name)
		self.file_list_show()

	def import_btn_clicked(self):
		"""导入工程所对应的素材"""
		if self.shot_list.count() != 0:
			seq_name_list = os.listdir(os.path.join(self.shot_path, self.shot_list.currentItem().text()))
			if "Thumbs.db" in seq_name_list:
				seq_name_list.remove("Thumbs.db")

			if len(seq_name_list[0].split(".")) == 2:
				first_frame = seq_name_list[0].split(".")[0].split("_")[-1]
				end_frame = seq_name_list[-1].split(".")[0].split("_")[-1]
				frame_len = str(len(end_frame))
				file_ext = os.path.splitext(seq_name_list[0])[1]
				seq_name = self.shot_path + "/" + self.shot_list.currentItem().text() + "/" + "_".join(
					seq_name_list[0].split(".")[0].split("_")[:-1]) + "_%0{}d".format(frame_len) + file_ext

			elif len(seq_name_list[0].split(".")) == 3:
				first_frame = seq_name_list[0].split(".")[1]
				end_frame = seq_name_list[-1].split(".")[1]
				frame_len = str(len(end_frame))
				file_ext = os.path.splitext(seq_name_list[0])[1]
				seq_name = self.shot_path + "/" + self.shot_list.currentItem().text() + "/" + \
						   seq_name_list[0].split(".")[0] + ".%0{}d".format(frame_len) + file_ext

			read_node = nuke.createNode("Read")
			read_node["file"].setValue(seq_name.replace("\\", "/"))
			read_node["first"].setValue(int(first_frame))
			read_node["last"].setValue(int(end_frame))
			read_node["origfirst"].setValue(int(first_frame))
			read_node["origlast"].setValue(int(end_frame))
			nuke.root()["first_frame"].setValue(int(first_frame))
			nuke.root()["last_frame"].setValue(int(end_frame))

	def open_btn_clicked(self):
		"""打开所选择的工程按钮"""
		self.close()
		self.final_file_path = os.path.join(self.project_root_path, self.project_list.currentItem().text(), "Nuke",
											self.scene_list.currentItem().text(), self.shot_list.currentItem().text(),
											self.category_comb.currentText()).replace("\\", "/")

		nuke.scriptOpen(self.final_file_path + "/" + self.file_list.currentItem().text().split("  ")[0])

	def open_dir_btn_clicked(self):
		"""打开素材路径"""
		os.startfile(os.path.join(self.shot_path, self.shot_list.currentItem().text()))

	def file_double_clicked(self):
		"""双击打开要使用的文件"""
		self.open_btn_clicked()

	def file_path_context_menu(self):
		"""在工程list中右键打开对应的工程目录"""
		popMenu = QtGui.QMenu()
		popMenu.setStyleSheet(self.get_style("menu_style"))
		add_action = QtGui.QAction(self)
		add_action.setText(u"打开工程目录")
		add_action.triggered.connect(self.open_file_path_button)
		popMenu.addAction(add_action)
		popMenu.exec_(QtGui.QCursor.pos())

	def open_file_path_button(self):
		try:
			os.startfile(self.file_path)
		except:
			QtGui.QMessageBox.information(self, u"提示", u"请选择要打的工程镜头名称~")

	def get_style(self, style_name):
		dirs = os.path.dirname(os.path.abspath(__file__))
		style = open(os.path.join(dirs, "src/%s.txt" % style_name)).read()
		return style


def start():
	start.pjPanel = projectPanel()
	start.pjPanel.show()
