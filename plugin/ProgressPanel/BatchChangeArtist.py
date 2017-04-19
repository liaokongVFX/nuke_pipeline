# -*- coding:utf-8 -*-
__date__ = '2017/4/19 13:20'
__author__ = 'liaokong'

import sys
import os

from PySide import QtGui
from PySide import QtCore

dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dirs)

import configure.configure as config

reload(sys)
sys.setdefaultencoding('utf-8')


class BatchChangeArtist(QtGui.QWidget):
	close_sig = QtCore.Signal(str)

	def __init__(self, parent=None):
		super(BatchChangeArtist, self).__init__(parent)

		self.setWindowTitle(u"批量分派")
		self.resize(200, 500)

		self.setStyleSheet("""
			*{color:#fffff8;
			font-family:宋体;
			font-size:12px;}
			""")

		v_layout = QtGui.QVBoxLayout()
		v_layout.setAlignment(QtCore.Qt.AlignCenter)
		main_layout = QtGui.QVBoxLayout(self)
		main_layout.addLayout(v_layout)
		self.add_button = QtGui.QPushButton(self)
		self.add_button.setText(u"分派")
		main_layout.addWidget(self.add_button)

		self.artist_radio_list = []
		for index, artist in enumerate(config.artists_list):
			artist_radio = QtGui.QRadioButton(self)
			artist_radio.setText(artist)
			self.artist_radio_list.append(artist_radio)
			v_layout.addWidget(artist_radio)

		self.add_button.clicked.connect(self.add_button_clicked)

	def add_button_clicked(self):
		for i in self.artist_radio_list:
			if i.isChecked():
				self.add_button.setText(i.text())
				self.close()
				self.close_sig.emit("fuck")


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)

	tw = BatchChangeArtist()
	tw.show()

	app.exec_()
