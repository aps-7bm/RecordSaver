# RecordSaver
Python code to save EPICS records locally.  

This program is intended to aid in saving and restoring 
the state of individual EPICS records.  This is not a 
replacement for autosave, simply a way to save a 
setup for a particular record and restore it 
at a later time.
Example applications include:
* Standard setup for a particular type of stage
* Restoring a standard scan setup after changes

The state of the PVs is saved in a user-defined local
location.  These files should be portable between 
beamlines, as only the information on the PV suffixes is
saved, not any information regarding the originating IOC.
        
Dependencies:
This code depends on PyEpics and either PyQt4 or PyQt5, 
aside from built-in Python packages.
For beamline workstations at the APS as of 10/2017, the
PyQt4 version should be used.
This code was written for Python 2.7 and has not been tested
with Python 3.x.

Record types:
The code is set up to save/restore synApps motor, scan,
userCalc, stringSeq, ArrayCalcOut, StringCalcOut, and 
DG645 timing generator records.  More record types can 
easily be added.  Put the suitable *.req file for the
record in the config directory and add a line in the 
config/RecordSaverConfig.xml file.  Follow the pattern 
for the other records.  Please contact me if you have
difficulties.

Setup:
The configuration of the code is in config/RecordSaverConfig.xml.
The main things to change would be the Program Defaults to match
the local installation.

Starting the program:
Go to the src directory of the installation.
For PyQt4 (APS workstations): type python RecordSaverQt4.py
for PyQt5: type python RecordSaver.py


To operate the program:

1. Type in the record to be saved or restored in the top text
entry box.  Leave off any PV suffixes.  

2. Use the center choice box to select the type of record.  
If this is wrong, saving/restoring will fail.

3. Click either "Save Record" or "Restore Record".  
If saving a record, select the directory in which to save
the record.  The data directory in the install is given
as a logical place to save the data.
If restoring a record, select the database file (*.dat) 
containing the record data.
Save/restore operations will start once the destination 
or restore file are selected. 
The bottom status bar will indicate the status of the 
saving/restoring.

That's it.  If you want any additional records added, please
contact me.

Alan Kastengren, 7-BM, APS
akastengren@anl.gov
