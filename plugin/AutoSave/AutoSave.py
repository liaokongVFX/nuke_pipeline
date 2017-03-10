# -*- coding:utf-8 -*-
__date__ = '2017/3/10 15:59'
__author__ = 'liaokong'

import os
import sys
import subprocess
import time

import nuke

dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dirs)

import configure.configure as config

pan = []
# 枚举计算机中所有存在的盘符
for i in range(65, 91):
	vol = chr(i) + ':'
	if os.path.isdir(vol):
		pan.append(vol)

backup_dir = "{}/nuke_backups/".format(pan[1])


def get_script_name():
	"""
	获取当前文件名
	"""
	script = nuke.root().name()
	script_name = os.path.basename(script)
	script_name = os.path.splitext(script_name)[0]  # splitext分割文件名和扩展名

	return script_name


def open_backup_dir():
	"""
	打开备份文件夹
	"""
	path = backup_dir.replace("/", "\\")
	subprocess.Popen(["explorer", path])


def make_save():
	"""
	保存备份文件
	"""
	script_name = get_script_name()
	project_name = script_name.split("_")[0]
	shot_name = "_".join(script_name.split("_")[1:-3])
	script_backup_dir = "{}/{}/{}".format(backup_dir, project_name, shot_name)
	current_time = time.strftime("%m%d_%H%M")

	if not os.path.isdir(script_backup_dir):
		os.makedirs(script_backup_dir)

	try:
		nuke.removeOnScriptSave(make_save)
		nuke.scriptSave("{}/{}_{}.nk".format(script_backup_dir, script_name, current_time))
		nuke.addOnScriptSave(make_save)

	except:
		nuke.message(u"没有需要备份的文件")

	del_older_backup_version(script_backup_dir)


def del_older_backup_version(path):
	"""
	删除多余的备份文件
	"""
	files_list = []

	for filename in os.listdir(path):
		if os.path.splitext(filename)[1] == ".nk":
			files_list.append(filename)

	if len(files_list) > config.number_of_backups:
		keep_list = files_list[-config.number_of_backups:]

		for filename in files_list:
			if filename not in keep_list:
				file_to_delete = "{}/{}".format(path, filename)
				if os.path.isfile(file_to_delete):
					os.remove(file_to_delete)
