import wx
from .plane_line import PlaneLine
from wx.lib.scrolledpanel import ScrolledPanel


class PlaneRegistrationPanel(wx.Panel):
    def __init__(self, parent, set_planes_callback, game_strategy_factory):
        super().__init__(parent)
        self.game_strategy_factory = game_strategy_factory
        self.pickers = []

        title = wx.StaticText(self, label="Set up planes")

        add_button = wx.Button(self, label="Add Plane")
        add_button.Bind(wx.EVT_BUTTON, lambda ev: self.add_picker())

        self.picker_sizer = wx.BoxSizer(wx.VERTICAL)
        self.scrolled_panel = ScrolledPanel(self, size=(300, 150))
        self.scrolled_panel.SetupScrolling()
        self.scrolled_panel.SetSizer(self.picker_sizer)

        btn = wx.Button(self, label="Confirm")
        btn.Bind(wx.EVT_BUTTON, lambda ev: self.get_planes(set_planes_callback))

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(title, 0, wx.ALL | wx.CENTER, 15)
        main_sizer.Add(add_button, 0, wx.ALL | wx.CENTER, 5)
        main_sizer.Add(self.scrolled_panel, 0, wx.ALL | wx.CENTER, 5)
        main_sizer.Add(btn, 0, wx.ALL, 15)

        self.SetSizer(main_sizer)

    def add_picker(self) -> None:
        title = f"Plane #{len(self.pickers) + 1}"
        plane_line = PlaneLine(self.scrolled_panel, title)
        self.pickers.append(plane_line)
        self.picker_sizer.Add(plane_line, 0, wx.ALL | wx.CENTER)
        self.Layout()

    def get_planes(self, set_planes_callback):
        planes = [plane.get_plane() for plane in self.pickers]
        for plane in planes:
            plane.set_game_strategy(self.game_strategy_factory.get_strategy())
        set_planes_callback(planes)
