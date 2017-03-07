# -*- coding:utf-8 -*-
__date__ = '2017/3/1 17:29'

import os
import sys

import PySide.QtGui as QtGui
import PySide.QtCore as QtCore

dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dirs)

import configure.configure as config
import Libs.pymongo as pymongo
import Libs.xlwt as xlwt

from Ui_ProgressPanel import Ui_ProgressPanel
from EditPanel import EditPanel


class ProgressPanel(QtGui.QDialog, Ui_ProgressPanel):
	def __init__(self, parent=None):
		super(ProgressPanel, self).__init__(parent)
		self.setupUi(self)

		self.setFixedSize(1450, 850)
		self.project_list.setFixedSize(120, 850)
		self.detail_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)  # 表格内容禁止修改
		self.detail_table.verticalHeader().hide()  # 隐藏边栏序号
		self.detail_table.horizontalHeader().setStretchLastSection(True)  # 设置表格最后对其到边缘
		self.detail_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)  # 设置选择一行
		# 设置点击表头排序
		self.detail_table.setSortingEnabled(True)
		self.detail_table.sortByColumn(0, QtCore.Qt.AscendingOrder)

		# 将项目名称插入到 listWidget 中
		for project_name in config.connect_mongo_progress.distinct("project"):
			self.project_list.addItem(project_name.decode("utf8"))

		self.project_list.setStyleSheet("QListWidget::item {color:#0b16ae;}")

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

		self.progressBar.setValue(0)

		# 在table中显示选项项目的信息
		self.project_list.currentItemChanged.connect(self.set_table_info)
		self.login_btn.clicked.connect(self.login_button)
		self.refurbish_btn.clicked.connect(self.refurbish_btn_clicked)
		self.save_excel_btn.clicked.connect(self.save_excel_btn_clicked)

	def set_table_info(self):
		sel_project = self.project_list.currentItem().text()

		self.detail_table.setRowCount(config.connect_mongo_progress.find({"project": sel_project}, {"_id": 0}).count())

		# 在 detailTable 中插入内容
		for r in xrange(config.connect_mongo_progress.find({"project": sel_project}, {"_id": 0}).count()):
			for c in xrange(len(self.db_progress_dataName)):
				self.detail_table.setItem(r, c, QtGui.QTableWidgetItem(
					config.connect_mongo_progress.find({"project": sel_project}, {"_id": 0})[r][
						self.db_progress_dataName.values()[c]]))

		# 设置通过颜色
		pass_num = []
		for r in xrange(0, self.detail_table.rowCount()):
			for c in xrange(0, self.detail_table.columnCount()):
				if self.detail_table.item(r, c).text() == u"通过":
					pass_num.append(r)

		for r in pass_num:
			for c in xrange(0, self.detail_table.columnCount()):
				self.detail_table.item(r, c).setBackground(QtGui.QColor(255, 255, 0))

		# 设置客户通过颜色
		client_pass_num = []
		self.client_pass_list = [x.values()[0] for x in
								 config.connect_mongo_progress.find({"client_pass": "pass"},
																	{"shot_name": 1, "_id": 0})]

		for r in xrange(0, self.detail_table.rowCount()):
			for c in xrange(0, self.detail_table.columnCount()):
				if self.detail_table.item(r, c).text() in self.client_pass_list:
					client_pass_num.append(r)

		for r in client_pass_num:
			for c in xrange(0, self.detail_table.columnCount()):
				self.detail_table.item(r, c).setBackground(QtGui.QColor(0, 255, 0))

		# 进度条设置
		self.progressBar.setMinimum(0)
		self.progressBar.setMaximum(
			config.connect_mongo_progress.find({"project": sel_project}, {"_id": 0}).count())
		self.progressBar.setValue(
			config.connect_mongo_progress.find({"$and": [{"project": sel_project}, {"client_pass": "pass"}]},
											   {"_id": 0}).count())

	def login_button(self):
		if os.path.isfile(config.lic_path):
			with open(config.lic_path, "r") as f:
				lic = f.readline()
				if lic == "568250549":  # fixme 这里可以修改成你自己的密码
					self.accept()  # 如果上面情况都符合，就接受连接
				else:
					QtGui.QMessageBox.information(self, u"提示", u"您没有编辑权限，如有问题请联系管理员。")
		else:
			QtGui.QMessageBox.information(self, u"提示", u"您没有编辑权限，如有问题请联系管理员。")

	def refurbish_btn_clicked(self):
		self.set_table_info()

	def save_excel_btn_clicked(self):
		save_path = str((QtGui.QFileDialog.getSaveFileName(self, u"请选择要输出的位置", "C:\Users\Administrator\Desktop",
														   "xls files (*.xls)"))[0].encode("utf8"))

		clo_progressData = config.connect_mongo_progress

		db_progress_dataName = config.db_progress_dataName

		# 设置excel
		try:
			sel_project = self.project_list.currentItem().text()

			wbook = xlwt.Workbook()
			wsheet = wbook.add_sheet("sheet1")

			# 设置daliy通过的黄色背景颜色风格
			pattern_y = xlwt.Pattern()
			pattern_y.pattern = xlwt.Pattern.SOLID_PATTERN
			pattern_y.pattern_fore_colour = 5
			style1 = xlwt.XFStyle()
			style1.pattern = pattern_y

			# 设置客户通过的绿色背景颜色风格
			pattern_g = xlwt.Pattern()
			pattern_g.pattern = xlwt.Pattern.SOLID_PATTERN
			pattern_g.pattern_fore_colour = 3
			style2 = xlwt.XFStyle()
			style2.pattern = pattern_g

			# 写入头部信息
			for index, item in enumerate(db_progress_dataName.keys()):
				wsheet.write(0, index, item)

			for r in xrange(1, clo_progressData.find().count() + 1):
				for c in xrange(0, len(db_progress_dataName)):
					try:
						# 当镜头daliy通过时，设置通过格为黄色
						if clo_progressData.find({"project": sel_project}, {"_id": 0})[r - 1][
							db_progress_dataName.values()[c]] == u"通过":
							wsheet.write(r, c, clo_progressData.find({"project": sel_project}, {"_id": 0})[r - 1][
								db_progress_dataName.values()[c]], style1)

						# 当镜头客户通过时，设置镜头格为绿色
						elif clo_progressData.find({"project": sel_project}, {"_id": 0})[r - 1][
							db_progress_dataName.values()[c]] in self.client_pass_list:
							wsheet.write(r, c, clo_progressData.find({"project": sel_project}, {"_id": 0})[r - 1][
								db_progress_dataName.values()[c]], style2)

						else:
							wsheet.write(r, c, clo_progressData.find({"project": sel_project}, {"_id": 0})[r - 1][
								db_progress_dataName.values()[c]])

					except:
						pass

			wbook.save(save_path)
			QtGui.QMessageBox.information(self, u"提示", u"保存成功啦,即将打开所输出的文件夹~")
			os.startfile("/".join(save_path.split("/")[:-1]))

		except:
			QtGui.QMessageBox.information(self, u"提示", u"请选择要导出excel的项目.")


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)

	ProgressPanel = ProgressPanel()
	ProgressPanel.show()

	if ProgressPanel.exec_() == QtGui.QDialog.Accepted:
		EditPanel = EditPanel()
		EditPanel.show()

		app.exec_()
