# -*- coding:utf-8 -*-

import nuke
import os
import sys
import time

# 将plugin路径插入到sys.path中，并导入configure模块
dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dirs)
import configure.configure as config
import Libs.pymongo as pymongo


def commandGrade():
	w = nuke.thisNode()
	grade = w["grade_list"].enumName(int(w["grade_list"].getValue()))

	file_name = w["file"].getValue().split("/")[-1]
	if "%" in file_name:
		if len(file_name.split(".")) == 2:
			shot_name = "_".join(file_name.split("_")[:-1])

		elif len(file_name.split(".")) == 3:
			shot_name = file_name.split(".")[0]

	else:
		shot_name = file_name.split(".")[0]

	project_name = w["file"].getValue().split(config.source_root_path)[1].split("/")[0]
	artist_name = w["artist_list"].enumName(int(w["artist_list"].getValue()))
	frame_len = str(int(w["last"].getValue()) - int(w["first"].getValue()) + 1)
	date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

	config.connect_mongo_progress.update({"$and": [{"shot_name": shot_name, "project": project_name}]},
										 {"$set": {"shot_name": shot_name,
												   "grade": grade,
												   "project": project_name,
												   "artist": artist_name,
												   "frame_len": frame_len,
												   "user_name": "",
												   "pass_value": "",
												   "client_feed_back": "",
												   "date": date}}, upsert=True)
