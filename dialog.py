import wx

from dataclasses import dataclass

from .dialog_base import ConfigDialogBase

@dataclass
class Config:
    pattern: str = ""
    replacement: str = ""
    #CHECK match_entire or something. ?

# Vaguely templated after TransformIt ui
class ConfigDialog(ConfigDialogBase):
    def __init__(self):
        ConfigDialogBase.__init__(self, None)

    def GetConfig(self) -> Config:
        return Config(
            self.m_tb_pattern.Value,
            self.m_tb_replacement.Value
        )
    
    def SetConfig(self, config):
        self.m_tb_pattern.Value = config.pattern
        self.m_tb_replacement.Value = config.replacement
