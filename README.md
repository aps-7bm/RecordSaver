# RecordSaver
Python code to save EPICS records.  

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