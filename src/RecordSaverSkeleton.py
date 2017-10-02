# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecordSaverSkeleton.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RecordSaver(object):
    def setupUi(self, RecordSaver):
        RecordSaver.setObjectName("RecordSaver")
        RecordSaver.resize(776, 214)
        self.centralwidget = QtWidgets.QWidget(RecordSaver)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 751, 137))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.gridLayout.addWidget(self.commandLinkButton, 0, 2, 1, 1)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.gridLayout.addWidget(self.commandLinkButton_2, 1, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        RecordSaver.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RecordSaver)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 776, 29))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        RecordSaver.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RecordSaver)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        RecordSaver.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(RecordSaver)
        QtCore.QMetaObject.connectSlotsByName(RecordSaver)

    def retranslateUi(self, RecordSaver):
        _translate = QtCore.QCoreApplication.translate
        RecordSaver.setWindowTitle(_translate("RecordSaver", "RecordSaver"))
        self.label_2.setText(_translate("RecordSaver", "Record Type"))
        self.label_3.setText(_translate("RecordSaver", "Record Name"))
        self.label.setText(_translate("RecordSaver", "Save/Restore Location"))
        self.commandLinkButton.setText(_translate("RecordSaver", "Save Record"))
        self.commandLinkButton_2.setText(_translate("RecordSaver", "Restore Record"))
        self.pushButton.setText(_translate("RecordSaver", "Select"))
        self.menuHelp.setTitle(_translate("RecordSaver", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RecordSaver = QtWidgets.QMainWindow()
    ui = Ui_RecordSaver()
    ui.setupUi(RecordSaver)
    RecordSaver.show()
    sys.exit(app.exec_())

