# -*- coding:utf-8 -*-
__date__ = '2017/3/24 17:30'
__author__ = 'liaokong'

import win32ui
import win32gui
import win32con
import win32api

# todo 把win32库打包过来

# 当拖入桌面的快捷方式生成icon图标需要的代码
def getShortcutRealPath(filePath):
	"""获取快捷方式的目标路径"""
	try:
		import pythoncom
		from win32com.shell import shell
		import locale
		pythoncom.CoInitialize()
		shortcut = pythoncom.CoCreateInstance(
			shell.CLSID_ShellLink, None, pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
		shortcut.QueryInterface(pythoncom.IID_IPersistFile).Load(filePath)
		fileRealPath = shortcut.GetPath(shell.SLGP_SHORTPATH)[0]
		fileRealPath = fileRealPath.decode(locale.getdefaultlocale()[1])
		return fileRealPath
	except Exception, e:
		print e
		return filePath


def make_icon(link_path, save_path):
	"""获取exe文件的图标"""
	ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
	ico_y = win32api.GetSystemMetrics(win32con.SM_CYICON)

	large, small = win32gui.ExtractIconEx(getShortcutRealPath(link_path), 0)
	win32gui.DestroyIcon(large[0])

	hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
	hbmp = win32ui.CreateBitmap()
	hbmp.CreateCompatibleBitmap(hdc, ico_x, ico_y)
	hdc = hdc.CreateCompatibleDC()

	hdc.SelectObject(hbmp)
	hdc.DrawIcon((0, 0), small[0])
	hbmp.SaveBitmapFile(hdc, save_path)


link_path = u"c:/QQ影音.lnk"
save_path = "save.bmp"

make_icon(link_path, save_path)

