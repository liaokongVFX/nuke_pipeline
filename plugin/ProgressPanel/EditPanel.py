# -*- coding:utf-8 -*-
__date__ = '2017/3/2 11:27'
__author__ = 'liaokong'

import os
import sys
import time

import PySide.QtGui as QtGui
import PySide.QtCore as QtCore

dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dirs)

import configure.configure as config
import Libs.pymongo as pymongo

from Ui_EditPanel import Ui_EditPanel


class EditPanel(QtGui.QDialog, Ui_EditPanel):
	def __init__(self, parent=None):
		super(EditPanel, self).__init__(parent)
		self.setupUi(self)

		self.setFixedSize(1450, 850)
		self.project_list.setFixedSize(120, 850)
		self.detail_table.verticalHeader().hide()  # 隐藏边栏序号
		self.detail_table.horizontalHeader().setStretchLastSection(True)  # 设置表格最后对其到边缘

		self.setStyleSheet("""
			*{color:#fffff8;
			font-family:宋体;
			font-size:12px;}
			QListWidget{
			font-size:17px;
			}
		""")

		# 设置点击表头排序
		self.detail_table.setSortingEnabled(True)
		self.detail_table.sortByColumn(0, QtCore.Qt.AscendingOrder)

		# 将项目名称插入到 listWidget 中
		for project_name in config.connect_mongo_progress.distinct("project"):
			self.project_list.addItem(project_name.decode("utf8"))
		# self.project_list.setStyleSheet("QListWidget::item {color:#0b16ae;}")

		# 设置 detail_table 头部信息
		self.db_progress_dataName = config.db_progress_dataName
		self.detail_table.setColumnCount(len(self.db_progress_dataName))
		self.detail_table.setHorizontalHeaderLabels(self.db_progress_dataName.keys())

		self.detail_table.setColumnWidth(0, 60)
		self.detail_table.setColumnWidth(1, 200)
		self.detail_table.setColumnWidth(2, 50)
		self.detail_table.setColumnWidth(3, 50)
		self.detail_table.setColumnWidth(4, 100)
		self.detail_table.setColumnWidth(5, 100)
		self.detail_table.setColumnWidth(6, 70)
		self.detail_table.setColumnWidth(7, 570)

		self.project_list.currentItemChanged.connect(self.set_table_info)
		self.client_pass.clicked.connect(self.client_pass_clicked)
		self.client_no_pass.clicked.connect(self.client_no_pass_clicked)
		self.detail_table.itemChanged.connect(self.item_change)

	def set_table_info(self):
		"""在table中显示选项项目的信息"""
		sel_project = self.project_list.currentItem().text()

		self.detail_table.setRowCount(config.connect_mongo_progress.find({"project": sel_project}, {"_id": 0}).count())

		# 在 detailTable 中插入内容
		for r in xrange(config.connect_mongo_progress.find({"project": sel_project}, {"_id": 0}).count()):
			for c in xrange(len(self.db_progress_dataName)):
				self.detail_table.setItem(r, c, QtGui.QTableWidgetItem(
					config.connect_mongo_progress.find({"project": sel_project}, {"_id": 0})[r][
						self.db_progress_dataName.values()[c]]))

			# 给分配人员设置下拉菜单选项
			self.artist_comb = QtGui.QComboBox(self)
			for artist_comb_item in config.artists_list:
				self.artist_comb.addItem(artist_comb_item)

			current_artist = config.connect_mongo_progress.find({"project": sel_project}, {"_id": 0})[r][
				self.db_progress_dataName.values()[self.get_header_index(u"artist")]]

			self.artist_comb.setCurrentIndex(config.artists_list.index(current_artist))

			self.detail_table.setCellWidget(r, self.get_header_index(u"artist"), self.artist_comb)

			# 给每个comb添加 row 和 col 属性，用于槽函数中对comb定位
			self.artist_comb.setProperty("row", r)
			self.artist_comb.setProperty("col", self.get_header_index(u"artist"))
			self.artist_comb.currentIndexChanged.connect(self.artist_comb_change)

		# 设置 daliy 通过颜色
		pass_num = []
		for r in xrange(0, self.detail_table.rowCount()):
			for c in xrange(0, self.detail_table.columnCount()):
				if self.detail_table.item(r, c).text() == u"通过":
					pass_num.append(r)

		for r in pass_num:
			for c in xrange(0, self.detail_table.columnCount()):
				self.detail_table.item(r, c).setBackground(QtGui.QColor(255, 205, 2))

		# 设置客户通过颜色
		client_pass_num = []
		client_pass_list = [x.values()[0] for x in
							config.connect_mongo_progress.find({"client_pass": "pass"}, {"shot_name": 1, "_id": 0})]

		for r in xrange(0, self.detail_table.rowCount()):
			for c in xrange(0, self.detail_table.columnCount()):
				if self.detail_table.item(r, c).text() in client_pass_list:
					client_pass_num.append(r)

		for r in client_pass_num:
			for c in xrange(0, self.detail_table.columnCount()):
				self.detail_table.item(r, c).setBackground(QtGui.QColor(105, 175, 115))

	def client_pass_clicked(self):
		"""客户通过按钮"""
		sel_rows = []
		for i in self.detail_table.selectedIndexes():
			sel_rows.append(i.row())

		for r in sel_rows:
			for c in xrange(0, self.detail_table.columnCount()):
				self.detail_table.item(r, c).setBackground(QtGui.QColor(105, 175, 115))

			date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
			config.connect_mongo_progress.update(
				{"shot_name": self.detail_table.item(r, self.get_header_index(u"shot_name")).text()},
				{"$set": {"client_pass": "pass",
						  "date": date}}, upsert=True)

	def client_no_pass_clicked(self):
		"""暂未通过按钮"""
		sel_rows = []
		for i in self.detail_table.selectedIndexes():
			sel_rows.append(i.row())

		for r in sel_rows:
			for c in xrange(0, self.detail_table.columnCount()):
				self.detail_table.item(r, c).setBackground(QtGui.QColor(255, 255, 255))

			date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
			config.connect_mongo_progress.update(
				{"shot_name": self.detail_table.item(r, self.get_header_index(u"shot_name")).text()},
				{"$set": {"client_pass": "",
						  "date": date}}, upsert=True)

	def item_change(self):
		"""当格内数据被修改后，实时写入数据库"""
		change_item = None
		r = None
		c = None
		try:
			change_item = self.detail_table.currentItem().text()
			r = self.detail_table.selectedIndexes()[0].row()
			c = self.detail_table.selectedIndexes()[0].column()
		except:
			pass

		if change_item != None:
			change_item_header = config.db_progress_dataName[self.detail_table.horizontalHeaderItem(c).text()]

			date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
			config.connect_mongo_progress.update(
				{"shot_name": self.detail_table.item(r, self.get_header_index(u"shot_name")).text()},
				{"$set": {change_item_header: change_item,
						  "date": date}}, upsert=True)

	def artist_comb_change(self):
		"""当分配人员下拉菜单被修改后，实时写入数据库"""
		current_comb_row = self.sender().property("row")
		current_comb_col = self.sender().property("col")
		current_comb = self.detail_table.cellWidget(current_comb_row, current_comb_col)
		current_artist = config.artists_list[current_comb.currentIndex()]
		date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

		config.connect_mongo_progress.update(
			{"shot_name": self.detail_table.item(current_comb_row, self.get_header_index(u"shot_name")).text()},
			{"$set": {"artist": current_artist,
					  "date": date}}, upsert=True)

	def get_header_index(self, name):
		# 获取头部名称序号
		for index, _ in enumerate(config.db_progress_dataName):
			if config.db_progress_dataName[self.detail_table.horizontalHeaderItem(index).text()] == name:
				self.shot_name_index = index
		return self.shot_name_index
