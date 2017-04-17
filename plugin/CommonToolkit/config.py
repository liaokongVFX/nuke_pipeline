# -*- coding:utf-8 -*-
__date__ = '2017/4/17 17:44'
__author__ = 'liaokong'

import os
import sys
import json

config_dir = os.path.join(os.path.expanduser('~'), "comToolkit")
config_path = os.path.join(config_dir, "config.json")

reload(sys)
sys.setdefaultencoding('utf-8')

def read_json():
	with open(config_path) as json_file:
		json_str = json_file.read()
		tools_list = json.loads(json_str)
	return tools_list


def write_json(tools_list):
	with open(config_path, "w") as json_file:
		json_str = json.dumps(tools_list, ensure_ascii=False, indent=2)
		json_file.write(json_str)


def get_style(style_name):
	dirs = os.path.dirname(os.path.abspath(__file__))
	style = open(os.path.join(dirs, "src/%s.txt" % style_name)).read()
	return style