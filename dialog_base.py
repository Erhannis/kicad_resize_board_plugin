# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.1.0-1-ga36064b9)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from .link_toggle import LinkToggle

###########################################################################
## Class ConfigDialogBase
###########################################################################

class ConfigDialogBase ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Resize Board", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText25 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Select a rectangle (board edge), a number of zones (e.g. ground planes), and footprints (mounting hole footprints).  The board will be resized to the new dimensions, the zones will be resized to match minus the new insets, and the footprints will be paired with the nearest corner and inset accordingly.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText25.Wrap( 375 )

        bSizer3.Add( self.m_staticText25, 0, wx.ALL, 5 )

        fgSizer1 = wx.FlexGridSizer( 0, 3, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText1 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Width (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        fgSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_newWidth = wx.SpinCtrlDouble( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10000, 100, 5 )
        self.m_newWidth.SetDigits( 2 )
        fgSizer1.Add( self.m_newWidth, 0, wx.EXPAND|wx.ALL, 5 )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText2 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Height (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        fgSizer1.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_newHeight = wx.SpinCtrlDouble( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10000, 100, 5 )
        self.m_newHeight.SetDigits( 2 )
        fgSizer1.Add( self.m_newHeight, 0, wx.EXPAND|wx.ALL, 5 )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticline112 = wx.StaticLine( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        fgSizer1.Add( self.m_staticline112, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_staticline113 = wx.StaticLine( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        fgSizer1.Add( self.m_staticline113, 0, wx.EXPAND |wx.ALL, 5 )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText3 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Zones inset left", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        fgSizer1.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_zi_left = wx.SpinCtrlDouble( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -100000, 100000, 0, 1 )
        self.m_zi_left.SetDigits( 2 )
        fgSizer1.Add( self.m_zi_left, 0, wx.ALL|wx.EXPAND, 5 )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_linkZonesButton = LinkToggle(self.m_panel)
        self.m_linkZonesButton.SetToolTip( u"Use 'left' value for all zone insets" )

        fgSizer1.Add( self.m_linkZonesButton, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText5 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Zones inset right", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        fgSizer1.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_zi_right = wx.SpinCtrlDouble( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -100000, 100000, 0, 1 )
        self.m_zi_right.SetDigits( 2 )
        self.m_zi_right.Enable( False )

        fgSizer1.Add( self.m_zi_right, 0, wx.ALL, 5 )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText6 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Zones inset top", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        fgSizer1.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_zi_top = wx.SpinCtrlDouble( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -100000, 100000, 0, 1 )
        self.m_zi_top.SetDigits( 2 )
        self.m_zi_top.Enable( False )

        fgSizer1.Add( self.m_zi_top, 0, wx.ALL, 5 )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText61 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Zones inset bottom", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText61.Wrap( -1 )

        fgSizer1.Add( self.m_staticText61, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_zi_bottom = wx.SpinCtrlDouble( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -100000, 100000, 0, 1 )
        self.m_zi_bottom.SetDigits( 2 )
        self.m_zi_bottom.Enable( False )

        fgSizer1.Add( self.m_zi_bottom, 0, wx.ALL, 5 )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticline11 = wx.StaticLine( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        fgSizer1.Add( self.m_staticline11, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline111 = wx.StaticLine( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        fgSizer1.Add( self.m_staticline111, 0, wx.EXPAND |wx.ALL, 5 )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText31 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Hole footprints inset left", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )

        fgSizer1.Add( self.m_staticText31, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_mi_left = wx.SpinCtrlDouble( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -100000, 100000, 0, 1 )
        self.m_mi_left.SetDigits( 2 )
        fgSizer1.Add( self.m_mi_left, 0, wx.ALL, 5 )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_linkMountsButton = LinkToggle(self.m_panel)
        self.m_linkMountsButton.SetToolTip( u"Use 'left' value for all footprint insets" )

        fgSizer1.Add( self.m_linkMountsButton, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText51 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Hole footprints inset right", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText51.Wrap( -1 )

        fgSizer1.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_mi_right = wx.SpinCtrlDouble( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -100000, 100000, 0, 1 )
        self.m_mi_right.SetDigits( 2 )
        self.m_mi_right.Enable( False )

        fgSizer1.Add( self.m_mi_right, 0, wx.ALL, 5 )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText62 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Hole footprints inset top", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText62.Wrap( -1 )

        fgSizer1.Add( self.m_staticText62, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_mi_top = wx.SpinCtrlDouble( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -100000, 100000, 0, 1 )
        self.m_mi_top.SetDigits( 2 )
        self.m_mi_top.Enable( False )

        fgSizer1.Add( self.m_mi_top, 0, wx.ALL, 5 )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText611 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Hole footprints inset bottom", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText611.Wrap( -1 )

        fgSizer1.Add( self.m_staticText611, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_mi_bottom = wx.SpinCtrlDouble( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -100000, 100000, 0, 1 )
        self.m_mi_bottom.SetDigits( 2 )
        self.m_mi_bottom.Enable( False )

        fgSizer1.Add( self.m_mi_bottom, 0, wx.ALL, 5 )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer3.Add( fgSizer1, 1, wx.EXPAND, 5 )

        self.m_staticline1 = wx.StaticLine( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer3.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1OK = wx.Button( self.m_panel, wx.ID_OK )
        m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
        self.m_sdbSizer1Cancel = wx.Button( self.m_panel, wx.ID_CANCEL )
        m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
        m_sdbSizer1.Realize();

        bSizer3.Add( m_sdbSizer1, 0, wx.BOTTOM|wx.EXPAND, 5 )


        self.m_panel.SetSizer( bSizer3 )
        self.m_panel.Layout()
        bSizer3.Fit( self.m_panel )
        bSizer1.Add( self.m_panel, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        bSizer1.Fit( self )

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


