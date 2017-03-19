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

def mydownloads():
    with open('mydownloads.txt','r') as f:
        toolnames = f.read()


    mydownloadf = Tk()

    mydownloadf.geometry("600x450+431+142")
    mydownloadf.title("My Downloads")
    mydownloadf.configure(background="#d9d9d9")



    Scrolledtext1 = sctx.ScrolledText(mydownloadf)
    Scrolledtext1.place(relx=0.05, rely=0.13, relheight=0.85
                , relwidth=0.9)
    Scrolledtext1.configure(background="white")
    Scrolledtext1.configure(font="TkTextFont")
    Scrolledtext1.configure(foreground="black")
    Scrolledtext1.configure(highlightbackground="#d9d9d9")
    Scrolledtext1.configure(highlightcolor="black")
    Scrolledtext1.configure(insertbackground="black")
    Scrolledtext1.configure(insertborderwidth="3")
    Scrolledtext1.configure(selectbackground="#c4c4c4")
    Scrolledtext1.configure(selectforeground="black")
    Scrolledtext1.configure(width=10)
    Scrolledtext1.configure(wrap=NONE)
    Scrolledtext1.insert(END, toolnames)

    TLabel1 = ttk.Label(mydownloadf)
    TLabel1.place(relx=0.05, rely=0.02, height=39, width=146)
    TLabel1.configure(background="#d9d9d9")
    TLabel1.configure(foreground="#000000")
    TLabel1.configure(relief=FLAT)
    TLabel1.configure(text='''My Downloads''')
    TLabel1.configure(width=146)


