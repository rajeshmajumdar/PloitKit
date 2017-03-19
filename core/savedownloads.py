#! /usr/bin/env python
__author__ = 'Rajesh Majumdar'

from download import download

def savedownloads(toolname):
    with open('mydownloads.txt', 'a') as f:
        f.write(toolname)
    lines = open('mydownloads.txt','r').readlines()
    lines_set = set(lines)
    output = open('mydownloads.txt','w')
    for line in lines_set:
        output.write(line)

def startdownload():
    with open('mydownloads.txt','r') as f:
        downloadinglist = f.read()
        download(downloadinglist)
