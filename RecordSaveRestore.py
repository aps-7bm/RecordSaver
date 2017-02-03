#!/APSshare/epd/rh6-x86_64/bin/python
'''GUI code for RecordSaveRestore, a code to allow for the saving and
restoring of the critical parameters for a generic record.

Alan Kastengren, XSD, APS

Started: June 26, 2015
'''
#Imports
import wx
from wx.lib.stattext import GenStaticText
import RecordSaveRestoreController as RSRcontroller
import time
import os

class MyApp(wx.App):
    '''Initialization of GUI code.
    '''
    def OnInit(self):
        frame = MainFrame(None,'RecordSaveRestore')
        frame.Show()
        self.SetTopWindow(frame)
        return True

class MainFrame(wx.Frame):
    '''Class for the main window
    '''
    def __init__(self,parent,title):
        #self.controller = controller.PyDMM_Mono_Control(self)
        self.main_font = wx.Font(16,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)
        self.default_directory = os.getcwd() + '/databases'
        self.controller = RSRcontroller.RecordSaveRestoreController(self)
        wx.Frame.__init__(self,parent,title=title,size=(800,220))
        self.main_panel = self.fmake_main_panel(self)
        self.Layout()
        self.Show(True)
        #Now, set the choice box to zero to force the controller to fill the PV list
        self.controller.fchoicebox_changed("")
        self.controller.fclear_PV_list_dict()
    
    def fmake_main_panel(self,parent,color='Gray'):
        #Make the panel
        local_panel = wx.Panel(parent,-1)
        local_panel.SetBackgroundColour(color)
        #Make a vertical BoxSizer to hold two horizontal BoxSizers: controls panel, 
        #table panel, and message 
        overall_sizer = wx.BoxSizer(wx.VERTICAL)
        panels_sizer = wx.BoxSizer(wx.HORIZONTAL)
        panels_sizer.Add(self.fmake_left_panel(local_panel),proportion=0,flag=wx.EXPAND)
        panels_sizer.Add(self.fmake_center_panel(local_panel),proportion=1,flag=wx.EXPAND)
        panels_sizer.Add(self.fmake_right_panel(local_panel),proportion=0,flag=wx.EXPAND)
        overall_sizer.Add(panels_sizer,proportion=1,flag=wx.EXPAND)
        #main_font = wx.Font(16,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_MAX)
        message_sizer = wx.BoxSizer(wx.HORIZONTAL)
        message_text = GenStaticText(local_panel,-1,"Status: ", style=wx.ALIGN_CENTER)
        self.message_label = GenStaticText(local_panel,-1,"Motors in position, ready to move. ")
        message_text.SetFont(self.main_font)
        self.message_label.SetFont(self.main_font)
        message_sizer.Add(message_text,proportion=0)
        message_sizer.AddStretchSpacer()
        message_sizer.Add(self.message_label,0,flag=wx.ALIGN_CENTER)
        message_sizer.AddStretchSpacer()
        overall_sizer.Add(message_sizer,0,wx.EXPAND|wx.TOP,10)
        local_panel.SetSizer(overall_sizer)
        local_panel.Fit()
        return local_panel
    
    def fmake_left_panel(self,parent):    
        '''Make the left-hand side of the window.
        '''
        #Make the panel
        local_panel = wx.Panel(parent,-1)
        local_panel.SetBackgroundColour('Gray')
        local_sizer = wx.GridSizer(rows=3,cols=1)
        for label_text in ['Record Name','Record Type','File Name']:
            label = GenStaticText(local_panel,-1,label_text, style=wx.ALIGN_CENTER)
            label.SetFont(self.main_font)
            local_sizer.Add(label,flag=wx.ALIGN_CENTER_VERTICAL)
