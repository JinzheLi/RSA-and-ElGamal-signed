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
## Class key_result
###########################################################################

class key_result(wx.Frame):

    def __init__(self, parent, p_len, q_len):

        from model.RSA import get_key
        n, e, d = get_key(len1=p_len, len2=q_len)

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u'密钥信息', pos=wx.DefaultPosition,
                          size=wx.Size(467, 355), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetBackgroundColour('#f0d05b')

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText15 = wx.StaticText(self, wx.ID_ANY, u"生成密钥结果", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)
        self.m_staticText15.SetFont(wx.Font(24, 70, 90, 90, False, "宋体"))

        bSizer7.Add(self.m_staticText15, 0, wx.ALL, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText16 = wx.StaticText(self, wx.ID_ANY, u"公开参数", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)
        self.m_staticText16.SetFont(wx.Font(16, 70, 90, 90, False, "宋体"))

        bSizer10.Add(self.m_staticText16, 1, wx.ALL | wx.EXPAND, 5)

        gSizer5 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"公钥 n", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        self.m_staticText17.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        gSizer5.Add(self.m_staticText17, 0, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), wx.TE_READONLY)
        self.m_textCtrl7.SetValue(str(n))
        gSizer5.Add(self.m_textCtrl7, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, u"公钥 e", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)
        self.m_staticText18.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        gSizer5.Add(self.m_staticText18, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl8 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), wx.TE_READONLY)
        self.m_textCtrl8.SetValue(str(e))
        gSizer5.Add(self.m_textCtrl8, 1, wx.ALL | wx.EXPAND, 5)

        bSizer10.Add(gSizer5, 1, wx.EXPAND, 5)

        bSizer7.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText19 = wx.StaticText(self, wx.ID_ANY, u"私人参数", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText19.Wrap(-1)
        self.m_staticText19.SetFont(wx.Font(16, 70, 90, 90, False, "宋体"))

        bSizer11.Add(self.m_staticText19, 1, wx.ALL, 5)

        gSizer6 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText20 = wx.StaticText(self, wx.ID_ANY, u"私钥 d", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText20.Wrap(-1)
        self.m_staticText20.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        gSizer6.Add(self.m_staticText20, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl9 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), wx.TE_READONLY)
        self.m_textCtrl9.SetValue(str(d))
        gSizer6.Add(self.m_textCtrl9, 1, wx.ALL | wx.EXPAND, 5)

        bSizer11.Add(gSizer6, 1, wx.EXPAND, 5)

        bSizer7.Add(bSizer11, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        self.Destroy()
