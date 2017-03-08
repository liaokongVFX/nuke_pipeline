# -*- coding:utf-8 -*-
__date__ = '2017/3/7 18:05'
__author__ = 'liaokong'

import nuke
import DaliyPanel

nuke.menu("Nuke").addMenu("nuke_pipeline").addCommand("daliyPanel", "DaliyPanel.start()")
