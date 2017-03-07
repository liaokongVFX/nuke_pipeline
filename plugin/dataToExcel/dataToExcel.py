# -*- coding:utf-8 -*-
import os
import sys
import time

dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dirs)
import configure.configure as config
import Libs.xlwt as xlwt
import Libs.pymongo as pymongo

# 设置数据库
mc = pymongo.MongoClient(host=config.mongodb_ip, port=config.mongodb_port)
db_nuke = mc.nuke
clo_readData = db_nuke.readData

# 建立数据库名字对应有序表
db_dataName = config.db_dataName

# 设置excel
wbook = xlwt.Workbook()
wsheet = wbook.add_sheet("sheet1")
excel_name = clo_readData.find_one({}, {"_id": 0})

# 设置绿色背景颜色风格
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 3
style1 = xlwt.XFStyle()
style1.pattern = pattern

for i in xrange(len(db_dataName.keys())):
	wsheet.write(0, i, db_dataName.keys()[i])

for r in xrange(1, clo_readData.find().count() + 1):
	for c in xrange(0, len(db_dataName)):
		# 当镜头通过时，设置通过格为绿色
		if clo_readData.find({}, {"_id": 0})[r - 1][db_dataName.values()[c]] == u"通过":
			wsheet.write(r, c, clo_readData.find({}, {"_id": 0})[r - 1][db_dataName.values()[c]], style1)
		else:
			wsheet.write(r, c, clo_readData.find({}, {"_id": 0})[r - 1][db_dataName.values()[c]])

wbook.save('%s.xls' % time.strftime("%Y%m%d", time.localtime(time.time())))
