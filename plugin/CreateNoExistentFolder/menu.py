# -*- coding:utf-8 -*-
__date__ = '2017/5/18 15:14'
__author__ = 'liaokong'

import nuke
from CreateNoExistentFolder import CreateNoExistentFolder

nuke.addBeforeRender(CreateNoExistentFolder)
