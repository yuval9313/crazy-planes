import time

import wx
from CrazyPlanesCore import GameBoard
from CrazyPlanesGui.src.score_board import ScoreBoard


class GameBoardGui(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self._done = False
        self.width = 0
        self.height = 0
        self.game = None

        title = wx.StaticText(self, label="Game!")

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, lambda ev: self.run(), self.timer)

        self.panels = []
        self.grid = None
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.main_sizer.Add(title, 0, wx.ALL | wx.CENTER, 15)

        self.score_board = ScoreBoard(self)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.score_board, 0, wx.ALL)
        sizer.Add(self.main_sizer, 0, wx.ALL)

        self.SetSizer(sizer)

    def create_grid(self, width, height):
        self.width = width
        self.height = height

        self.grid = wx.FlexGridSizer(rows=width, cols=height, vgap=0, hgap=0)
        for i in range(width * height):
            self.panels.append(wx.Panel(self, style=wx.SIMPLE_BORDER | wx.EXPAND, size=(width*5, height*5)))

        self.grid.AddMany(self.panels)
        self.main_sizer.Add(self.grid, 0, wx.ALL | wx.CENTER, 5)
        self.Layout()

    def initiate_game(self, planes):
        self.game = GameBoard(self.width, self.height, planes)
        self.score_board.generate_board(self.game.board_state)
        self.timer.Start(300)

    def run(self):
        if not self._done:
            state = self.game.run()
            self._done = self.game.check_if_done()
            for plane in state:
                plane.clear()
                pos = plane.pos
                panel = self.panels[pos[0] + pos[1] * self.height]
                plane.create_plane(panel, panel.GetClientSize())
                self.Layout()

        else:
            self.timer.Stop()

        self.score_board.render(self.game.board_state)
