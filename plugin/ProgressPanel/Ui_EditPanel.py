# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditPanel.ui'
#
# Created: Wed Apr 19 15:19:37 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_EditPanel(object):
    def setupUi(self, EditPanel):
        EditPanel.setObjectName("EditPanel")
        EditPanel.resize(1358, 572)
        self.verticalLayout = QtGui.QVBoxLayout(EditPanel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.batch_change_btn = QtGui.QPushButton(EditPanel)
        self.batch_change_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.batch_change_btn.setObjectName("batch_change_btn")
        self.horizontalLayout.addWidget(self.batch_change_btn)
        self.client_pass = QtGui.QPushButton(EditPanel)
        self.client_pass.setObjectName("client_pass")
        self.horizontalLayout.addWidget(self.client_pass)
        self.client_no_pass = QtGui.QPushButton(EditPanel)
        self.client_no_pass.setObjectName("client_no_pass")
        self.horizontalLayout.addWidget(self.client_no_pass)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter = QtGui.QSplitter(EditPanel)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.project_list = QtGui.QListWidget(self.splitter)
        self.project_list.setMinimumSize(QtCore.QSize(85, 0))
        self.project_list.setObjectName("project_list")
        self.detail_table = QtGui.QTableWidget(self.splitter)
        self.detail_table.setMinimumSize(QtCore.QSize(1250, 0))
        self.detail_table.setObjectName("detail_table")
        self.detail_table.setColumnCount(0)
        self.detail_table.setRowCount(0)
        self.verticalLayout.addWidget(self.splitter)
        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(EditPanel)
        QtCore.QMetaObject.connectSlotsByName(EditPanel)

    def retranslateUi(self, EditPanel):
        EditPanel.setWindowTitle(QtGui.QApplication.translate("EditPanel", "Progress Panel", None, QtGui.QApplication.UnicodeUTF8))
        self.batch_change_btn.setText(QtGui.QApplication.translate("EditPanel", "批量分派人员", None, QtGui.QApplication.UnicodeUTF8))
        self.client_pass.setText(QtGui.QApplication.translate("EditPanel", "客户通过", None, QtGui.QApplication.UnicodeUTF8))
        self.client_no_pass.setText(QtGui.QApplication.translate("EditPanel", "暂未通过", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EditPanel = QtGui.QWidget()
    ui = Ui_EditPanel()
    ui.setupUi(EditPanel)
    EditPanel.show()
    sys.exit(app.exec_())

