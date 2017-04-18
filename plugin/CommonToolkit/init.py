# -*- coding:utf-8 -*-
__date__ = '2017/4/5 13:46'
__author__ = 'liaokong'

from CommonToolkit import CommonToolkit
from nukescripts import panels
from PyDropping import PyDropping
import nukescripts

nukescripts.addDropDataCallback(PyDropping)

panels.registerWidgetAsPanel('CommonToolkit', u'预设工具',"example.test.panel", True)
