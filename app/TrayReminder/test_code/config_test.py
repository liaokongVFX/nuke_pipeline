# -*- coding:utf-8 -*-
__date__ = '2017/3/27 14:25'
__author__ = 'liaokong'

import json

with open("F:/work/TD/github/nuke_pipeline/app/TrayReminder/test_code/config.json") as json_file:
	# fixme 配置文件路径需要自动获取
	json_str = json_file.read()
	test_dir = json.loads(json_str)
	print test_dir
