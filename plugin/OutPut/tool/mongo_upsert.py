# -*- coding:utf-8 -*-
import time
import os
import sys
import nuke

# 将plugin路径插入到sys.path中，并导入configure模块
dirs = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, dirs)
import configure.configure as config
import Libs.pymongo as pymongo


def mongo_upsert():
	"""
	获取渲染的视频名称和镜头名称，最后插入到readData集合中去
	:return:None
	"""

	# 获取镜头名
	project_name_list = nuke.root().name().split("/")[-1].split("_")[1:-3]
	clean_project_name = list(set(project_name_list))
	clean_project_name.sort(key=project_name_list.index)
	clean_project_name_final = "_".join(clean_project_name)

	# 获取时间
	day = time.strftime("%d", time.localtime(time.time()))

	# 获取输出后的文件名
	write_node = nuke.thisNode()
	file_name = write_node["file"].getValue().split("/")[-1]

	# 插入 daliy 数据库数据
	config.connect_mongo.update({"$and": [{"file_name": file_name}, {"day": day}]},
								{"$set": {"file_name": file_name,
										  "shot_name": clean_project_name_final,
										  "day": day}}, upsert=True)

	# 插入 progress 数据库数据
	config.connect_mongo_progress.update({"shot_name": clean_project_name_final},
										 {"$set": {"file_name": file_name,
												   "shot_name": clean_project_name_final,
												   "day": day}}, upsert=True)
