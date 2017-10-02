# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecordSaverSkeleton.ui'
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

class Ui_RecordSaver(object):
    def setupUi(self, RecordSaver):
        RecordSaver.setObjectName(_fromUtf8("RecordSaver"))
        RecordSaver.resize(776, 214)
        self.centralwidget = QtGui.QWidget(RecordSaver)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 751, 137))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.commandLinkButton = QtGui.QCommandLinkButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.gridLayout.addWidget(self.commandLinkButton, 0, 2, 1, 1)
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.gridLayout.addWidget(self.commandLinkButton_2, 1, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        RecordSaver.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RecordSaver)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 776, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        RecordSaver.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(RecordSaver)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        RecordSaver.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(RecordSaver)
        QtCore.QMetaObject.connectSlotsByName(RecordSaver)

    def retranslateUi(self, RecordSaver):
        RecordSaver.setWindowTitle(_translate("RecordSaver", "RecordSaver", None))
        self.label_2.setText(_translate("RecordSaver", "Record Type", None))
        self.label_3.setText(_translate("RecordSaver", "Record Name", None))
        self.label.setText(_translate("RecordSaver", "Save/Restore Location", None))
        self.commandLinkButton.setText(_translate("RecordSaver", "Save Record", None))
        self.commandLinkButton_2.setText(_translate("RecordSaver", "Restore Record", None))
        self.pushButton.setText(_translate("RecordSaver", "Select", None))
        self.menuHelp.setTitle(_translate("RecordSaver", "Help", None))

