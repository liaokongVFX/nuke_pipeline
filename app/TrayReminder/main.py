# -*- coding:utf-8 -*-
__date__ = '2017/3/16 17:32'
__author__ = 'liaokong'

import sys

from PySide import QtGui

from TrayReminder import TrayReminderServer

from tuopan import TuoPan

def main():
	app = QtGui.QApplication(sys.argv)
	POST = 5000
	# todo POST 需要写到配置文件中

	tuopan=TuoPan()
	tuopan.show()

	simple = TrayReminderServer("", POST)
	simple.connect()

	while 1:
		print u"等待连接建立..."
		simple.receive()

	app.exec_()


if __name__ == '__main__':
	main()
