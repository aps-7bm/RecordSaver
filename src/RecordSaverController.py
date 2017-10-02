'''Controller code for the RecordSaver program.

Alan Kastengren, XSD, APS

Started: June 29, 2015

Updates:
February 4, 2016: Add try/except block on update so things don't hang if a PV fails to update.  Having problems with the motor record's .DISP field.
'''
import epics
import os
import os.path
import shelve
import anydbm
import xml.etree.ElementTree as ET
anydbm._defaultmod = __import__('dumbdbm')
import time

connection_timeout = 5  #seconds to wait for PV to connect

class RecordSaveRestoreController():
    def __init__(self,GUI_object):
        self.valid_PVs = False          #Flag for whether PVs actually work
        self.valid_file = False         #Flag for whether we have a save/restore file to use
        self.valid_DB = False           #Flag for whether database actually matches
        self.GUI_object = GUI_object
        self.program_defaults = {}
        self.fparse_config_file()
        self.save_directory = self.program_defaults['Default_Save_Location']
        
    def fparse_config_file(self):
        '''Parse the XML config file.
        '''
        config_tree = ET.parse(os.path.abspath('../config') + '/RecordSaverConfig.xml')
        config_root = config_tree.getroot()
        self.record_dict = {}
        self.separator_dict = {}
        for child in config_root:
            print(child.tag)
            if child.tag == 'ProgramDefaults':
                print(child.attrib)
                self.program_defaults = child.attrib
            elif child.tag == 'RecordTypes':
                for rec in child:
                    print(rec.attrib["FileName"])
                    self.record_dict[rec.tag] = rec.attrib["FileName"]
                    self.separator_dict[rec.tag] = rec.attrib["Separator"]
        print(self.record_dict)
        print(self.separator_dict)
    
    def fparse_req_file(self,record_name):
        '''Parses the .req file to get the correct EPICS PVs.
        '''
        #Figure out which req file to use
        selected_record_type = str(self.GUI_object.comboBox.currentText())
        req_filename = self.record_dict[selected_record_type]
        with open(os.path.join(os.path.abspath('../config') + '/' + req_filename),'r') as req_file:
            #Trap for blank lines
            blank_lines = 0
            while blank_lines < 3:
                line = req_file.readline()
                if line == None or len(line) < 2:
                    blank_lines += 1
                    continue
                #Trap to skip comment lines
                if line.startswith("#"):
                    continue
                print line
                #Remove ending "$" if it exists
                req_suffix = line.split('.')[1].strip()
                if req_suffix[-1] == '$':
                    self.PV_list.append(record_name + req_suffix[:-1])
                else:
                    self.PV_list.append(record_name + req_suffix)
        print self.PV_list
        self.GUI_object.fwrite_status_message("List of PVs read in")
    
    def fvalidate_PV_list(self):
        '''Tries to connect to all PVs to make sure they exist.
        '''
        self.GUI_object.fwrite_status_message("Attempting to connect PVs") 
        for PV_name in self.PV_list:
            PV_obj = epics.PV(PV_name)
            #If things connect, add to the list
            if PV_obj.wait_for_connection(connection_timeout):
                self.PV_dict[PV_name] = PV_obj
                self.GUI_object.fwrite_status_message("PV " + PV_name + " connected")
            else:           #We didn't connect
                self.fclear_PV_list_dict("PV " + PV_name + " failed to connect")               
                return 
        #If we got here, everything worked
        self.GUI_object.fwrite_status_message("PVs successfully connected") 
        self.valid_PVs = True
        return
         
    def fvalidate_db_file(self,db_filename):
        '''Parses the database file to make sure PVs match req file.
        '''
        try:
            #Try to open a shelve object 
            db_dict = shelve.open(db_filename,'r') 
            #Loop through the suffixes, making sure they match entries in PV list
            for db_suffix in db_dict.keys():
                if self.record_name+db_suffix not in self.PV_list:
                    self.fclear_PV_list_dict("Mismatch between database and PV list.")
                    return
                else:
                    print(self.record_name + db_suffix)
                    self.GUI_object.fwrite_status_message("DB file match: " + self.record_name + db_suffix)
            self.GUI_object.fwrite_status_message("DB file check complete")
            self.GUI_object.status_label.repaint()
            self.valid_DB = True
        finally:
            if db_dict:
                db_dict.close()

    def fclear_PV_list_dict(self,message='Ready for selections'):
        self.PV_list = []
        self.PV_dict = {}
        self.valid_file = False
        self.valid_PVs = False
        self.valid_DB = False
        self.GUI_object.fwrite_status_message(message)
        
    def fsave_record(self,event):
        self.fchoicebox_changed()
        self.GUI_object.fselect_save_file()
        if self.valid_file:
            self.fvalidate_PV_list()
        else:
            self.fclear_PV_list_dict("No valid file selected")
            return
        if self.valid_PVs:
            self.fwrite_values_to_file()

    def frestore_record(self,event):
        self.fchoicebox_changed()
        self.GUI_object.fselect_open_file()
        db_filename = self.GUI_object.file_text.text()
        print db_filename
        if self.valid_file:
            self.fvalidate_PV_list()
        else:
            self.fclear_PV_list_dict("No valid file selected")
            return
        if self.valid_PVs:
            self.fvalidate_db_file(db_filename)
            if self.valid_DB:
                self.frestore_values_from_file(db_filename)
                          
    def fchoicebox_changed(self):
        self.fclear_PV_list_dict()
        selected_record_type = str(self.GUI_object.comboBox.currentText())
        self.separator = self.separator_dict[selected_record_type]
        self.record_name = str(self.GUI_object.lineEdit.displayText()) + self.separator
        self.fparse_req_file(self.record_name)
        print("changed")
        print self.GUI_object.comboBox.count()
    
    def fwrite_values_to_file(self):
        '''Read the PVs from EPICS and save to file.
        '''    
        #Make a shelve object to hold the suffixes and values
        print self.GUI_object.file_text.text()
        pv_database = shelve.open(self.GUI_object.file_text.text(),'n')
        self.GUI_object.fwrite_status_message("Database opened successfully")
        #Loop through the suffixes and values
        for PV_name in self.PV_list:
            suffix = str(PV_name.split(self.separator)[-1])
            print suffix
            print self.PV_dict[PV_name]
            print self.PV_dict[PV_name].value
            pv_database[suffix] = str(self.PV_dict[PV_name].value)
        #Close the shelve object
        pv_database.close()
        #Write a message that things were saved correctly
        self.GUI_object.fwrite_status_message("Database written successfully") 

    def frestore_values_from_file(self,db_filename):
        '''Read the PVs from the database and restore to EPICS.
        ''' 
        failed_PVs = [] 
        timeout_time = float(elf.program_defaults['CA_Timeout'])      
        try:
            #Try to open a shelve object 
            db_dict = shelve.open(db_filename,'r') 
            #Loop through the suffixes, setting value of PVs to the entry from the database
            #Loop through the PV_name list to keep the same order as req file
            for PV_name in self.PV_list:
                print "Restoring " + PV_name
                db_suffix = PV_name.split(self.separator)[-1]
                print(db_dict[db_suffix])
                try:
                    self.PV_dict[PV_name].put(str(db_dict[db_suffix]),timeout=timeout_time)
                    self.GUI_object.fwrite_status_message("PV " + self.record_name+db_suffix + " restored") 
                except:
                    print(PV_name + ' failed to update!')
                    failed_PVs.append(PV_name)
        finally:
            if db_dict:
                db_dict.close()   
        #Write a message that things were saved correctly
        if failed_PVs:
            self.GUI_object.fwrite_status_message("Record restored, PVs: " + str(failed_PVs) + " failed to update.")
        else:
            self.GUI_object.fwrite_status_message("Record restored successfully.")

if __name__ == '__main__':
    __ = RecordSaveRestoreController(None)
