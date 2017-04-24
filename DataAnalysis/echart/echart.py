# -*- coding:utf-8 -*-
import sys
import os

dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dirs)

from Libs.echarts import Echart, Legend, Bar, Axis

chart = Echart('GDP', 'This is a fake chart')
chart.use(Bar('China', [2, 3, 4, 5]))
chart.use(Legend(['GDP']))
chart.use(Axis('category', 'bottom', data=['Nov', 'Dec', 'Jan', 'Feb']))
chart.use(Bar('China', [2, 3, 4, 5]))
chart.use(Legend(['GDP']))
chart.use(Axis('category', 'bottom', data=['Nov', 'Dec', 'Jan', 'Feb']))
chart.save("../data_temp/", "echart")


# 生成的网页只能用QT5读取
# 函数参考页面：
# http://echarts.baidu.com/echarts2/doc/doc.html


def fix_echart(path):
	find_str = "https://cdnjs.cloudflare.com/ajax/libs/echarts/3.1.10/echarts.min.js"
	replace_str = "echarts.min.js"
	with open(path) as f:
		data = f.readlines()
		for i in range(len(data)):
			if find_str in data[i]:
				data[i] = data[i].replace(find_str, replace_str)

		open(path, "w").writelines(data)


fix_echart("../data_temp/echart.html")

