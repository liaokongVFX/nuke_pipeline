# -*- coding:utf-8 -*-
import nuke
import os
import nukescripts
import time
import sys

# 将plugin路径插入到sys.path中，并导入configure模块
dirs = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, dirs)
import configure.configure as config


def SJ_output():
	"""
	SJ渲染输出模板设置
	:return:None
	"""
	nukescripts.modelbuilder.clearNodeSelection()

	# 导入MDL_output渲染模板
	nuke.loadToolset(os.path.dirname(os.path.abspath(__file__)) + '/nk/SJ/SJ_output.nk')
	nuke.message(u"该项目最终输出尺寸为 UHD_4K 3840x2160")

	# 输出模板的说明
	StickyNote = nuke.createNode("StickyNote")
	StickyNote["label"].setValue(u"该项目最终输出尺寸为: <font color='red' size='12'><b>UHD_4K 3840x2160</b></font><br>"
								 u"<img src='Z:/Tools/.nuke/OutPut/output_v01/muban/nk/SJ/SJ.png' />")

	bookX = nuke.toNode("Daliy_Output").xpos()
	bookY = nuke.toNode("Daliy_Output").ypos()
	sel = nuke.selectedNode()
	sel.setYpos(bookY + 340)
	sel.setXpos(bookX)

	root_name = nuke.root()["name"].getValue()
	file_path = "Y:/Render/" + "/".join(root_name.split("/")[2:7]) + "/" + \
				root_name.split("/")[-1].split(".")[0].split("_")[-1] + "/"

	name = "SJ_comp_" + "_".join(root_name.split("/")[-3].split("_")[2:]) + "_" + \
		   root_name.split("/")[-1].split(".")[0].split("_")[-1][0:3] + ".mov"

	# 获取最新导入模板的Daliy、Final和add_shot_name名字
	all_write = nuke.allNodes("ModifyMetaData") + nuke.allNodes("Write")
	daliy_list = []
	final_list = []
	metadata_list = []
	for write_node in all_write:
		if "Daliy" in write_node.name():
			daliy_list.append(write_node.name())
		elif "Final" in write_node.name():
			final_list.append(write_node.name())
		elif "add_shot_name" in write_node.name():
			metadata_list.append(write_node.name())

	daliy_name = max(daliy_list)
	final_name = max(final_list)
	# metadata_name = max(metadata_list)

	# 修改Daliy输出模板的输出路径和帧速率
	sample_path = "Y:/Daliy/SJ/" + time.strftime('%Y%m%d', time.localtime(time.time())) + "/"
	sample_name = "SJ_comp_" + "_".join(root_name.split("/")[-3].split("_")[2:]) + "_" + "_".join(
		root_name.split("/")[-1].split(".")[0].split("_")[-2:]) + ".mov"

	# 获取 tool
	tool_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
							 "tool/").replace("\\", "/")
	writeToRead_path = os.path.join(tool_path, "writeToRead.py")
	mongo_upsert_path = os.path.join(tool_path, "mongo_upsert.py")

	nuke.toNode(daliy_name)["file"].setValue(sample_path + sample_name)
	nuke.toNode(daliy_name)["mov32_fps"].setValue(24)
	nuke.toNode(daliy_name)["mov64_fps"].setValue(24)
	nuke.toNode(daliy_name)["afterRender"].setValue(
		"exec(open('%s').read());write_to_read();exec(open('%s').read());mongo_upsert();" % (writeToRead_path,
																							 mongo_upsert_path))

	nuke.toNode(final_name)["file"].setValue(file_path + name)
	nuke.toNode(final_name)["mov32_fps"].setValue(24)
	nuke.toNode(final_name)["mov64_fps"].setValue(24)
	nuke.toNode(final_name)["afterRender"].setValue("exec(open('%s').read());write_to_read()" % writeToRead_path)

	# metadata信息并不能一起渲染出去
	# nuke.toNode(metadata_name)["metadata"].fromScript("{set shot_name %s}" % clean_project_name_final)

	# 生成Daliy和Final模板的渲染文件夹
	if os.path.exists(sample_path) == False:
		os.makedirs(sample_path)

	if os.path.exists(file_path) == False:
		os.makedirs(file_path)
