# -*- coding:utf-8 -*-
__date__ = '2017/3/9 19:05'
__author__ = 'liaokong'

import nuke
import projectPanel

nuke.menu("Nuke").addMenu("nuke_pipeline").addCommand("projectPanel", "projectPanel.start()", "Shift+q")
