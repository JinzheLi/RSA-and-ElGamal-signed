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
## Class de_data
###########################################################################

class de_data(wx.Frame):

    def __init__(self, parent, path, file=True):
        self.file = file
        self.path = path

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(512, 436), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetBackgroundColour('#f0d05b')

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"验证操作", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(24, 70, 90, 90, False, "宋体"))

        bSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"参数设置", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(wx.Font(16, 70, 90, 90, False, "宋体"))

        bSizer3.Add(self.m_staticText2, 0, wx.ALL, 5)

        bSizer1.Add(bSizer3, 1, wx.EXPAND, 5)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"签名文档规范长度", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        self.m_staticText7.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        gSizer2.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.c_len = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.c_len, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"公开参数 n", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        self.m_staticText9.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        gSizer2.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.n = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.n, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"私人密钥 d", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        self.m_staticText10.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        gSizer2.Add(self.m_staticText10, 0, wx.ALL, 5)

        self.d = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.d, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(gSizer2, 1, wx.EXPAND, 5)

        chioce = wx.GridSizer(0, 2, 0, 0)

        if self.file:
            self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"验证文件保存目录", wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_staticText11.Wrap(-1)
            self.m_staticText11.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

            chioce.Add(self.m_staticText11, 0, wx.ALL, 5)

            self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, u"验证文件保存名称", wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_staticText12.Wrap(-1)
            self.m_staticText12.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

            chioce.Add(self.m_staticText12, 0, wx.ALL, 5)

            self.m_file = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition,
                                           wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
            chioce.Add(self.m_file, 0, wx.ALL | wx.EXPAND, 5)

            self.m_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
            chioce.Add(self.m_name, 0, wx.ALL | wx.EXPAND, 5)

            bSizer1.Add(chioce, 1, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"验证操作", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button2, 0, wx.ALL, 5)

        bSizer1.Add(bSizer4, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button2.Bind(wx.EVT_BUTTON, self.de_result)

    def __del__(self):
        self.Destroy()

    # Virtual event handlers, overide them in your derived class
    def de_result(self, event):
        from model.RSA import data_decrypt
        import os
        if self.file:
            res = data_decrypt(n=int(self.n.GetValue()),d=int(self.d.GetValue()),c_max_len=int(self.c_len.GetValue()),
                               c_path=self.path, m_path=os.path.join(self.m_file.GetPath(), self.m_name.GetValue()))
        else:
            res = data_decrypt(n=int(self.n.GetValue()),d=int(self.d.GetValue()),c_max_len=int(self.c_len.GetValue()),
                               c_path=self.path)
        from Gui.RSA.de_result import de_Frame
        self.__del__()
        myframe = de_Frame(None, res)
        myframe.Show(True)