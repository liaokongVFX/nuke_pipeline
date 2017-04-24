# -*- coding:utf-8 -*-
__date__ = '2017/3/1 13:32'

import os
import sys

dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dirs)

import Libs.pymongo as pymongo
import configure as config


def connect_mongo():
	# 连接 daliy 数据库
	mc = pymongo.MongoClient(host=config.mongodb_ip, port=config.mongodb_port)
	db_nuke = mc.nuke
	clo_readData = db_nuke.readData

	return clo_readData


def connect_mongo_progress():
	# 连接 progress 数据库
	mc = pymongo.MongoClient(host=config.mongodb_ip, port=config.mongodb_port)
	db_nuke = mc.nuke
	clo_progressData = db_nuke.progressData

	return clo_progressData


def connect_mongo_ip():
	# 连接 ip 数据库
	mc = pymongo.MongoClient(host=config.mongodb_ip, port=config.mongodb_port)
	db_ip = mc.UserIp
	clo_userIpData = db_ip.userIpData

	return clo_userIpData