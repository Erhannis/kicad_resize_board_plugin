"""
Regex replace the references of the selected footprints.
"""

import re
import pcbnew
import os
import wx

from .dialog import ConfigDialog, Config

class GroupRenamePlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "GroupRename"
        self.category = "pcbnew, footprints, group, mass, rename"
        self.description = "Mass regex replace references of selected footprints"
        self.show_toolbar_button = False # Optional, defaults to False
        # self.icon_file_name = os.path.join(os.path.dirname(__file__), 'simple_plugin.png') # Optional, defaults to ""
        self.config = None

    def Run(self):
        board = pcbnew.GetBoard()

        selected_items = [item for item in board.Footprints() if item.IsSelected()]

        if len(selected_items) == 0:
            wx.MessageBox("Select some footprints first!", "GroupRename")
            return

        dialog = ConfigDialog()

        try:
            if self.config != None:
                dialog.SetConfig(self.config)

            if dialog.ShowModal() != wx.ID_OK:
                return

            self.config = dialog.GetConfig()

            for item in selected_items:
                if item.IsSelected():
                    # print(item.GetReferenceAsString())
                    original_ref = item.GetReferenceAsString()
                    new_ref = re.sub(self.config.pattern, self.config.replacement, original_ref)
                    item.SetReference(new_ref)
            
            pcbnew.Refresh()

        finally:
            dialog.Destroy()
    
GroupRenamePlugin().register()