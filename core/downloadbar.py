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

from urllib2 import *
import requests.packages.urllib3
import requests
requests.packages.urllib3.disable_warnings()

from downloadurl import geturl
from finaldownload import download

def downloadbar(tool):
    link = geturl()
    download(link)
