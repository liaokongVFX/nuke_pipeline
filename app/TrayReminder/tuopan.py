# -*- coding:utf-8 -*-
__date__ = '2017/3/16 17:46'
__author__ = 'liaokong'

import sys

from PySide import QtGui


class TuoPan(QtGui.QSystemTrayIcon):
	def __init__(self,parent=None):
		super(TuoPan, self).__init__(parent)


