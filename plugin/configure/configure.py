# -*- coding:utf-8 -*-
import os
from collections import OrderedDict
import connectMongo

########################
#
#   配置文件设置
#
########################

# 项目素材根目录
source_root_path = "Z:/Plates/"

# mongodb的ip及端口设置
mongodb_ip = "10.0.0.117"
mongodb_port = 27017

# 连接 daliy 数据库
connect_mongo = connectMongo.connect_mongo()

# 连接 progress 数据库
connect_mongo_progress = connectMongo.connect_mongo_progress()

# 连接 ip 数据库
connect_mongo_ip = connectMongo.connect_mongo_ip()

######################################################
# 制作人员对应ip的字典

# 方案1：通过手写来指认用户对应的ip
artists_ip = {u"侯世鹏": "10.0.0.117", u"郭伟": "10.0.0.118", u"常亚茹": "10.0.0.119"}

# 方案2：通过数据库获取ip及对应的用户
# artists_ip = {i.values()[1]: i.values()[0] for i in connect_mongo_ip.find({}, {"ip": 1, "user_name": 1, "_id": 0})}
# 返回数据：{u'GuiW': u'10.0.0.118', u'Wanghf': u'10.0.0.117'}
######################################################

# 制作人员列表
artists_list = artists_ip.keys()

# lic 存放位置
lic_path = "D:/pipeline.lic"

# daliy 数据库内容
db_dataName = OrderedDict(
	[(u"项目名", u"project"), (u"镜头名", u"shot_name"), (u"文件名", u"file_name"), (u"制作人员", u"user_name"),
	 (u"帧数", u"frame_len"), (u"是否通过", u"pass_value"), (u"反馈", u"feed_back"), (u"日期", u"date")])

# grader 数据库内容
db_progress_dataName = OrderedDict(
	[(u"项目名", u"project"), (u"镜头名", u"shot_name"), (u"帧数", u"frame_len"), (u"级别", u"grade"), (u"分配人员", u"artist"),
	 (u"制作人员", u"user_name"), (u"内部审核", u"pass_value"), (u"客户反馈", u"client_feed_back"), (u"阶段完成日期", u"date")])

# TODO: 或许需要一个 artist 和 user 的键值对
# http://blog.csdn.net/qq_33232071/article/details/50915760

# 自动保存文件个数
number_of_backups = 5
