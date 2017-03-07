import nuke
import output_v01.menu as opmenu
nuke.menu("Nodes").findItem("outPut").addCommand("Reload","for i in range(2):reload(opmenu)",index=0)
