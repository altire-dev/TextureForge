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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Image Forge"), pos = wx.DefaultPosition, size = wx.Size( 1084,506 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

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

        self.dp_outputdir = wx.DirPickerCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, _(u"Select a folder"), wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
        bSizer81.Add( self.dp_outputdir, 1, wx.ALL, 5 )


        sbSizer3.Add( bSizer81, 0, wx.EXPAND, 5 )


        sbSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_convert = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, _(u"CONVERT"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer3.Add( self.btn_convert, 1, wx.ALL|wx.EXPAND, 10 )


        self.m_panel2.SetSizer( sbSizer3 )
        self.m_panel2.Layout()
        sbSizer3.Fit( self.m_panel2 )
        bSizer7.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel3 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sb_input_maps = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, _(u"Input Maps") ), wx.VERTICAL )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        sb_column_headings = wx.BoxSizer( wx.HORIZONTAL )

        self.label_enabled = wx.StaticText( sb_input_maps.GetStaticBox(), wx.ID_ANY, _(u"Enabled"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_enabled.Wrap( -1 )

        sb_column_headings.Add( self.label_enabled, 1, wx.ALL, 5 )

        self.label_texture_path = wx.StaticText( sb_input_maps.GetStaticBox(), wx.ID_ANY, _(u"Texture Path"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_texture_path.Wrap( -1 )

        sb_column_headings.Add( self.label_texture_path, 5, wx.ALL, 5 )

        self.label_compression_type = wx.StaticText( sb_input_maps.GetStaticBox(), wx.ID_ANY, _(u"Compression"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label_compression_type.Wrap( -1 )

        sb_column_headings.Add( self.label_compression_type, 2, wx.ALL, 5 )


        bSizer3.Add( sb_column_headings, 0, wx.EXPAND, 5 )

        self.m_staticline1 = wx.StaticLine( sb_input_maps.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer3.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        self.slots_scrollbox = wx.ScrolledWindow( sb_input_maps.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
        self.slots_scrollbox.SetScrollRate( 5, 5 )
        self.sb_slots = wx.BoxSizer( wx.VERTICAL )

        sb_slot1 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_checkBox1 = wx.CheckBox( self.slots_scrollbox, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        sb_slot1.Add( self.m_checkBox1, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 10 )

        self.m_filePicker2 = wx.FilePickerCtrl( self.slots_scrollbox, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN|wx.FLP_SMALL )
        sb_slot1.Add( self.m_filePicker2, 5, wx.ALL, 5 )

        m_choice1Choices = []
        self.m_choice1 = wx.Choice( self.slots_scrollbox, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        sb_slot1.Add( self.m_choice1, 2, wx.ALL, 5 )


        self.sb_slots.Add( sb_slot1, 0, wx.EXPAND, 5 )


        self.slots_scrollbox.SetSizer( self.sb_slots )
        self.slots_scrollbox.Layout()
        self.sb_slots.Fit( self.slots_scrollbox )
        bSizer3.Add( self.slots_scrollbox, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

        self.btn_clear_slots = wx.Button( sb_input_maps.GetStaticBox(), wx.ID_ANY, _(u"Clear Slots"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.btn_clear_slots, 0, wx.ALL, 5 )


        bSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_add_slot = wx.Button( sb_input_maps.GetStaticBox(), wx.ID_ANY, _(u"Add Slot"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.btn_add_slot, 0, wx.ALL, 5 )


        bSizer3.Add( bSizer14, 0, wx.EXPAND, 5 )


        sb_input_maps.Add( bSizer3, 1, wx.EXPAND, 5 )


        self.m_panel3.SetSizer( sb_input_maps )
        self.m_panel3.Layout()
        sb_input_maps.Fit( self.m_panel3 )
        bSizer7.Add( self.m_panel3, 3, wx.EXPAND |wx.ALL, 5 )


        bSizer2.Add( bSizer7, 1, wx.EXPAND, 5 )

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
        self.Notebook.AddPage( self.m_panel1, _(u"PNG to DDS"), False )

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


###########################################################################
## Class AbsInputMapSlot
###########################################################################

class AbsInputMapSlot ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

        self.cb_enabled = wx.CheckBox( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cb_enabled.SetValue(True)
        bSizer17.Add( self.cb_enabled, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 10 )

        self.fp_map_path = wx.FilePickerCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN|wx.FLP_SMALL )
        bSizer17.Add( self.fp_map_path, 5, wx.ALL, 5 )

        choice_compressionChoices = []
        self.choice_compression = wx.Choice( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_compressionChoices, 0 )
        self.choice_compression.SetSelection( 0 )
        bSizer17.Add( self.choice_compression, 2, wx.ALL, 5 )


        self.m_panel10.SetSizer( bSizer17 )
        self.m_panel10.Layout()
        bSizer17.Fit( self.m_panel10 )
        bSizer12.Add( self.m_panel10, 1, wx.ALL, 0 )


        self.SetSizer( bSizer12 )
        self.Layout()
        bSizer12.Fit( self )

    def __del__( self ):
        pass


