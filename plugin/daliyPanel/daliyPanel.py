# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dirs)

import configure.configure as config
import Libs.pymongo as pymongo

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))


class daliyPanel(QTableWidget):
	def __init__(self, parent=None):
		super(daliyPanel, self).__init__(parent)

		self.db_dataName = config.db_dataName

		# 表格设置
		self.setFixedSize(1580, 600)
		self.setColumnCount(len(self.db_dataName))
		self.setRowCount(config.connect_mongo.find().count() + 1)
		self.horizontalHeader().setStretchLastSection(True)  # 设置表格最后对其到边缘
		self.setSelectionBehavior(QAbstractItemView.SelectRows)

		# 如果设置了表头 style里面的 QTableWidget QTableCornerButton::section 会失效
		# 解决方法就直接隐藏掉表头，然后在添加一行表头信息
		# self.setHorizontalHeaderLabels(self.db_dataName.keys())  # 设置表头
		# self.setSortingEnabled(True)
		self.horizontalHeader().hide()  # 隐藏默认表头
		self.verticalHeader().hide()  # 隐藏边栏序号

		# 设置表头
		for head in xrange(0, len(self.db_dataName)):
			self.setItem(0, head, QTableWidgetItem(self.db_dataName.keys()[head]))

		# 将数据库中的内容输出到表格中
		for r in xrange(1, config.connect_mongo.find().count() + 1):
			for c in xrange(0, len(self.db_dataName)):
				self.setItem(r, c, QTableWidgetItem(
					config.connect_mongo.find({}, {"_id": 0})[r - 1][self.db_dataName.values()[c]]))

		# 将通过的镜头整行颜色都设置成绿色
		pass_num = []
		for r in xrange(0, self.rowCount()):
			for c in xrange(0, self.columnCount()):
				if self.item(r, c).text() == u"通过":
					pass_num.append(r)

		for r in pass_num:
			for c in xrange(0, self.columnCount()):
				self.item(r, c).setBackground(QColor(0, 205, 0))  # 设置表格通过那一行内的颜色

		# 设置列宽
		self.setColumnWidth(0, 210)
		self.setColumnWidth(1, 340)
		self.setColumnWidth(5, 400)

		# 设置表格风格
		text = open("src/style.txt").read()
		self.setStyleSheet(text)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	daliyPanel = daliyPanel()
	daliyPanel.setWindowTitle("Daliy Panel")
	daliyPanel.show()
	app.exec_()
