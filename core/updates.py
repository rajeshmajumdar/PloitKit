#! /usr/bin/env python
__author__ = "Rajesh Majumdar"
__version__ = "1.5"

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

import urllib2
import webbrowser
import os

def checkupdates():
    checking = Toplevel()
    checking.geometry("270x192+454+143")
    checking.title("Software Update")
    checking.configure(background='#ffffff')
    #checking.wm_iconbitmap('images/icon.ico')

    def errorbox():
        error = Tk()
        error.geometry("268x82+482+242")
        error.title("Error!")
        error.configure(background="#ffffff")
        #error.wm_iconbitmap('images/icon.ico')

        Label1 = Label(error)
        Label1.place(relx=0.04, rely=0.24, height=21, width=244)
        Label1.configure(background="#ffffff")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(foreground="#000000")
        Label1.configure(text='''Oops! I think you''')
        Label1.configure(width=244)

        Label2 = Label(error)
        Label2.place(relx=0.07, rely=0.49, height=21, width=230)
        Label2.configure(background="#ffffff")
        Label2.configure(disabledforeground="#a3a3a3")
        Label2.configure(foreground="#000000")
        Label2.configure(text='''don't have a working internet connection !''')

        error.mainloop()

    try:
        versionfile = urllib2.urlopen('https://raw.githubusercontent.com/rajeshmajumdar/PloitKit/master/core/version.txt').read()
        if float(versionfile) > float(__version__):
            checking.quit()
            updatefunc()
        else:
            lbl = Label(checking)
            lbl.place(relx=0.04, rely=0.24, height=21, width=244)
            lbl.configure(background="#ffffff")
            lbl.configure(disabledforeground="#a3a3a3")
            lbl.configure(foreground="#000000")
            lbl.configure(text='''Your already have an updated PloitKit.''')
            lbl.configure(width=244)
    except Exception as e:
        errorbox()

    checking.mainloop()

def updatefunc():

    update = Tk()

    update.geometry("270x192+454+143")
    update.title("Software Update")
    update.configure(background='#d9d9d9')
    #update.wm_iconbitmap('images/icon.ico')

    def yes():
        if os.name == 'nt':
            webbrowser.open_new_tab('https://github.com/rajeshmajumdar/PloitKit/archive/master.zip')
            update.destroy()
        else:
            os.system('git clone https://github.com/rajeshmajumdar/PloitKit.git')
            update.destroy()
    def no():
        print 'This thing is also working.'
        update.destroy()

    Label1 = Label(update)
    Label1.place(relx=0.07, rely=0.1, height=21, width=224)
    Label1.configure(background="#d9d9d9")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(foreground="#000000")
    Label1.configure(text='''PloitKit got a new update !''')
    Label1.configure(width=224)

    Button1 = Button(update, command=yes)
    Button1.place(relx=0.19, rely=0.57, height=24, width=69)
    Button1.configure(activebackground="#ffffff")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#d9d9d9")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(foreground="#000000")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady="0")
    Button1.configure(text='''Yes''')
    Button1.configure(width=69)

    Button2 = Button(update, command=no)
    Button2.place(relx=0.52, rely=0.57, height=24, width=67)
    Button2.configure(activebackground="#ffffff")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#d9d9d9")
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(text='''No''')
    Button2.configure(width=67)

    Label2 = Label(update)
    Label2.place(relx=0.07, rely=0.31, height=21, width=213)
    Label2.configure(background="#d9d9d9")
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(foreground="#000000")
    Label2.configure(text='''Do you want to download this update ?''')

    update.mainloop()
