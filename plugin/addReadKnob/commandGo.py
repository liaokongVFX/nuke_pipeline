# -*- coding:utf-8 -*-
import nuke
import time
import os
import sys

# 将plugin路径插入到sys.path中，并导入configure模块
dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dirs)
import configure.configure as config
import Libs.pymongo as pymongo


def command_go():
	"""
	将检查的反馈内容以及当前文件名，时间插入到readData数据库中
	:return: None
	"""

	# 获取需要存储的信息
	w = nuke.thisNode()
	project = w["file"].getValue().split("/")[-1].split("_")[0]
	file_name = w["file"].getValue().split("/")[-1]
	user_name = file_name.split(".")[0].split("_")[-2]
	if w["Pass?"].getValue() == 1.0:
		pass_value = u"通过"
	elif w["Pass?"].getValue() == 0.0:
		pass_value = u"修改"

	feed_back = w["Feedback"].getValue()
	frame_len = str(int(w["last"].getValue()) - int(w["first"].getValue()) + 1)

	year = time.strftime("%Y", time.localtime(time.time()))
	month = time.strftime("%m", time.localtime(time.time()))
	day = time.strftime("%d", time.localtime(time.time()))
	date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

	# 插入数据库数据
	config.connect_mongo.update({"$and": [{"file_name": file_name}, {"day": day}, {"month": month}]},
								{"$set": {"file_name": file_name,
										  "project": project,
										  "user_name": user_name,
										  "frame_len": frame_len,
										  "pass_value": pass_value,
										  "feed_back": feed_back,
										  "year": year,
										  "month": month,
										  "day": day,
										  "date": date}}, upsert=True)

	shot_name = "_".join(file_name.split("_comp")[0].split("_")[1:])
	# 插入 progress 数据库数据
	config.connect_mongo_progress.update({"shot_name": shot_name},
										 {"$set": {"file_name": file_name,
												   "project": project,
												   "user_name": user_name,
												   "frame_len": frame_len,
												   "pass_value": pass_value,
												   "feed_back": feed_back,
												   "year": year,
												   "month": month,
												   "day": day,
												   "date": date}}, upsert=True)
