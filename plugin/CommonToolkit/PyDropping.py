# -*- coding:utf-8 -*-
__date__ = '2017/4/18 11:47'
__author__ = 'liaokong'

import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def PyDropping(droptype, dropped_data):
	if os.path.splitext(dropped_data)[-1] == ".py":
		try:
			execfile(dropped_data.encode("gbk"))
		except:
			pass

		return True
	else:
		return False


