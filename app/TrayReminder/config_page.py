# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))


class MainUI(QDialog):
	"""随便添加了一个，这个需要自行修改"""
	def __init__(self, parent=None):
		super(MainUI, self).__init__(parent)

		self.setWindowTitle("Standard Dialog")

		filePushButton = QPushButton(self.tr("文件对话框"))
		colorPushButton = QPushButton(self.tr("颜色对话框"))
		fontPushButton = QPushButton(self.tr("字体对话框"))

		self.fileLineEdit = QLineEdit()
		self.colorFrame = QFrame()
		self.colorFrame.setFrameShape(QFrame.Box)
		self.colorFrame.setAutoFillBackground(True)
		self.fontLineEdit = QLineEdit("Hello World!")

		layout = QGridLayout()
		layout.addWidget(filePushButton, 0, 0)
		layout.addWidget(self.fileLineEdit, 0, 1)
		layout.addWidget(colorPushButton, 1, 0)
		layout.addWidget(self.colorFrame, 1, 1)
		layout.addWidget(fontPushButton, 2, 0)
		layout.addWidget(self.fontLineEdit, 2, 1)

		self.setLayout(layout)

		self.connect(filePushButton, SIGNAL("clicked()"), self.openFile)
		self.connect(colorPushButton, SIGNAL("clicked()"), self.openColor)
		self.connect(fontPushButton, SIGNAL("clicked()"), self.openFont)

	def openFile(self):

		s = QFileDialog.getOpenFileName(self, "Open file dialog", "/", "Python files(*.py)")
		self.fileLineEdit.setText(str(s))

	def openColor(self):

		c = QColorDialog.getColor(Qt.blue)
		if c.isValid():
			self.colorFrame.setPalette(QPalette(c))

	def openFont(self):

		f, ok = QFontDialog.getFont()
		if ok:
			self.fontLineEdit.setFont(f)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = MainUI()
	form.show()
	app.exec_()