# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddPyWin.ui'
#
# Created: Mon Apr 17 15:52:05 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(580, 650)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.path_line = QtGui.QLineEdit(Dialog)
        self.path_line.setObjectName("path_line")
        self.horizontalLayout.addWidget(self.path_line)
        self.input_file_btn = QtGui.QPushButton(Dialog)
        self.input_file_btn.setObjectName("input_file_btn")
        self.horizontalLayout.addWidget(self.input_file_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(10, 5, 10, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.name_line = QtGui.QLineEdit(Dialog)
        self.name_line.setObjectName("name_line")
        self.horizontalLayout_2.addWidget(self.name_line)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.file_widget = FileWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_widget.sizePolicy().hasHeightForWidth())
        self.file_widget.setSizePolicy(sizePolicy)
        self.file_widget.setObjectName("file_widget")
        self.verticalLayout.addWidget(self.file_widget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(-1, 0, 15, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.add_tool_btn = QtGui.QPushButton(Dialog)
        self.add_tool_btn.setMinimumSize(QtCore.QSize(85, 27))
        self.add_tool_btn.setObjectName("add_tool_btn")
        self.horizontalLayout_3.addWidget(self.add_tool_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(2, 5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "添加脚本", None, QtGui.QApplication.UnicodeUTF8))
        self.input_file_btn.setText(QtGui.QApplication.translate("Dialog", "导入", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "工具名称：", None, QtGui.QApplication.UnicodeUTF8))
        self.add_tool_btn.setText(QtGui.QApplication.translate("Dialog", "添加", None, QtGui.QApplication.UnicodeUTF8))

from FileWidget import FileWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

