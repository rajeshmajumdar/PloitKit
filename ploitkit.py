#!/usr/bin/env python
__author__ = "Rajesh Majumdar"

import os
try:
    import urllib.request as urllib2
except:
    import urllib2

def main():
    path = os.getcwd()
    command = path+'/core/background.py'
    if os.name == 'nt':
        os.system(command)
    else:
        os.system('python '+command)
main()
