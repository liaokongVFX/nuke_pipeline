# -*- coding:utf-8 -*-
__date__ = '2017/3/8 10:55'
__author__ = 'liaokong'

import nuke
import ProgressPanel

nuke.menu("Nuke").addMenu("nuke_pipeline").addCommand("progressPanel", "ProgressPanel.start()")
