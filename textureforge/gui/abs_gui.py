# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class TextureForgeMF
###########################################################################

class TextureForgeMF ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Texture Forge"), pos = wx.DefaultPosition, size = wx.Size( 950,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer19 = wx.BoxSizer( wx.VERTICAL )

        self.Notebook = wx.Notebook( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel1 = wx.Panel( self.Notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel4 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.btn_new_project = wx.Button( self.m_panel4, wx.ID_ANY, _(u"New Project"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.btn_new_project, 0, wx.ALL, 5 )

        self.btn_load_project = wx.Button( self.m_panel4, wx.ID_ANY, _(u"Load Project"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.btn_load_project, 0, wx.ALL, 5 )

        self.btn_save_project = wx.Button( self.m_panel4, wx.ID_ANY, _(u"Save Project"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.btn_save_project, 0, wx.ALL, 5 )


        self.m_panel4.SetSizer( bSizer5 )
        self.m_panel4.Layout()
        bSizer5.Fit( self.m_panel4 )
        bSizer2.Add( self.m_panel4, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel2 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, _(u"Project Settings") ), wx.VERTICAL )

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.lbl_project_name = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, _(u"Name"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_project_name.Wrap( -1 )

        bSizer8.Add( self.lbl_project_name, 1, wx.ALL, 5 )

        self.text_project_name = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.text_project_name, 1, wx.ALL, 5 )


        sbSizer3.Add( bSizer8, 0, wx.EXPAND, 5 )

        bSizer81 = wx.BoxSizer( wx.HORIZONTAL )

        self.lbl_output_dir = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, _(u"Output Directory"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_output_dir.Wrap( -1 )

        bSizer81.Add( self.lbl_output_dir, 1, wx.ALL, 5 )

        self.dp_outputdir = wx.DirPickerCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, _(u"Select a folder"), wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        bSizer81.Add( self.dp_outputdir, 1, wx.ALL, 5 )


        sbSizer3.Add( bSizer81, 0, wx.EXPAND, 5 )


        self.m_panel2.SetSizer( sbSizer3 )
        self.m_panel2.Layout()
        sbSizer3.Fit( self.m_panel2 )
        bSizer7.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel3 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sb_input_maps = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, _(u"Input Maps") ), wx.VERTICAL )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.slots_table = wx.ScrolledWindow( sb_input_maps.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
        self.slots_table.SetScrollRate( 5, 5 )
        bSizer33 = wx.BoxSizer( wx.HORIZONTAL )

        sbSizer20 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText10 = wx.StaticText( self.slots_table, wx.ID_ANY, _(u"Enabled"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        sbSizer20.Add( self.m_staticText10, 0, wx.ALL, 5 )

        self.m_staticline4 = wx.StaticLine( self.slots_table, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        sbSizer20.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

        self.col_enabled = wx.BoxSizer( wx.VERTICAL )

        self.m_checkBox14 = wx.CheckBox( self.slots_table, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox14.SetMinSize( wx.Size( -1,30 ) )

        self.col_enabled.Add( self.m_checkBox14, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_checkBox141 = wx.CheckBox( self.slots_table, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox141.SetMinSize( wx.Size( -1,30 ) )

        self.col_enabled.Add( self.m_checkBox141, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        sbSizer20.Add( self.col_enabled, 0, wx.EXPAND, 5 )


        bSizer33.Add( sbSizer20, 0, wx.EXPAND, 5 )

        sbSizer21 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText101 = wx.StaticText( self.slots_table, wx.ID_ANY, _(u"Texture Path"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText101.Wrap( -1 )

        sbSizer21.Add( self.m_staticText101, 0, wx.ALL, 5 )

        self.m_staticline41 = wx.StaticLine( self.slots_table, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        sbSizer21.Add( self.m_staticline41, 0, wx.ALL|wx.EXPAND, 5 )

        self.col_texture_path = wx.BoxSizer( wx.VERTICAL )

        self.m_filePicker11 = wx.FilePickerCtrl( self.slots_table, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN|wx.FLP_SMALL )
        self.m_filePicker11.SetMinSize( wx.Size( -1,30 ) )

        self.col_texture_path.Add( self.m_filePicker11, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_filePicker111 = wx.FilePickerCtrl( self.slots_table, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_SMALL )
        self.m_filePicker111.SetMinSize( wx.Size( -1,30 ) )

        self.col_texture_path.Add( self.m_filePicker111, 0, wx.ALL|wx.EXPAND, 5 )


        sbSizer21.Add( self.col_texture_path, 1, wx.EXPAND, 5 )


        bSizer33.Add( sbSizer21, 2, wx.EXPAND, 5 )

        sbSizer22 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1011 = wx.StaticText( self.slots_table, wx.ID_ANY, _(u"Compression"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1011.Wrap( -1 )

        sbSizer22.Add( self.m_staticText1011, 0, wx.ALL, 5 )

        self.m_staticline411 = wx.StaticLine( self.slots_table, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        sbSizer22.Add( self.m_staticline411, 0, wx.EXPAND |wx.ALL, 5 )

        self.col_compression = wx.BoxSizer( wx.VERTICAL )

        choice_compressionChoices = []
        self.choice_compression = wx.Choice( self.slots_table, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_compressionChoices, 0 )
        self.choice_compression.SetSelection( 0 )
        self.choice_compression.SetMinSize( wx.Size( -1,30 ) )

        self.col_compression.Add( self.choice_compression, 0, wx.ALL|wx.EXPAND, 5 )

        choice_compression1Choices = []
        self.choice_compression1 = wx.Choice( self.slots_table, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_compression1Choices, 0 )
        self.choice_compression1.SetSelection( 0 )
        self.choice_compression1.SetMinSize( wx.Size( -1,30 ) )

        self.col_compression.Add( self.choice_compression1, 0, wx.ALL|wx.EXPAND, 5 )


        sbSizer22.Add( self.col_compression, 1, wx.EXPAND, 5 )


        bSizer33.Add( sbSizer22, 1, wx.EXPAND, 5 )

        bSizer29 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText101111 = wx.StaticText( self.slots_table, wx.ID_ANY, _(u"Status"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText101111.Wrap( -1 )

        bSizer29.Add( self.m_staticText101111, 0, wx.ALL, 5 )

        self.m_staticline41111 = wx.StaticLine( self.slots_table, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer29.Add( self.m_staticline41111, 0, wx.EXPAND |wx.ALL, 5 )

        self.col_status = wx.BoxSizer( wx.VERTICAL )

        bSizer331 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer331.SetMinSize( wx.Size( -1,35 ) )
        self.m_staticText20 = wx.StaticText( self.slots_table, wx.ID_ANY, _(u"Waiting"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )

        bSizer331.Add( self.m_staticText20, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        self.col_status.Add( bSizer331, 0, wx.EXPAND, 5 )

        bSizer3311 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer3311.SetMinSize( wx.Size( -1,35 ) )
        self.m_staticText201 = wx.StaticText( self.slots_table, wx.ID_ANY, _(u"Waiting"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText201.Wrap( -1 )

        bSizer3311.Add( self.m_staticText201, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        self.col_status.Add( bSizer3311, 0, wx.EXPAND, 5 )


        bSizer29.Add( self.col_status, 1, wx.EXPAND, 5 )


        bSizer33.Add( bSizer29, 0, wx.EXPAND, 5 )

        sbSizer23 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText10111 = wx.StaticText( self.slots_table, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10111.Wrap( -1 )

        sbSizer23.Add( self.m_staticText10111, 0, wx.ALL, 5 )

        self.m_staticline4111 = wx.StaticLine( self.slots_table, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        sbSizer23.Add( self.m_staticline4111, 0, wx.EXPAND |wx.ALL, 5 )

        self.col_actions = wx.BoxSizer( wx.VERTICAL )

        self.btn_delete_slot = wx.Button( self.slots_table, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.col_actions.Add( self.btn_delete_slot, 0, wx.ALL|wx.EXPAND, 5 )

        self.btn_delete_slot1 = wx.Button( self.slots_table, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btn_delete_slot1.SetMinSize( wx.Size( -1,30 ) )

        self.col_actions.Add( self.btn_delete_slot1, 0, wx.ALL|wx.EXPAND, 5 )


        sbSizer23.Add( self.col_actions, 1, wx.EXPAND, 5 )


        bSizer33.Add( sbSizer23, 0, wx.EXPAND, 5 )


        self.slots_table.SetSizer( bSizer33 )
        self.slots_table.Layout()
        bSizer33.Fit( self.slots_table )
        bSizer3.Add( self.slots_table, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

        self.btn_clear_slots = wx.Button( sb_input_maps.GetStaticBox(), wx.ID_ANY, _(u"Clear Slots"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btn_clear_slots.SetMinSize( wx.Size( -1,35 ) )

        bSizer14.Add( self.btn_clear_slots, 0, wx.ALL, 5 )


        bSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_add_slot = wx.Button( sb_input_maps.GetStaticBox(), wx.ID_ANY, _(u"Add Slot"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btn_add_slot.SetMinSize( wx.Size( -1,40 ) )

        bSizer14.Add( self.btn_add_slot, 0, wx.ALL, 5 )


        bSizer3.Add( bSizer14, 0, wx.EXPAND, 5 )


        sb_input_maps.Add( bSizer3, 1, wx.EXPAND, 5 )


        self.m_panel3.SetSizer( sb_input_maps )
        self.m_panel3.Layout()
        sb_input_maps.Fit( self.m_panel3 )
        bSizer7.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer2.Add( bSizer7, 2, wx.EXPAND, 5 )

        self.m_panel9 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer44 = wx.BoxSizer( wx.VERTICAL )

        self.m_gauge1 = wx.Gauge( self.m_panel9, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.m_gauge1.SetValue( 0 )
        bSizer44.Add( self.m_gauge1, 0, wx.ALL|wx.EXPAND, 5 )

        self.btn_convert = wx.Button( self.m_panel9, wx.ID_ANY, _(u"CONVERT"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btn_convert.SetMinSize( wx.Size( -1,40 ) )

        bSizer44.Add( self.btn_convert, 1, wx.ALL|wx.EXPAND, 10 )


        self.m_panel9.SetSizer( bSizer44 )
        self.m_panel9.Layout()
        bSizer44.Fit( self.m_panel9 )
        bSizer2.Add( self.m_panel9, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel5 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel5, wx.ID_ANY, _(u"Output Log") ), wx.VERTICAL )

        self.text_output_log = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        sbSizer5.Add( self.text_output_log, 1, wx.ALL|wx.EXPAND, 5 )


        self.m_panel5.SetSizer( sbSizer5 )
        self.m_panel5.Layout()
        sbSizer5.Fit( self.m_panel5 )
        bSizer2.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )


        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        self.Notebook.AddPage( self.m_panel1, _(u"DDS Converter"), False )

        bSizer19.Add( self.Notebook, 1, wx.EXPAND |wx.ALL, 5 )


        self.m_panel6.SetSizer( bSizer19 )
        self.m_panel6.Layout()
        bSizer19.Fit( self.m_panel6 )
        bSizer1.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 0 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


