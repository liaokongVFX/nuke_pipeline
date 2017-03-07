# -*- coding: utf-8 -*-

"""
Module implementing daliyPanel.
"""
import sys
import os
from PySide.QtCore import Slot
from PySide.QtGui import QMainWindow
from PySide.QtGui import *

from Ui_daliyPanel import Ui_MainWindow

reload(sys)
sys.setdefaultencoding('utf-8')

dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dirs)

import Libs.pymongo as pymongo
import configure.configure as config


class daliyPanel(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)
		self.setupUi(self)

		self.daliyTable.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 表格内容禁止修改
		self.daliyTable.setSortingEnabled(True)  # 设置表格可排序
		self.daliyTable.verticalHeader().hide()  # 隐藏边栏序号

		# 设置 dataLabel 显示的默认日期
		self.date = self.daliyCalendar.selectedDate()
		self.dataLabel.setText(u"日期: " + self.date.toString())

		# 设置 daliyTable 头部信息
		self.db_dataName = config.db_dataName
		self.daliyTable.setColumnCount(len(self.db_dataName))
		self.daliyTable.setHorizontalHeaderLabels(self.db_dataName.keys())

		self.daliyTable.setColumnWidth(0, 50)
		self.daliyTable.setColumnWidth(1, 220)
		self.daliyTable.setColumnWidth(2, 350)
		self.daliyTable.setColumnWidth(3, 80)
		self.daliyTable.setColumnWidth(4, 50)
		self.daliyTable.setColumnWidth(5, 70)
		self.daliyTable.setColumnWidth(6, 500)

		self.set_table_info(self.date)

		self.daliyCalendar.selectionChanged.connect(self.on_daliyCalendar_selectionChanged)

		self.set_style_sheet()

	def set_style_sheet(self):
		dirs = os.path.dirname(os.path.abspath(__file__))
		style = open(os.path.join(dirs,"src/style.txt")).read()
		self.setStyleSheet(style)

	def on_daliyCalendar_selectionChanged(self):
		"""
		1.设置dateLabel;
		2.选择日期，在table里面显示所选日期当天的镜头提交情况。
		"""
		# 动态的显示 dateLabel 里面的内容
		self.date = self.daliyCalendar.selectedDate()
		self.dataLabel.setText(u"日期: " + self.date.toString())

		self.set_table_info(self.date)

	def set_table_info(self, date):
		"""设置table中的内容"""
		# 动态的设置 daliyTable 行数
		sel_day = str(date.day())
		if len(sel_day) != 2:
			sel_day = "0" + sel_day

		sel_month = str(date.month())
		if len(sel_month) != 2:
			sel_month = "0" + sel_month

		sel_year = str(date.year())

		self.daliyTable.setRowCount(config.connect_mongo.find(
			{"$and": [{"day": sel_day}, {"month": sel_month}, {"year": sel_year}]}).count())

		# 在 daliyTable 中插入内容
		for r in xrange(config.connect_mongo.find(
				{"$and": [{"day": sel_day}, {"month": sel_month}, {"year": sel_year}]}).count()):
			for c in xrange(len(self.db_dataName)):
				self.daliyTable.setItem(r, c, QTableWidgetItem(config.connect_mongo.find(
					{"$and": [{"day": sel_day}, {"month": sel_month}, {"year": sel_year}]}, {"_id": 0})[r][
																   self.db_dataName.values()[c]]))

		# 设置通过行颜色
		pass_num = []
		for r in xrange(0, self.daliyTable.rowCount()):
			for c in xrange(0, self.daliyTable.columnCount()):
				if self.daliyTable.item(r, c).text() == u"通过":
					pass_num.append(r)

		for r in pass_num:
			for c in xrange(0, self.daliyTable.columnCount()):
				self.daliyTable.item(r, c).setBackground(QColor(0, 205, 0))  # 设置表格通过那一行内的颜色为绿色



def start():
	start.panel = daliyPanel()
	start.panel.show()
