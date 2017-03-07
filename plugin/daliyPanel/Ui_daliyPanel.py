# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\work\TD\nuke_pipeline\plugin\daliyPanel\ui\daliyPanel.ui'
#
# Created: Tue Jan 10 13:34:51 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

import sys

QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setEnabled(True)
		MainWindow.setFixedSize(1750, 750)
		self.centralWidget = QtGui.QWidget(MainWindow)
		self.centralWidget.setObjectName("centralWidget")
		self.daliyTable = QtGui.QTableWidget(self.centralWidget)
		self.daliyTable.setGeometry(QtCore.QRect(330, 10, 1411, 730))
		self.daliyTable.setObjectName("daliyTable")
		self.daliyTable.horizontalHeader().setStretchLastSection(True)
		self.daliyCalendar = QtGui.QCalendarWidget(self.centralWidget)
		self.daliyCalendar.setGeometry(QtCore.QRect(10, 10, 310, 300))
		self.daliyCalendar.setObjectName("daliyCalendar")
		self.dataLabel = QtGui.QLabel(self.centralWidget)
		self.dataLabel.setGeometry(QtCore.QRect(158, 315, 150, 40))
		self.dataLabel.setObjectName("dataLabel")
		self.textEdit = QtGui.QTextEdit(self.centralWidget)
		self.textEdit.setEnabled(False)
		self.textEdit.setGeometry(QtCore.QRect(10, 650, 310, 91))
		self.textEdit.setObjectName("textEdit")
		MainWindow.setCentralWidget(self.centralWidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(
			QtGui.QApplication.translate("MainWindow", "Daliy Info Panel", None, QtGui.QApplication.UnicodeUTF8))

		self.textEdit.setHtml(QtGui.QApplication.translate("MainWindow",
														   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
														   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
														   "p, li { white-space: pre-wrap; }\n"
														   "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
														   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">在上方点击要查看的日期，即会显示所查看日期当天镜头提交的相关信息。</p></body></html>",
														   None, QtGui.QApplication.UnicodeUTF8))

