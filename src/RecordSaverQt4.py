#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecordSaverSkeleton.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys 
import RecordSaverController as RScontroller
import time
import os
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
    def __init__(self):
        self.controller = RScontroller.RecordSaveRestoreController(self)
            
    def setupUi(self, RecordSaver):
        RecordSaver.setObjectName(_fromUtf8("RecordSaver"))
        window_size = self.controller.program_defaults["WindowSize"].split(",")
        RecordSaver.resize(int(window_size[0]),int(window_size[1]))
        self.centralwidget = QtGui.QWidget(RecordSaver)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 751, 137))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
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
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.file_text = QtGui.QLineEdit(self.gridLayoutWidget)
        self.file_text.setObjectName(_fromUtf8("file_text"))
        self.file_text.setText(self.controller.program_defaults['Default_Save_Location'])
        self.gridLayout.addWidget(self.file_text, 2, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setText(self.controller.program_defaults['Default_Record'])
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.commandLinkButton = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.gridLayout.addWidget(self.commandLinkButton, 0, 2, 1, 1)
        self.commandLinkButton_2 = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.gridLayout.addWidget(self.commandLinkButton_2, 1, 2, 1, 1)
        RecordSaver.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RecordSaver)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 776, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.helpAction = QtGui.QAction("Help",RecordSaver)
        self.helpAction.triggered.connect(self.fdisplay_help)
        self.menuHelp.addAction(self.helpAction)
        RecordSaver.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(RecordSaver)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.status_label = QtGui.QLabel(self.statusbar)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.status_label.setFont(font)
        self.status_label.setObjectName(_fromUtf8("Status Label"))
        self.status_label.setText("")
        self.status_label.setSizePolicy(QtGui.QSizePolicy.MinimumExpanding,
                     QtGui.QSizePolicy.MinimumExpanding)
        self.statusbar.addWidget(self.status_label)
        RecordSaver.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(RecordSaver)
        self.ffill_ui_data()
        QtCore.QMetaObject.connectSlotsByName(RecordSaver)

    def retranslateUi(self, RecordSaver):
        _translate = QtCore.QCoreApplication.translate
        RecordSaver.setWindowTitle(_translate("RecordSaver", "RecordSaver", None))
        self.label_2.setText(_translate("RecordSaver", "Record Type", None))
        self.label_3.setText(_translate("RecordSaver", "Record Name", None))
        self.label.setText(_translate("RecordSaver", "Save/Restore Location", None))
        self.commandLinkButton.setText(_translate("RecordSaver", "Save Record", None))
        self.commandLinkButton_2.setText(_translate("RecordSaver", "Restore Record", None))
        self.menuHelp.setTitle(_translate("RecordSaver", "Help", None))
    
    def fwire_signals(self):
        #Set the selector for the record type
        self.comboBox.activated.connect(self.controller.fchoicebox_changed)
        for i in range(self.comboBox.count()):
            if self.comboBox.itemText(i) == self.controller.program_defaults["DefaultRecordType"]:
                self.comboBox.setCurrentIndex(i)
        #Wire the command buttons
        self.commandLinkButton.clicked.connect(self.controller.fsave_record)
        self.commandLinkButton_2.clicked.connect(self.controller.frestore_record)
    
    def ffill_ui_data(self):
        #Fill in the combo box
        for rec_type in self.controller.record_dict.keys():
            self.comboBox.addItem(rec_type)
        
    def fwrite_status_message(self,text):
        '''Writes a message on the status bar.
        '''
        self.status_label.setText(text)
        self.status_label.repaint()
        time.sleep(0.01)
        
    def fselect_save_file(self):
        '''Opens up the file saving dialog.
        '''
        filename= QtGui.QFileDialog.getSaveFileName(caption='Choose save file, no extension',directory=self.controller.save_directory,filter='')
        print(filename)
        if filename:
            #Remove any extension from the file
            if "." in filename:
                self.file_text.setText(".".join(filename.split('.')[:-1]))
            else:
                self.file_text.setText(filename)
            self.controller.valid_file = True
            self.controller.save_directory = os.path.dirname(filename)
        else:
            self.controller.valid_file = False
            
    def fselect_open_file(self):
        '''Opens up the file saving dialog.
        '''
        filename = QtGui.QFileDialog.getOpenFileName(caption='Choose file to open',directory=self.controller.save_directory,filter='*.dat')
        print(filename)
        if filename:
            #Remove any extension from the file
            if "." in filename:
                self.file_text.setText(".".join(filename.split('.')[:-1]))
            else:
                self.file_text.setText(filename)
            self.controller.valid_file = True
            self.controller.save_directory = os.path.dirname(filename)
        else:
            self.controller.valid_file = False
    
    def fdisplay_help(self):
        '''Displays a help dialog.
        '''
        help_text = '''        
        This program is intended to aid in saving and restoring 
        the state of individual EPICS records.  This is not a 
        replacement for autosave, simply a way to save a 
        setup for a particular record and restore it 
        at a later time.
        Example applications include:
        * Standard setup for a particular type of stage
        * Restoring a standard scan setup after changes
        
        To run the code:
        1. Type in the record to be saved or restored.  
        Leave off any PV suffixes.
        
        2. Use the center choice box to select the type of record.  
        If this is wrong, saving/restoring will fail.
        
        3. Click either "Save Record" or "Restore Record".  
        The bottom status bar will indicate the status of the 
        saving/restoring.
        
        That's it.  If you want any additional records added, please
        contact me.
        
        Alan Kastengren, 7-BM, APS
        akastengren@anl.gov
        '''
        print(help_text)
        QtGui.QMessageBox.about(RecordSaver, "RecordSaver Help", help_text)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    RecordSaver = QtGui.QMainWindow()
    ui = Ui_RecordSaver()
    ui.setupUi(RecordSaver)
    RecordSaver.show()
    ui.fwire_signals()
    sys.exit(app.exec_())

