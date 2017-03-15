# -*- coding:utf-8 -*-
__date__ = '2017/3/15 18:39'
__author__ = 'liaokong'

import socket
import sys

from PySide import QtGui

reload(sys)
sys.setdefaultencoding('utf-8')

class TrayReminderServer(object):
	BUFFER_SIZE = 2048 * 100

	def __init__(self, host="", post=5000):
		self.sock = None
		self.host = host
		self.post = post

	def connect(self):
		"""开启服务，等待接受内容"""
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.bind((self.host, self.post))
			self.sock.listen(5)
		except Exception, e:
			print "socket 错误: %s" % str(e)
			return None

	def receive(self):
		"""连接后接受内容"""
		if self.sock:
			conn, addr = self.sock.accept()
			while 1:
				data = conn.recv(self.BUFFER_SIZE)
				if len(data):
					# 当接受到内容在托盘气泡中显示
					tuopan.showMessage(u"注意", data.decode("utf-8"))
				else:
					print u"socket连接中断。"
					break