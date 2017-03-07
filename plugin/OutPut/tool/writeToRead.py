# -*- coding:utf-8 -*-
import nuke
import os
import re

def write_to_read():

	write_nodes = nuke.selectedNodes("Write")

	for node in write_nodes:
		filename = node["file"].getValue()

		if "%" in filename.split("/")[-1] or "#" in filename.split("/")[-1]:

			# 素材为序列
			all_files = os.listdir(filename.split(filename.split("/")[-1])[0])
			if "Thumbs.db" in all_files:
				all_files.remove("Thumbs.db")

			frame_first = re.split(r"[._-]+", all_files[0])[-2]
			frame_last = re.split(r"[._-]+", all_files[-1])[-2]

			fullTCL = "first %d last %d origfirst %d origlast %d" % (int(frame_first), int(frame_last), int(frame_first), int(frame_last))

		else:

			# 素材为视频
			root_first = nuke.root().frameRange().first()
			root_last = nuke.root().frameRange().last()

			fullTCL = "first %d last %d origfirst %d origlast %d" % (1, root_last - root_first + 1, 1, root_last - root_first + 1)

		read_node = nuke.createNode("Read", fullTCL)
		read_node["file"].setValue(filename)
		read_node.setXpos(node.xpos())
		read_node.setYpos(node.ypos() + 100)
