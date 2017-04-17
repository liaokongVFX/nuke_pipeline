# -*- coding:utf-8 -*-
__date__ = '2017/4/17 13:28'
__author__ = 'liaokong'

import sys
import os
import json

from PySide import QtGui
from PySide import QtCore

from Ui_AddPyWin import Ui_Dialog
from FileWidget import TextEdit
import syntax
from config import config_dir, config_path, write_json, read_json, get_style


class AddPyWin(QtGui.QDialog, Ui_Dialog):
	closed_sig = QtCore.Signal(str)

	def __init__(self, parent=None):
		super(AddPyWin, self).__init__(parent)

		self.setupUi(self)
		self.setup_editor()

		self.setStyleSheet(get_style("style"))

		self.file_widget.file_line.path_sig.connect(self.path_sig_change)

		self.input_file_btn.clicked.connect(self.input_file_btn_clicked)
		self.add_tool_btn.clicked.connect(self.add_tool_btn_clicked)

	def path_sig_change(self):
		self.path_line.setText(self.sender().temp_path)
		self.name_line.setText(self.sender().temp_path.split("/")[-1].split(".py")[0])

	def input_file_btn_clicked(self):
		file_name = QtGui.QFileDialog.getOpenFileName(self, u"请选择要添加的python文件", "C:\Users\Administrator\Desktop",
													  "Python files(*.py)")

		self.path_line.setText(file_name[0])
		self.name_line.setText(file_name[0].split("/")[-1].split(".py")[0])

		with open(file_name[0]) as py_file:
			py_code = py_file.read().decode("gbk")
			self.file_widget.file_line.setText(py_code)

	def add_tool_btn_clicked(self):
		if self.name_line.text():
			with open(os.path.join(config_dir, self.name_line.text()) + ".py", "w") as py_file:
				py_file.write(self.file_widget.file_line.toPlainText())

			tools_list = read_json()
			current_tool = {"name": self.name_line.text(),
							"type": "python",
							"command": (os.path.join(config_dir, self.name_line.text()) + ".py").replace("\\", "/")}
			tools_list.append(current_tool)
			write_json(tools_list)
			self.close()
			self.closed_sig.emit("go")

		else:
			QtGui.QMessageBox.information(None, u"提示", u"添加要添加的python文件")

	def setup_editor(self):
		font = QtGui.QFont()
		font.setFamily("Courier")
		font.setFixedPitch(True)
		font.setPointSize(10)

		self.file_widget.file_line.setFont(font)

		self.higth_light = syntax.PythonHighlighter(self.file_widget.file_line.document())


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)

	add_py_win = AddPyWin()
	add_py_win.show()

	app.exec_()