#         local_sizer.Add(GenStaticText(local_panel,-1,"Record Name", style=wx.ALIGN_CENTER),flag=wx.ALIGN_CENTER_VERTICAL)
#         local_sizer.Add(GenStaticText(local_panel,-1,"Record Type", style=wx.ALIGN_CENTER),flag=wx.ALIGN_CENTER_VERTICAL)
#         local_sizer.Add(GenStaticText(local_panel,-1,"File Name", style=wx.ALIGN_CENTER),flag=wx.ALIGN_CENTER_VERTICAL)
#         local_sizer.Add(GenStaticText(local_panel,-1,"Path", style=wx.ALIGN_CENTER),flag=wx.ALIGN_CENTER_VERTICAL)
        local_panel.SetSizer(local_sizer)
        local_panel.Fit()
        return local_panel
    
    def fmake_center_panel(self,parent):    
        '''Make the left-hand side of the window.
        '''
        #Make the panel
        local_panel = wx.Panel(parent,-1)
        local_panel.SetBackgroundColour('Gray')
        local_sizer = wx.GridSizer(rows=3,cols=1)
        self.record_text = wx.TextCtrl(local_panel,-1,"7bmb1:scan1")
        self.record_text.SetFont(self.main_font)
        local_sizer.Add(self.record_text,flag=wx.ALIGN_CENTER_VERTICAL|wx.GROW)
        self.record_type_cbox = wx.Choice(local_panel,-1,choices=sorted(self.controller.record_dict.keys()))
        self.record_type_cbox.SetFont(self.main_font)
        self.Bind(wx.EVT_CHOICE,self.controller.fchoicebox_changed,self.record_type_cbox)
        local_sizer.Add(self.record_type_cbox,flag=wx.ALIGN_CENTER_VERTICAL|wx.GROW)
        self.file_text = wx.TextCtrl(local_panel,-1,str(self.default_directory))
        local_sizer.Add(self.file_text,flag=wx.ALIGN_CENTER_VERTICAL|wx.GROW)
        self.file_text.SetFont(self.main_font)
        local_panel.SetSizer(local_sizer)
        local_panel.Fit()
        return local_panel
    
    def fmake_right_panel(self,parent):    
        '''Make the left-hand side of the window.
        '''
        #Make the panel
        local_panel = wx.Panel(parent,-1)
        local_panel.SetBackgroundColour('Gray')
        local_sizer = wx.GridSizer(rows=3,cols=1)
        self.save_record_button = wx.Button(local_panel,-1,'Save Record')
        self.save_record_button.SetFont(self.main_font)
        self.Bind(wx.EVT_BUTTON,self.controller.fsave_record,self.save_record_button)
        local_sizer.Add(self.save_record_button,flag=wx.ALIGN_CENTER)
        self.restore_record_button = wx.Button(local_panel,-1,'Restore Record')
        self.restore_record_button.SetFont(self.main_font)
        self.Bind(wx.EVT_BUTTON,self.controller.frestore_record,self.restore_record_button)
        local_sizer.Add(self.restore_record_button,flag=wx.ALIGN_CENTER)
        self.get_help_button = wx.Button(local_panel,-1,'Get Help')
        self.get_help_button.SetFont(self.main_font)
        self.Bind(wx.EVT_BUTTON,self.fdisplay_help,self.get_help_button)
        local_sizer.Add(self.get_help_button,flag=wx.ALIGN_CENTER)
        local_panel.SetSizer(local_sizer)
        local_panel.Fit()
        return local_panel
    
    def fwrite_status_message(self,text):
        '''Writes a message on the status bar.
        '''
        self.message_label.SetLabel(text)
        self.main_panel.Layout()
        wx.Yield()
        time.sleep(0.01)
        
    def fselect_save_file(self):
        '''Opens up the file saving dialog.
        '''
        dialog=wx.FileDialog(None,'Choose file ',self.default_directory,"","*.dat",wx.SAVE)
        if dialog.ShowModal() == wx.ID_OK:
            #Remove any extension from the file
            if "." in dialog.GetFilename():
                self.file_text.SetValue(".".join(dialog.GetPath().split('.')[:-1]))
            else:
                self.file_text.SetValue(dialog.GetPath())
            self.controller.valid_file = True
        else:
            self.controller.valid_file = False
            
    def fselect_open_file(self):
        '''Opens up the file saving dialog.
        '''
        dialog=wx.FileDialog(None,'Choose file ',self.default_directory,"","*.dat",wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            #Remove any extension from the file
            if "." in dialog.GetFilename():
                self.file_text.SetValue(".".join(dialog.GetPath().split('.')[:-1]))
            else:
                self.file_text.SetValue(dialog.GetPath())
            self.controller.valid_file = True
        else:
            self.controller.valid_file = False
    
    def fdisplay_help(self,event):
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
        The bottom status barwill indicate the status of the 
        saving/restoring.
        
        That's it.  If you want any additional records added, please
        contact me.
        
        Alan Kastengren, 7-BM, APS
        akastengren@anl.gov
        '''
        wx.MessageBox(help_text,'Help Text',wx.OK)
        
app = MyApp(False)
app.MainLoop()
