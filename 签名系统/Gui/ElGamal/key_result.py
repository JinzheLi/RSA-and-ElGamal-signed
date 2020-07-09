#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 14:34
# @Author  : 李金哲
# @Site    : 
# @File    : key_result.py
# @Software: PyCharm

import wx
import wx.xrc
"""
密钥生成结果窗口
"""


class MyDialog5(wx.Frame):

    def __init__(self, parent, lenth):
        from model.ElGamal import get_key

        p, g, y, x = get_key(int(lenth))
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(469, 373), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetBackgroundColour('#f0d05b')

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"公开参数", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(16, 70, 90, 90, False, "宋体"))
        bSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"公钥 p", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        self.m_staticText8.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
        bSizer4.Add(self.m_staticText8, 0, wx.ALL, 5)

        self.p_data = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(420, -1), wx.TE_READONLY)
        self.p_data.SetValue(str(p))
        bSizer4.Add(self.p_data, 0, wx.ALL, 5)

        bSizer1.Add(bSizer4, 1, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"公钥 g", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        self.m_staticText9.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
        bSizer5.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.g_data = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(420, -1), wx.TE_READONLY)
        self.g_data.SetValue(str(g))
        bSizer5.Add(self.g_data, 0, wx.ALL, 5)

        bSizer1.Add(bSizer5, 1, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"公钥 y", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        self.m_staticText10.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
        bSizer6.Add(self.m_staticText10, 0, wx.ALL, 5)

        self.y_data = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(420, -1), wx.TE_READONLY)
        self.y_data.SetValue(str(y))
        bSizer6.Add(self.y_data, 0, wx.ALL, 5)

        bSizer1.Add(bSizer6, 1, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"私人参数", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        self.m_staticText11.SetFont(wx.Font(16, 70, 90, 90, False, "宋体"))
        bSizer7.Add(self.m_staticText11, 0, wx.ALL, 5)

        bSizer1.Add(bSizer7, 1, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, u"私钥 x", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        self.m_staticText13.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
        bSizer8.Add(self.m_staticText13, 0, wx.ALL, 5)

        self.x_data = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(420, -1), wx.TE_READONLY)
        self.x_data.SetValue(str(x))
        bSizer8.Add(self.x_data, 0, wx.ALL, 5)

        bSizer1.Add(bSizer8, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        self.Destroy()
