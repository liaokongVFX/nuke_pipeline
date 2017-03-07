# -*- coding:utf-8 -*-
import nuke

import muban.SJ_output as SJ_output
# 需要import新模板

te_menu = nuke.menu("Nodes").addMenu("outPut", icon="logo.png")

# 添加MDL项目的渲染模板，并且需要添加reload(当前项目渲染模块)，这样使用reload按钮时模板项目渲染模块中新修改的内容才会被重载

# SJ
te_menu.addCommand("SJ", SJ_output.SJ_output)
reload(SJ_output)

# 如果想要删除上面的一个模板输出按钮并且想要在nuke中也删除那个按钮需要启用下面这句，否则菜单中的项目渲染模板按钮不会更新
# nuke.menu("Nodes").findItem("outPut").removeItem("GCD")
