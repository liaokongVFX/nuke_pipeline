# -*- coding:utf-8 -*-
__date__ = '2017/5/18 15:14'
__author__ = 'liaokong'

import nuke
import os


def CreateNoExistentFolder():
	node = nuke.thisNode()
	file_name = node["file"].value()
	dir_path = os.path.dirname(file_name)

	if not os.path.exists(dir_path):
		os.makedirs(dir_path)
