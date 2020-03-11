import wx
from CrazyPlanesGui.src.colored_plane import ColoredPlane


class PlaneLine(wx.Panel):
    def __init__(self, parent, title):
        super().__init__(parent)

        main_sizer = wx.BoxSizer()
        self.name_ctrl = wx.TextCtrl(self, value=title)
        self.color_picker = wx.ColourPickerCtrl(self)

        main_sizer.Add(self.name_ctrl, 0, wx.ALL, 5)
        main_sizer.Add(self.color_picker, 0, wx.ALL, 5)

        self.SetSizer(main_sizer)

    def get_plane(self):
        return ColoredPlane(
            self.name_ctrl.GetValue(),
            self.color_picker.GetColour()
        )
