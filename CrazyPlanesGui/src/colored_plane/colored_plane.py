import wx
from abc import ABC
from CrazyPlanesCore import Plane


class ColoredPlane(Plane, ABC):
    def __init__(self, name, color):
        super().__init__(None)
        self.name = name
        self._color = color

        self.window = None

    def set_game_strategy(self, game_strategy):
        self._game_strategy = game_strategy

    def create_plane(self, parent, size):
        self.window = wx.Window(parent, size=size)
        self.window.Bind(wx.EVT_PAINT, lambda e: self.display())

    def display(self):
        circle = wx.PaintDC(self.window)
        circle.SetBrush(wx.Brush(self._color))
        size = self.window.GetClientSize()
        circle.DrawCircle(size[0]/2-1, size[1]/2-1, size[0]/2.5)

    def clear(self):
        if self.window is not None:
            self.window.Destroy()
