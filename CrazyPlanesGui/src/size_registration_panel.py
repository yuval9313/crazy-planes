import wx


class SizeRegistrationPanel(wx.Panel):
    def __init__(self, parent, size_callback):
        wx.Panel.__init__(self, parent)

        title = wx.StaticText(self, label="Welcome to Crazy Planes")

        width_sizer = wx.BoxSizer(wx.HORIZONTAL)
        width_label = wx.StaticText(self, label="Width of the board:")

        width = wx.TextCtrl(self)
        width_sizer.Add(width_label, 0, wx.ALL | wx.CENTER, 5)
        width_sizer.Add(width, 0, wx.ALL, 5)

        height_sizer = wx.BoxSizer(wx.HORIZONTAL)
        height_label = wx.StaticText(self, label="Height of the board:")
        height = wx.TextCtrl(self)
        height_sizer.Add(height_label, 0, wx.ALL | wx.CENTER, 5)
        height_sizer.Add(height, 0, wx.ALL, 5)

        btn = wx.Button(self, label="Submit")
        btn.Bind(wx.EVT_BUTTON, lambda ev: size_callback(width.GetValue(), height.GetValue()))

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(title, 0, wx.ALL | wx.CENTER, 15)
        main_sizer.Add(width_sizer, 0, wx.ALL | wx.CENTER, 5)
        main_sizer.Add(height_sizer, 0, wx.ALL | wx.CENTER, 5)
        main_sizer.Add(btn, 0, wx.ALL | wx.CENTER, 15)

        self.SetSizer(main_sizer)

