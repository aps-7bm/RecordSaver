#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecordSaverSkeleton.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys 
import RecordSaverController as RScontroller
import time
import os

class Ui_RecordSaver(object):
    def __init__(self):
        self.controller = RScontroller.RecordSaveRestoreController(self)
            
    def setupUi(self, RecordSaver):
        RecordSaver.setObjectName("RecordSaver")
        window_size = self.controller.program_defaults["WindowSize"].split(",")
        RecordSaver.resize(int(window_size[0]),int(window_size[1]))
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
        self.file_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.file_text.setObjectName("file_text")
        self.file_text.setText(self.controller.program_defaults['Default_Save_Location'])
        self.gridLayout.addWidget(self.file_text, 2, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(self.controller.program_defaults['Default_Record'])
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.commandLinkButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.gridLayout.addWidget(self.commandLinkButton, 0, 2, 1, 1)
        self.commandLinkButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.gridLayout.addWidget(self.commandLinkButton_2, 1, 2, 1, 1)
        RecordSaver.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RecordSaver)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 776, 29))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.helpAction = QtWidgets.QAction("Help",RecordSaver)
        self.helpAction.triggered.connect(self.fdisplay_help)
        self.menuHelp.addAction(self.helpAction)
        RecordSaver.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RecordSaver)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        self.status_label = QtWidgets.QLabel(self.statusbar)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.status_label.setFont(font)
        self.status_label.setObjectName("Status Label")
        self.status_label.setText("")
        self.status_label.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                     QtWidgets.QSizePolicy.MinimumExpanding)
        self.statusbar.addWidget(self.status_label)
        RecordSaver.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(RecordSaver)
        self.ffill_ui_data()
        QtCore.QMetaObject.connectSlotsByName(RecordSaver)

    def retranslateUi(self, RecordSaver):
        _translate = QtCore.QCoreApplication.translate
        RecordSaver.setWindowTitle(_translate("RecordSaver", "RecordSaver"))
        self.label_2.setText(_translate("RecordSaver", "Record Type"))
        self.label_3.setText(_translate("RecordSaver", "Record Name"))
        self.label.setText(_translate("RecordSaver", "Save/Restore Location"))
        self.commandLinkButton.setText(_translate("RecordSaver", "Save Record"))
        self.commandLinkButton_2.setText(_translate("RecordSaver", "Restore Record"))
        self.menuHelp.setTitle(_translate("RecordSaver", "Help"))
    
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
        filename,__ = QtWidgets.QFileDialog.getSaveFileName(caption='Choose save file, no extension',directory=self.controller.save_directory)
        #print(filename)
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
        filename,__ = QtWidgets.QFileDialog.getOpenFileName(caption='Choose file to open',directory=self.controller.save_directory,filter='*.dat')
        #print(filename)
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
        #print(help_text)
        QtWidgets.QMessageBox.about(RecordSaver, "RecordSaver Help", help_text)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    RecordSaver = QtWidgets.QMainWindow()
    ui = Ui_RecordSaver()
    ui.setupUi(RecordSaver)
    RecordSaver.show()
    ui.fwire_signals()
    sys.exit(app.exec_())

