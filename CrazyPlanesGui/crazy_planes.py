import wx
from concurrent.futures import ThreadPoolExecutor
from CrazyPlanesGui.src import SizeRegistrationPanel, PlaneRegistrationPanel
from CrazyPlanesGui.src.factories import StandardFactory
from CrazyPlanesGui.src.game_board import GameBoardGui


class MainFrame(wx.Frame):
    def __init__(self, title, size):
        super().__init__(None, wx.ID_ANY, title=title, size=size)
        self._stage = 0
        self.width, self.height = 0, 0
        self.planes = []
        self.game_strategy_factory = StandardFactory()

        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.size_registration = SizeRegistrationPanel(self, self.set_sizes)
        self.plane_registration = PlaneRegistrationPanel(self, self.set_planes, self.game_strategy_factory)
        self.plane_registration.Hide()

        self.game_board = GameBoardGui(self)
        self.game_board.Hide()

        self.main_sizer.Add(self.size_registration, 1, wx.EXPAND)
        self.main_sizer.Add(self.plane_registration, 1, wx.EXPAND)
        self.main_sizer.Add(self.game_board, 1, wx.EXPAND)

        self.SetSizer(self.main_sizer)

    def switch_panel(self):
        self._stage += 1
        if self._stage == 1:
            self.size_registration.Destroy()
            self.plane_registration.Show()
        elif self._stage == 2:
            self.plane_registration.Destroy()
            self.game_board.Show()
        self.Layout()

    def set_sizes(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.game_strategy_factory.set_size(self.width, self.height)
        self.game_board.create_grid(self.width, self.height)
        self.switch_panel()

    def set_planes(self, planes):
        self.planes = planes
        self.game_board.initiate_game(planes)
        self.switch_panel()


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame("Crazy Planes", size=(800, 600))
    frame.Show()
    app.MainLoop()
