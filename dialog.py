import wx

from dataclasses import dataclass

from .dialog_base import ConfigDialogBase

@dataclass
class Config:
    new_width: float = 100
    new_height: float = 100
    planes_inset_left: float = 1
    planes_inset_right: float = 1 
    planes_inset_top: float = 1 
    planes_inset_bottom: float = 1 
    mounts_inset_left: float = 4 
    mounts_inset_right: float = 4 
    mounts_inset_top: float = 4
    mounts_inset_bottom: float = 4
    #CHECK match_entire or something. ?

# Vaguely templated after TransformIt ui
class ConfigDialog(ConfigDialogBase):
    def __init__(self):
        ConfigDialogBase.__init__(self, None)
        self.Bind(wx.EVT_TOGGLEBUTTON, self.OnLinkZonesToggle, self.m_linkZonesButton)
        self.Bind(wx.EVT_TOGGLEBUTTON, self.OnLinkMountsToggle, self.m_linkMountsButton)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.OnZoneInsetLeftChange, self.m_zi_left)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.OnMountInsetLeftChange, self.m_mi_left)

    def GetConfig(self) -> Config:
        return Config(
            self.m_newWidth.Value,
            self.m_newHeight.Value,
            self.m_zi_left.Value,
            self.m_zi_right.Value,
            self.m_zi_top.Value,
            self.m_zi_bottom.Value,
            self.m_mi_left.Value,
            self.m_mi_right.Value,
            self.m_mi_top.Value,
            self.m_mi_bottom.Value
        )
    
    def SetConfig(self, config):
        self.m_newWidth.Value = config.new_width
        self.m_newHeight.Value = config.new_height
        self.m_zi_left.Value = config.planes_inset_left
        self.m_zi_right.Value = config.planes_inset_right
        self.m_zi_top.Value = config.planes_inset_top
        self.m_zi_bottom.Value = config.planes_inset_bottom
        self.m_mi_left.Value = config.mounts_inset_left
        self.m_mi_right.Value = config.mounts_inset_right
        self.m_mi_top.Value = config.mounts_inset_top
        self.m_mi_bottom.Value = config.mounts_inset_bottom

    def OnLinkZonesToggle(self, event: wx.CommandEvent):
        if event.GetEventObject().GetValue():
            self.m_zi_right.Enable(False)
            self.m_zi_right.SetValue(self.m_zi_left.Value)
            self.m_zi_top.Enable(False)
            self.m_zi_top.SetValue(self.m_zi_left.Value)
            self.m_zi_bottom.Enable(False)
            self.m_zi_bottom.SetValue(self.m_zi_left.Value)
        else:
            self.m_zi_right.Enable()
            self.m_zi_top.Enable()
            self.m_zi_bottom.Enable()

    def OnLinkMountsToggle(self, event: wx.CommandEvent):
        if event.GetEventObject().GetValue():
            self.m_mi_right.Enable(False)
            self.m_mi_right.SetValue(self.m_mi_left.Value)
            self.m_mi_top.Enable(False)
            self.m_mi_top.SetValue(self.m_mi_left.Value)
            self.m_mi_bottom.Enable(False)
            self.m_mi_bottom.SetValue(self.m_mi_left.Value)
        else:
            self.m_mi_right.Enable()
            self.m_mi_top.Enable()
            self.m_mi_bottom.Enable()

    def OnZoneInsetLeftChange(self, event: wx.CommandEvent):
        if self.m_linkZonesButton.Value:
            self.m_zi_right.SetValue(self.m_zi_left.Value)
            self.m_zi_top.SetValue(self.m_zi_left.Value)
            self.m_zi_bottom.SetValue(self.m_zi_left.Value)

    def OnMountInsetLeftChange(self, event: wx.CommandEvent):
        if self.m_linkMountsButton.Value:
            self.m_mi_right.SetValue(self.m_mi_left.Value)
            self.m_mi_top.SetValue(self.m_mi_left.Value)
            self.m_mi_bottom.SetValue(self.m_mi_left.Value)
