# -*- coding:utf-8 -*-
__date__ = '2017/3/15 14:15'
__author__ = 'liaokong'

import socket
import threading
import time


class MasterSocket(threading.Thread):
	BUFFER_SIZE = 2048 * 100

	def __init__(self, host="", post=5000, command="", timecut=5):
		threading.Thread.__init__(self)
		self.connected = False
		self.sock = None
		self.host = host
		self.post = post
		self.command = command
		self.timecut = timecut

	def connect(self):
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.connect((self.host, self.post))
			self.connected = True
			return True
		except Exception, e:
			return False

	def run(self):
		start_time = time.time()
		time_delta = 0
		while time_delta <= self.timecut:
			print "尝试连接..."
			if self.connect():
				print "连接成功"
				self.send(self.command)
				break
			else:
				time.sleep(1)
				time_delta = int(time.time() - start_time)
		if time_delta > self.timecut:
			print u"连接超时"

	def send(self, command):
		try:
			self.sock.sendall(command)
			amount_received = 0
			amount_expected = len(command)
			while amount_received < amount_expected:
				data = self.sock.recv(self.BUFFER_SIZE)
				amount_received += len(data)
				print u"收到服务器返回: %s" % data

		except socket.errno, e:
			print "socket error: %s" % format(e)

		except Exception, e:
			print "other exception: %s" % e

		finally:
			print "关闭socket"
			self.sock.close()
