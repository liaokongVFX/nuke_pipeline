# -*- coding:utf-8 -*-
__date__ = '2017/3/15 18:49'
__author__ = 'liaokong'

import threading

from PySide import QtGui

from TrayReminder import TrayReminderServer

def run_tuopan():
	POST = 5000
	# todo POST 需要写到配置文件中

	simple = TrayReminderServer("", POST)
	simple.connect()

	while 1:
		print u"等待连接建立..."
		simple.receive()


a = threading.Thread(target=run_tuopan)
a.start()


# todo 未完成