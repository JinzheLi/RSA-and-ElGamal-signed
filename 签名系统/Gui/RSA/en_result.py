# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class x_result
###########################################################################
"""
产生加密结果界面
"""
class x_result(wx.Frame):

    def __init__(self, parent, path_1, len_1):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"签名结果", pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_DIALOG_STYLE)

        self.SetBackgroundColour('#f0d05b')

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        gSizer8 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"签名文档 c 地址", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        self.m_staticText8.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
        gSizer8.Add(self.m_staticText8, 0, wx.ALL | wx.EXPAND, 5)

        self.c1_path = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(230, -1), wx.TE_READONLY)
        self.c1_path.SetValue(path_1)
        gSizer8.Add(self.c1_path, 0, wx.ALL, 5)

        bSizer5.Add(gSizer8, 1, wx.EXPAND, 5)

        gSizer9 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"签名文档 c 规范长度", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        self.m_staticText9.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
        gSizer9.Add(self.m_staticText9, 0, wx.ALL | wx.EXPAND, 5)

        self.c1_len = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(230, -1), wx.TE_READONLY)
        self.c1_len.SetValue(len_1)
        gSizer9.Add(self.c1_len, 0, wx.ALL, 5)

        bSizer5.Add(gSizer9, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        self.Destroy()
