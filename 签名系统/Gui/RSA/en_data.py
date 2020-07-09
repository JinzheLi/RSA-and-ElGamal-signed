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
## Class en_data
###########################################################################

class en_data(wx.Frame):

    def __init__(self, parent, path=None, m=None):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetBackgroundColour('#f0d05b')

        self.path = path
        self.m = m
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText22 = wx.StaticText(self, wx.ID_ANY, u"签名界面", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        self.m_staticText22.SetFont(wx.Font(24, 70, 90, 90, False, "宋体"))

        bSizer13.Add(self.m_staticText22, 0, wx.ALL, 5)

        bSizer12.Add(bSizer13, 1, wx.EXPAND, 5)

        gSizer7 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText23 = wx.StaticText(self, wx.ID_ANY, u"公开参数 n", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText23.Wrap(-1)
        self.m_staticText23.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        gSizer7.Add(self.m_staticText23, 0, wx.ALL, 5)

        self.n = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer7.Add(self.n, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText24 = wx.StaticText(self, wx.ID_ANY, u"公开参数 e", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText24.Wrap(-1)
        self.m_staticText24.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        gSizer7.Add(self.m_staticText24, 0, wx.ALL, 5)

        self.e = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer7.Add(self.e, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText25 = wx.StaticText(self, wx.ID_ANY, u"签名文档目录", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText25.Wrap(-1)
        self.m_staticText25.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        gSizer7.Add(self.m_staticText25, 0, wx.ALL, 5)

        self.m_staticText26 = wx.StaticText(self, wx.ID_ANY, u"签名文档名称", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText26.Wrap(-1)
        self.m_staticText26.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        gSizer7.Add(self.m_staticText26, 0, wx.ALL, 5)

        self.c_path = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition,
                                       wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        gSizer7.Add(self.c_path, 0, wx.ALL, 5)

        self.c_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer7.Add(self.c_name, 0, wx.ALL | wx.EXPAND, 5)

        bSizer12.Add(gSizer7, 1, wx.EXPAND, 5)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"签名", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_button6, 0, wx.ALL, 5)

        self.SetSizer(bSizer12)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button6.Bind(wx.EVT_BUTTON, self.en_result)

    def __del__(self):
        self.Destroy()

    # Virtual event handlers, overide them in your derived class
    def en_result(self, event):
        from model.RSA import data_encrypt
        import os
        c_path = os.path.join(self.c_path.GetPath(), self.c_name.GetValue())
        if self.path:
            c_path, lenth = data_encrypt(n=int(self.n.GetValue()), e=int(self.e.GetValue()),c_path=c_path, path=self.path)
        elif self.m:
            c_path, lenth = data_encrypt(n=int(self.n.GetValue()), e=int(self.e.GetValue()),c_path=c_path, m=self.m)

        from Gui.RSA.en_result import x_result
        self.__del__()
        myframe = x_result(None, path_1=c_path, len_1=str(lenth))
        myframe.Show(True)
