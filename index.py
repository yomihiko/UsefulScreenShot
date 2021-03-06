#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Oct 16, 2021 02:09:06 PM JST  platform: Windows NT

import sys
import threading

import tkinter as tk
from models.path import Path
from controller import Controller
from functools import partial

def vp_start_gui():
    root = tk.Tk()
    MainPanel (root)
    root.mainloop()

class MainPanel:
    def __init__(self, top: tk.Tk):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("450x220+672+405")
        top.resizable(0,  0)
        top.title("高性能スクリーンショット")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.protocol("WM_DELETE_WINDOW", lambda: self.controller.shutDown(top))

        self.SaveFolderEntry = tk.Entry(top)
        self.SaveFolderEntry.place(relx=0.244, rely=0.186, height=20
                , relwidth=0.564)
        self.SaveFolderEntry.configure(background="white")
        self.SaveFolderEntry.configure(disabledforeground="#a3a3a3")
        self.SaveFolderEntry.configure(font="TkFixedFont")
        self.SaveFolderEntry.configure(foreground="#000000")
        self.SaveFolderEntry.configure(highlightbackground="#d9d9d9")
        self.SaveFolderEntry.configure(highlightcolor="black")
        self.SaveFolderEntry.configure(insertbackground="black")
        self.SaveFolderEntry.configure(selectbackground="blue")
        self.SaveFolderEntry.configure(selectforeground="white")
        self.SaveFolderEntry.configure(state="readonly")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.067, rely=0.182, height=21, width=77)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''保存先フォルダ''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.RefButton = tk.Button(top)
        self.RefButton.place(relx=0.822, rely=0.182, height=24, width=35)
        self.RefButton.configure(activebackground="#ececec")
        self.RefButton.configure(activeforeground="#000000")
        self.RefButton.configure(background="#d9d9d9")
        self.RefButton.configure(disabledforeground="#a3a3a3")
        self.RefButton.configure(foreground="#000000")
        self.RefButton.configure(highlightbackground="#d9d9d9")
        self.RefButton.configure(highlightcolor="black")
        self.RefButton.configure(pady="0")
        self.RefButton.configure(text='''参照''')
        self.RefButton.configure(command=lambda: self.controller.onClickFolderRef(self.SaveFolderEntry))
        self.SaveFolderEntry.insert(0, "a")

        self.Title = tk.Label(top)
        self.Title.place(relx=0.244, rely=0.0, height=41, width=234)
        self.Title.configure(activebackground="#f9f9f9")
        self.Title.configure(activeforeground="black")
        self.Title.configure(background="#d9d9d9")
        self.Title.configure(disabledforeground="#a3a3a3")
        self.Title.configure(font="-family {Yu Gothic UI} -size 18 -weight bold")
        self.Title.configure(foreground="#000000")
        self.Title.configure(highlightbackground="#d9d9d9")
        self.Title.configure(highlightcolor="black")
        self.Title.configure(text='''高性能スクリーンショット''')

        self.RangeButton = tk.Button(top)
        self.RangeButton.place(relx=0.089, rely=0.409, height=24, width=367)
        self.RangeButton.configure(activebackground="#ececec")
        self.RangeButton.configure(activeforeground="#000000")
        self.RangeButton.configure(background="#d9d9d9")
        self.RangeButton.configure(disabledforeground="#a3a3a3")
        self.RangeButton.configure(foreground="#000000")
        self.RangeButton.configure(highlightbackground="#d9d9d9")
        self.RangeButton.configure(highlightcolor="black")
        self.RangeButton.configure(pady="0")
        self.RangeButton.configure(text='''範囲指定''')
        self.RangeButton.configure(command=lambda: self.controller.onClickRangeBtn())

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.12, rely=0.286, height=21, width=54)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''ファイル名''')

        self.FileNameEntry = tk.Entry(top)
        self.FileNameEntry.place(relx=0.244, rely=0.291, height=20
                , relwidth=0.564)
        self.FileNameEntry.configure(background="white")
        self.FileNameEntry.configure(disabledforeground="#a3a3a3")
        self.FileNameEntry.configure(font="TkFixedFont")
        self.FileNameEntry.configure(foreground="#000000")
        self.FileNameEntry.configure(insertbackground="black")
        self.FileNameEntry.bind("<Return>", lambda e: self.controller.saveFileNameFormat(e, self.FileNameEntry))

        self.controller = Controller()

        self.FileNameEntry.insert(0, self.controller.image.fileNameFormat)

if __name__ == '__main__':
    vp_start_gui()





