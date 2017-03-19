#! /usr/bin/env python
__author__ = 'Rajesh Majumdar'

try:
    from tkinter import *
    import tkinter.scrolledtext as sctx
except:
    from Tkinter import *
    import ScrolledText as sctx


try:
    import ttk
except ImportError:
    from tkinter.ttk import ttk

from downloadbar import downloadbar

def download(tool):

    def yes():
        dframe.destroy()
        strtool = str(tool)
        downloadbar(strtool)


    dframe = Tk()
    dframe.geometry("311x241+465+128")
    dframe.title("Downloading...")
    dframe.configure(background="#d9d9d9")
    dframe.wm_iconbitmap('images/icon.ico')



    TLabel1 = ttk.Label(dframe)
    TLabel1.place(relx=0.26, rely=0.08, height=19, width=166)
    TLabel1.configure(background="#d9d9d9")
    TLabel1.configure(foreground="#000000")
    TLabel1.configure(relief=FLAT)
    TLabel1.configure(text='''You're about to download''')
    TLabel1.configure(width=166)

    ScrolledText1 = sctx.ScrolledText(dframe)
    ScrolledText1.place(relx=0.1, rely=0.21, height=99, width=256)
    ScrolledText1.configure(background="#d9d9d9")
    ScrolledText1.configure(foreground="#000000")
    ScrolledText1.configure(relief=FLAT)
    ScrolledText1.configure(width=256)
    ScrolledText1.insert(END, tool)

    TButton1 = ttk.Button(dframe, command = yes)
    TButton1.place(relx=0.35, rely=0.75, height=25, width=76)
    TButton1.configure(takefocus="")
    TButton1.configure(text='''Continue''')