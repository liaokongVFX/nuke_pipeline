# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_StrackDesktop(object):
    def setupUi(self, StrackDesktop):
        StrackDesktop.setObjectName(_fromUtf8("StrackDesktop"))
        StrackDesktop.resize(585, 811)
        StrackDesktop.setMinimumSize(QtCore.QSize(320, 500))
        StrackDesktop.setMaximumSize(QtCore.QSize(600, 16777215))
        StrackDesktop.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/strack.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StrackDesktop.setWindowIcon(icon)
        StrackDesktop.setStyleSheet(_fromUtf8("QDialog{\n"
"background-color: rgb(255, 255, 255);\n"
"}"))
        self.win_layout = QtGui.QVBoxLayout(StrackDesktop)
        self.win_layout.setSpacing(0)
        self.win_layout.setObjectName(_fromUtf8("win_layout"))
        self.main_frame = QtGui.QFrame(StrackDesktop)
        self.main_frame.setStyleSheet(_fromUtf8(""))
        self.main_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.main_frame.setObjectName(_fromUtf8("main_frame"))
        self.main_layout = QtGui.QVBoxLayout(self.main_frame)
        self.main_layout.setMargin(0)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(_fromUtf8("main_layout"))
        self.top_grp = QtGui.QGroupBox(self.main_frame)
        self.top_grp.setMinimumSize(QtCore.QSize(0, 146))
        self.top_grp.setMaximumSize(QtCore.QSize(16777215, 146))
        self.top_grp.setStyleSheet(_fromUtf8("QGroupBox#top_grp\n"
"{\n"
"    background-image: url(:/backgroud/top_back.png);\n"
"    padding:0;\n"
"    margin:0;\n"
"    border-style:soild;\n"
"    border-width: 0px;\n"
"    border-top-left-radius:2px;\n"
"    border-top-right-radius:2px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"\n"
"}"))
        self.top_grp.setTitle(_fromUtf8(""))
        self.top_grp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.top_grp.setFlat(False)
        self.top_grp.setCheckable(False)
        self.top_grp.setObjectName(_fromUtf8("top_grp"))
        self.top_group_layout = QtGui.QVBoxLayout(self.top_grp)
        self.top_group_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.top_group_layout.setMargin(0)
        self.top_group_layout.setSpacing(0)
        self.top_group_layout.setObjectName(_fromUtf8("top_group_layout"))
        self.title_bar_grp = QtGui.QGroupBox(self.top_grp)
        self.title_bar_grp.setMinimumSize(QtCore.QSize(0, 26))
        self.title_bar_grp.setMaximumSize(QtCore.QSize(16777215, 26))
        self.title_bar_grp.setStyleSheet(_fromUtf8("QGroupBox{\n"
"    border:none;\n"
"    padding:3px;\n"
"    margin:0;\n"
"}"))
        self.title_bar_grp.setObjectName(_fromUtf8("title_bar_grp"))
        self.titile_bar_layout = QtGui.QHBoxLayout(self.title_bar_grp)
        self.titile_bar_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.titile_bar_layout.setMargin(0)
        self.titile_bar_layout.setSpacing(0)
        self.titile_bar_layout.setObjectName(_fromUtf8("titile_bar_layout"))
        spacerItem = QtGui.QSpacerItem(5, 0, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.titile_bar_layout.addItem(spacerItem)
        self.icon_label = QtGui.QLabel(self.title_bar_grp)
        self.icon_label.setMaximumSize(QtCore.QSize(20, 20))
        self.icon_label.setText(_fromUtf8(""))
        self.icon_label.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/strack.png")))
        self.icon_label.setScaledContents(True)
        self.icon_label.setObjectName(_fromUtf8("icon_label"))
        self.titile_bar_layout.addWidget(self.icon_label)
        self.title_label = QtGui.QLabel(self.title_bar_grp)
        self.title_label.setStyleSheet(_fromUtf8("font: 75 10pt \"Leelawadee UI\";\n"
"color: rgb(255, 255, 255);"))
        self.title_label.setObjectName(_fromUtf8("title_label"))
        self.titile_bar_layout.addWidget(self.title_label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.titile_bar_layout.addItem(spacerItem1)
        self.minimize_btn = QtGui.QToolButton(self.title_bar_grp)
        self.minimize_btn.setMinimumSize(QtCore.QSize(25, 25))
        self.minimize_btn.setMaximumSize(QtCore.QSize(25, 25))
        self.minimize_btn.setStyleSheet(_fromUtf8("QToolButton#minimize_btn\n"
"{\n"
"    image: url(:/icons/min_white.png);\n"
"    height: 20px;\n"
"    width: 20px;\n"
"    border: none;\n"
"}\n"
"QToolButton#minimize_btn::hover\n"
"{\n"
"    image: url(:/icons/min_white.png);\n"
"    background-color: rgba(135, 158, 199, 100);;\n"
"}"))
        self.minimize_btn.setText(_fromUtf8(""))
        self.minimize_btn.setObjectName(_fromUtf8("minimize_btn"))
        self.titile_bar_layout.addWidget(self.minimize_btn)
        spacerItem2 = QtGui.QSpacerItem(10, 0, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.titile_bar_layout.addItem(spacerItem2)
        self.close_btn = QtGui.QToolButton(self.title_bar_grp)
        self.close_btn.setMinimumSize(QtCore.QSize(25, 25))
        self.close_btn.setMaximumSize(QtCore.QSize(25, 25))
        self.close_btn.setStyleSheet(_fromUtf8("QToolButton#close_btn\n"
"{\n"
"    image: url(:/icons/close_white.png);\n"
"    height: 20px;\n"
"    width: 20px;\n"
"    border: none;\n"
"}\n"
"QToolButton#close_btn::hover\n"
"{\n"
"    image: url(:/icons/close_white.png);\n"
"    background-color: #D50000;\n"
"}"))
        self.close_btn.setText(_fromUtf8(""))
        self.close_btn.setObjectName(_fromUtf8("close_btn"))
        self.titile_bar_layout.addWidget(self.close_btn)
        self.top_group_layout.addWidget(self.title_bar_grp)
        self.user_info_grp = QtGui.QGroupBox(self.top_grp)
        self.user_info_grp.setMinimumSize(QtCore.QSize(0, 120))
        self.user_info_grp.setMaximumSize(QtCore.QSize(16777215, 120))
        self.user_info_grp.setStyleSheet(_fromUtf8("QGroupBox{\n"
"    border:none;\n"
"    padding:0;\n"
"    margin:0;\n"
"}"))
        self.user_info_grp.setFlat(False)
        self.user_info_grp.setObjectName(_fromUtf8("user_info_grp"))
        self.user_info_layout = QtGui.QHBoxLayout(self.user_info_grp)
        self.user_info_layout.setMargin(0)
        self.user_info_layout.setSpacing(0)
        self.user_info_layout.setObjectName(_fromUtf8("user_info_layout"))
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.user_info_layout.addItem(spacerItem3)
        self.thubnail_label = QtGui.QLabel(self.user_info_grp)
        self.thubnail_label.setText(_fromUtf8(""))
        self.thubnail_label.setPixmap(QtGui.QPixmap(_fromUtf8(":/thumbnails/default_avatar.png")))
        self.thubnail_label.setObjectName(_fromUtf8("thubnail_label"))
        self.user_info_layout.addWidget(self.thubnail_label)
        spacerItem4 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.user_info_layout.addItem(spacerItem4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.user_info_grp)
        self.label.setStyleSheet(_fromUtf8("font: 75 12pt \"Leelawadee UI\";\n"
"color: rgb(255, 255, 255);"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.user_info_layout.addLayout(self.verticalLayout_2)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.user_info_layout.addItem(spacerItem5)
        self.user_info_layout.setStretch(3, 2)
        self.top_group_layout.addWidget(self.user_info_grp)
        self.main_layout.addWidget(self.top_grp)
        self.work_area_grp = QtGui.QGroupBox(self.main_frame)
        self.work_area_grp.setStyleSheet(_fromUtf8("background-color: #ffffff;"))
        self.work_area_grp.setTitle(_fromUtf8(""))
        self.work_area_grp.setFlat(False)
        self.work_area_grp.setObjectName(_fromUtf8("work_area_grp"))
        self.workarea_layout = QtGui.QVBoxLayout(self.work_area_grp)
        self.workarea_layout.setMargin(0)
        self.workarea_layout.setSpacing(0)
        self.workarea_layout.setObjectName(_fromUtf8("workarea_layout"))
        self.allApps = TestPage(self.work_area_grp)
        self.allApps.setObjectName(_fromUtf8("allApps"))
        self.workarea_layout.addWidget(self.allApps)
        self.main_layout.addWidget(self.work_area_grp)
        self.buttom_grp = QtGui.QGroupBox(self.main_frame)
        self.buttom_grp.setMinimumSize(QtCore.QSize(0, 35))
        self.buttom_grp.setMaximumSize(QtCore.QSize(16777215, 35))
        self.buttom_grp.setStyleSheet(_fromUtf8("background-color: #E0E0E0;\n"
"padding:0px;\n"
"border-color:#E7EFF8;\n"
"border-width:1px 0px 0px 0px;\n"
"border-style:solid;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:2px;\n"
"border-bottom-left-radius:2px;"))
        self.buttom_grp.setTitle(_fromUtf8(""))
        self.buttom_grp.setObjectName(_fromUtf8("buttom_grp"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.buttom_grp)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.menu_layout = QtGui.QHBoxLayout()
        self.menu_layout.setObjectName(_fromUtf8("menu_layout"))
        spacerItem6 = QtGui.QSpacerItem(10, 0, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.menu_layout.addItem(spacerItem6)
        self.menu_btn = QtGui.QToolButton(self.buttom_grp)
        self.menu_btn.setStyleSheet(_fromUtf8("QToolButton#menu_btn\n"
"{\n"
"    image: url(:/icons/menu_blue.png);\n"
"    height: 20px;\n"
"    border: none;\n"
"}\n"
"QToolButton#menu_btn::checked\n"
"{\n"
"    image: url(:/icons/menu_dark_blue.png);\n"
"}\n"
""))
        self.menu_btn.setText(_fromUtf8(""))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setObjectName(_fromUtf8("menu_btn"))
        self.menu_layout.addWidget(self.menu_btn)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.menu_layout.addItem(spacerItem7)
        self.horizontalLayout_2.addLayout(self.menu_layout)
        self.sizegrip_layout = QtGui.QHBoxLayout()
        self.sizegrip_layout.setObjectName(_fromUtf8("sizegrip_layout"))
        spacerItem8 = QtGui.QSpacerItem(10, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.sizegrip_layout.addItem(spacerItem8)
        self.horizontalLayout_2.addLayout(self.sizegrip_layout)
        self.main_layout.addWidget(self.buttom_grp)
        self.main_layout.setStretch(0, 1)
        self.main_layout.setStretch(1, 20)
        self.main_layout.setStretch(2, 1)
        self.win_layout.addWidget(self.main_frame)

        self.retranslateUi(StrackDesktop)
        QtCore.QObject.connect(self.close_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), StrackDesktop.close)
        QtCore.QObject.connect(self.minimize_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), StrackDesktop.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(StrackDesktop)

    def retranslateUi(self, StrackDesktop):
        StrackDesktop.setWindowTitle(_translate("StrackDesktop", "Quick Start", None))
        self.title_label.setText(_translate("StrackDesktop", "Quick Start", None))

from TestPage import TestPage
import icons_rc
import other_images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    StrackDesktop = QtGui.QDialog()
    ui = Ui_StrackDesktop()
    ui.setupUi(StrackDesktop)
    StrackDesktop.show()
    sys.exit(app.exec_())

