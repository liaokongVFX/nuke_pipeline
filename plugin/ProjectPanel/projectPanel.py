# -*- coding:utf-8 -*-
__date__ = '2017/3/8 15:04'
__author__ = 'liaokong'

import sys
import os

from PySide import QtGui
from PySide import QtCore
# import nuke

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
		self.splitter.setSizes((20, 20, 120, 270))

		self.setFixedSize(1005, 675)
		self.creat_btn.setFixedSize(215, 27)
		self.import_btn.setFixedSize(215, 27)
		self.open_btn.setFixedSize(215, 27)
		self.open_dir_btn.setFixedSize(215, 27)
		self.category_comb.setFixedSize(105, 27)
		self.lineEdit.setText(self.root_path)

		# project 显示对应的内容
		self.project_list.addItems([x.decode("gbk") for x in os.listdir(self.root_path) if
									os.path.isdir(os.path.join(self.root_path, x)) == True])
		self.project_list.currentItemChanged.connect(self.scene_list_show)

		self.creat_btn.clicked.connect(self.creat_btn_clicked)
		# todo 导入按钮实现
		self.import_btn.clicked.connect(self.import_btn_clicked)
		# todo 打开按钮实现
		self.open_btn.clicked.connect(self.open_btn_clicked)
		# todo 导入素材按钮的实现
		self.open_dir_btn.clicked.connect(self.open_dir_btn_clicked)
		# todo 打开素材路径按钮实现

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

			self.file_list.addItems([x.decode("utf8") for x in os.listdir(self.file_path)])
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
		self.update()
		self.file_list_show()

	def import_btn_clicked(self):
		pass

	def open_btn_clicked(self):
		pass

	def open_dir_btn_clicked(self):
		pass

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)

	pjPanel = projectPanel()
	pjPanel.show()

	app.exec_()
