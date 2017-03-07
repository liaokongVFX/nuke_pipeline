# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProgressPanel.ui'
#
# Created: Tue Mar 07 17:37:02 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ProgressPanel(object):
    def setupUi(self, ProgressPanel):
        ProgressPanel.setObjectName("ProgressPanel")
        ProgressPanel.resize(1358, 572)
        self.verticalLayout = QtGui.QVBoxLayout(ProgressPanel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.refurbish_btn = QtGui.QPushButton(ProgressPanel)
        self.refurbish_btn.setObjectName("refurbish_btn")
        self.horizontalLayout.addWidget(self.refurbish_btn)
        self.save_excel_btn = QtGui.QPushButton(ProgressPanel)
        self.save_excel_btn.setObjectName("save_excel_btn")
        self.horizontalLayout.addWidget(self.save_excel_btn)
        self.login_btn = QtGui.QPushButton(ProgressPanel)
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout.addWidget(self.login_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter = QtGui.QSplitter(ProgressPanel)
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
        self.progressBar = QtGui.QProgressBar(ProgressPanel)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(ProgressPanel)
        QtCore.QMetaObject.connectSlotsByName(ProgressPanel)

    def retranslateUi(self, ProgressPanel):
        ProgressPanel.setWindowTitle(QtGui.QApplication.translate("ProgressPanel", "Grader Panel", None, QtGui.QApplication.UnicodeUTF8))
        self.refurbish_btn.setText(QtGui.QApplication.translate("ProgressPanel", "刷新", None, QtGui.QApplication.UnicodeUTF8))
        self.save_excel_btn.setText(QtGui.QApplication.translate("ProgressPanel", "导出EXCEL", None, QtGui.QApplication.UnicodeUTF8))
        self.login_btn.setText(QtGui.QApplication.translate("ProgressPanel", "编辑", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ProgressPanel = QtGui.QWidget()
    ui = Ui_ProgressPanel()
    ui.setupUi(ProgressPanel)
    ProgressPanel.show()
    sys.exit(app.exec_())

