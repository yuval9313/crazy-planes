import wx


class ScoreBoard(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.scores = {}

    def generate_board(self, board_initial_state):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(10, 0, 0, 0)
        for plane in board_initial_state:
            plane_sizer = wx.BoxSizer()
            plane_title = wx.StaticText(self, label=f"{plane.name}: ")
            plane_score = wx.TextCtrl(self, style=wx.TE_READONLY | wx.BORDER_NONE, value=f"{plane.score}")

            plane_sizer.Add(plane_title, 0, wx.ALL, 5)
            plane_sizer.Add(plane_score, 0, wx.ALL, 5)
            self.scores[plane] = plane_score
            main_sizer.Add(plane_sizer, 0, wx.ALL, 3)

        self.SetSizer(main_sizer)
        self.Layout()

    def render(self, board_state):
        for plane in board_state:
            self.scores[plane].SetValue(f"{plane.score}")

        self.Layout()
