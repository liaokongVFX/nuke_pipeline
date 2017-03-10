# -*- coding:utf-8 -*-
__date__ = '2017/3/10 16:00'
__author__ = 'liaokong'

import nuke
import AutoSave

nuke.menu("Nuke").addCommand("pipeline/open backup dir","AutoSave.open_backup_dir()")
nuke.addOnScriptSave(autoSave.make_save)
