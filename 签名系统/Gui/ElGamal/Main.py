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
## Class Elgamal
###########################################################################

class Elgamal(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"ElGamal数字签名界面", pos=wx.DefaultPosition,
                          size=wx.Size(565, 523), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetBackgroundColour('#f0d05b')

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"ElGamal数字签名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(22, 70, 90, 90, False, "宋体"))
        bSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.long = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        gSizer1.Add(self.long, 0, wx.ALL, 5)

        self.button = wx.Button(self, wx.ID_ANY, u"质数长度(长度应大于等于2位)，生成密钥", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.button, 0, wx.ALL, 5)

        bSizer1.Add(gSizer1, 1, wx.EXPAND, 5)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        self.text = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        gSizer2.Add(self.text, 0, wx.ALL, 5)

        self.file = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition,
                                      wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        gSizer2.Add(self.file, 0, wx.ALL, 5)

        bSizer1.Add(gSizer2, 1, wx.EXPAND, 5)

        gSizer3 = wx.GridSizer(0, 2, 0, 0)

        choice_enChoices = [u"文档签名", u"数据签名"]
        self.choice_en = wx.ComboBox(self, wx.ID_ANY, choice_enChoices[0], wx.DefaultPosition, wx.Size(200, -1),
                                     choice_enChoices,
                                     wx.TE_READONLY)
        gSizer3.Add(self.choice_en, 0, wx.ALL, 5)

        self.button3 = wx.Button(self, wx.ID_ANY, u"签名操作", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer3.Add(self.button3, 0, wx.ALL, 5)

        bSizer1.Add(gSizer3, 1, wx.EXPAND, 5)

        gSizer4 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"签名文档 C1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
        gSizer4.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"签名文档 C2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        self.m_staticText4.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
        gSizer4.Add(self.m_staticText4, 0, wx.ALL, 5)

        bSizer1.Add(gSizer4, 1, wx.EXPAND, 5)

        gSizer6 = wx.GridSizer(0, 2, 0, 0)

        self.c1_file = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition,
                                         wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        gSizer6.Add(self.c1_file, 0, wx.ALL, 5)

        self.c2_file = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition,
                                         wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        gSizer6.Add(self.c2_file, 0, wx.ALL, 5, )

        bSizer1.Add(gSizer6, 1, wx.EXPAND, 5)

        gSizer31 = wx.GridSizer(0, 2, 0, 0)

        choice_deChoices = [u"文档验证", u"数据验证"]
        self.choice_de = wx.ComboBox(self, wx.ID_ANY, choice_deChoices[0], wx.DefaultPosition, wx.Size(200, -1),
                                     choice_deChoices,
                                     wx.TE_READONLY)
        gSizer31.Add(self.choice_de, 0, wx.ALL, 5)

        self.button4 = wx.Button(self, wx.ID_ANY, u"验证操作", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer31.Add(self.button4, 0, wx.ALL, 5)

        self.button5 = wx.Button(self, wx.ID_ANY, u"返回主菜单", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer31.Add(self.button5, 0, wx.ALL, 5)

        bSizer1.Add(gSizer31, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.button.Bind(wx.EVT_BUTTON, self.get_key)
        self.button3.Bind(wx.EVT_BUTTON, self.encrypt)
        self.button4.Bind(wx.EVT_BUTTON, self.decrypt)
        self.button5.Bind(wx.EVT_BUTTON, self.return_menu)

    def __del__(self):
        self.Destroy()

    # Virtual event handlers, overide them in your derived class
    def get_key(self, event):
        if int(self.long.GetValue()) >= 2:
            from Gui.ElGamal.tip import tip
            myframe = tip(None, self.long.GetValue())
            myframe.Show(True)

    def encrypt(self, event):
        choice = self.choice_en.GetValue()
        from Gui.ElGamal.en_data import MyDialog2
        if choice == '文档签名':
            print(self.file.GetPath())
            if self.file.GetPath():
                myframe = MyDialog2(None, path=self.file.GetPath())
                myframe.Show(True)

        else:
            print(self.text.GetValue())
            if self.text.GetValue():
                myframe = MyDialog2(None, data=self.text.GetValue())
                myframe.Show(True)

    def decrypt(self, event):
        choice = self.choice_de.GetValue()
        if choice == '文档验证':
            file = True
        else:
            file = False
        if self.c1_file.GetPath() and self.c2_file.GetPath():
            from Gui.ElGamal.de_data import MyFrame3
            myframe = MyFrame3(None, c1_path=self.c1_file.GetPath(), c2_path=self.c2_file.GetPath(), file=file)
            myframe.Show(True)

    def return_menu(self, event):
        self.__del__()
        from Gui.enter import MyFrame2
        SiteFrame = MyFrame2(None)
        SiteFrame.Show()
