# -*- coding:utf-8 -*-

import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import nuke
import commandGo
import commandGrade

# 将plugin路径插入到sys.path中，并导入configure模块
dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dirs)

import configure.configure as config


def add_read_knob():
	w = nuke.thisNode()
	w_tab = nuke.Tab_Knob("check_up", "Check Up")
	w_pass = nuke.Boolean_Knob("Pass?")
	w_fix = nuke.String_Knob("Feedback")
	w_submit = nuke.PyScript_Knob("submit", "Submit")

	w_tab2 = nuke.Tab_Knob("grade", "grade")
	w_grade = nuke.Enumeration_Knob("grade_list", "grade: ", ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'])
	w_artist = nuke.Enumeration_Knob("artist_list", "artist: ", config.artists_list)
	w_submit_grade = nuke.PyScript_Knob("submit_grade", "Submit")

	if w.Class() == "Read":
		w.addKnob(w_tab)
		w_text = nuke.Text_Knob("read_file", "  Shot:  ")
		w.addKnob(w_text)
		w_kong = nuke.Text_Knob("kong", "", "")
		w.addKnob(w_kong)
		w.addKnob(w_pass)
		w.addKnob(w_fix)
		w.addKnob(w_submit)

		w["submit"].setCommand("addReadKnob.commandGo.command_go()")

		read_name = w["file"].getValue().split("/")[-1]
		w["read_file"].setValue(read_name)

		w.addKnob(w_tab2)
		w_text = nuke.Text_Knob("read_file1", "  Shot:  ")
		w.addKnob(w_text)
		w_kong = nuke.Text_Knob("kong", "", "")
		w.addKnob(w_kong)
		w.addKnob(w_grade)
		w.addKnob(w_artist)
		w.addKnob(w_submit_grade)

		w["read_file1"].setValue(read_name)

		w["submit_grade"].setCommand("addReadKnob.commandGrade.commandGrade()")
