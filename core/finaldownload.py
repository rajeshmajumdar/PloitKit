#!/usr/bin/env python
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

from urllib2 import *
import requests.packages.urllib3
import requests
requests.packages.urllib3.disable_warnings()
import os
import sys
import ssl

def download(link):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    print link
    g = 'github'
    sf = 'sourceforge'
    if g in link:
        file_name = link.split('/')[-3]
        final_name = file_name+'.zip'
        fullfinalname = os.path.join('Downloads/',final_name)
    elif sf in link:
        if 'ace' in link:
            file_name = 'ace-voip'
            final_name = 'ace-1.10.tar.gz'
            fullfinalname = os.path.join('Downloads/',final_name)
        elif 'dnmap' in link:
            file_name = 'DNMap'
            final_name = 'dnmap_v0.6.tgz'
            fullfinalname = os.path.join('Downloads/',final_name)
        elif 'dnswalk' in link:
            file_name = 'DNSWalk'
            final_name = 'dnswalk-2.0.2.tar.gz'
            fullfinalname = os.path.join('Downloads/',final_name)
        elif 'enumiax' in link:
            file_name = 'enumiax'
            final_name = 'enumiax-0.4a.tar.gz'
            fullfinalname = os.path.join('Downloads/',final_name)
        elif 'xplico' in link:
            file_name = 'XPlico'
            final_name = 'xplico-1.1.2.tgz'
            fullfinalname = os.path.join('Downloads/',final_name)
    else:
        file_name = link.split("/")[-1]
        final_name = file_name
        fullfinalname = os.path.join('Downloads/',final_name)
    top = Tk()
    top.geometry("322x89+466+161")
    top.configure(background="#d9d9d9")
    top.wm_iconbitmap('images/icon.ico')



    TProgressbar1 = ttk.Progressbar(top)
    TProgressbar1.place(relx=0.09, rely=0.56, relwidth=0.78
                , relheight=0.0, height=22)
    TProgressbar1.configure(length="200")
    TProgressbar1.configure(mode="determinate")

    TLabel1 = ttk.Label(top)
    TLabel1.place(relx=0.09, rely=0.11, height=29, width=236)
    TLabel1.configure(background="#d9d9d9")
    TLabel1.configure(foreground="#000000")
    TLabel1.configure(relief=FLAT)
    TLabel1.configure(text='''Downloading '''+file_name+'''...''')
    TLabel1.configure(width=236)

    url = urlopen(link, context=ctx)
    html = url.info()
    try:
        cl = html['Content-Length']
    except KeyError:
        executable = sys.executable
        args = sys.argv[:]
        args.insert(0, sys.executable)
        os.execvp(executable, args)
    f = open(fullfinalname,'wb+')
    fl=0
    TProgressbar1.start()
    while 1:
        xr = url.read(1024)
        fl+=len(xr)
        TProgressbar1.update()
        top.title(file_name+' %s%s'%(fl*100/int(cl),'%'))
        TProgressbar1["maximum"]=100
        TProgressbar1["value"]=fl*100/int(cl)
        f.write(xr)
        if not xr:break
        del xr
    f.close()
    TProgressbar1.stop()

    def downloaded(name):
        top.destroy()
        def OK():
            downloadedw.destroy()
            executable = sys.executable
            args = sys.argv[:]
            args.insert(0, sys.executable)
            os.execvp(executable, args)

        downloadedw = Tk()
        downloadedw.geometry("302x98+479+151")
        downloadedw.configure(background="#d9d9d9")
        downloadedw.wm_iconbitmap('images/icon.ico')

        TLabel1 = ttk.Label(downloadedw)
        TLabel1.place(relx=0.07, rely=0.2, height=19, width=256)
        TLabel1.configure(background="#d9d9d9")
        TLabel1.configure(foreground="#000000")
        TLabel1.configure(relief=FLAT)
        TLabel1.configure(text=name+''' has been downloaded.''')
        TLabel1.configure(width=256)

        TButton1 = ttk.Button(downloadedw, command=OK)
        TButton1.place(relx=0.36, rely=0.61, height=25, width=76)
        TButton1.configure(takefocus="")
        TButton1.configure(text='''OK''')

    downloaded(file_name)

    top.mainloop()
