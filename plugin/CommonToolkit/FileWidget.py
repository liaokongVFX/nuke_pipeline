# -*- coding:utf-8 -*-
__date__ = '2017/4/17 14:15'
__author__ = 'liaokong'

import sys

from PySide import QtGui
from PySide import QtCore


class FileWidget(QtGui.QWidget):
	def __init__(self, parent=None):
		super(FileWidget, self).__init__(parent)

		self.file_line = TextEdit()
		self.v_layout = QtGui.QVBoxLayout()

		self.v_layout.addWidget(self.file_line)
		self.setLayout(self.v_layout)

		self.setContentsMargins(0, 0, 0, 0)


class TextEdit(QtGui.QTextEdit):
	path_sig = QtCore.Signal(str)
	temp_path = None

	def __init__(self, parent=None):
		super(TextEdit, self).__init__(parent)

		self.setAcceptDrops(True)

	def dragEnterEvent(self, event):
		event.acceptProposedAction()

	def dragMoveEvent(self, event):
		pass

	def dropEvent(self, event):
		mimeData = event.mimeData()

		if mimeData.hasUrls:
			if len(mimeData.urls()) == 1:
				if mimeData.urls()[0].toLocalFile().split(".")[-1] == "py":
					with open(mimeData.urls()[0].toLocalFile()) as py_file:
						py_code = py_file.read().decode("gbk")
						self.setText(py_code)

						global temp_path
						self.temp_path = mimeData.urls()[0].toLocalFile()

						self.path_sig.emit(mimeData.urls()[0].toLocalFile())

				else:
					QtGui.QMessageBox.information(None, u"提示", u"请拖入py格式的文件")

			else:
				QtGui.QMessageBox.information(None, u"提示", u"请拖入1个文件")


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	file_widget = FileWidget()
	file_widget.show()

	app.exec_()
