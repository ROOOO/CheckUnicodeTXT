#!/usr/bin/env python
#encoding: utf-8
import binascii
import os
import re

def func(fileName):
    fh = open(fileName, 'rb')
    a = fh.read()
    hexstr = binascii.b2a_hex(a)
    bsstr = hex(int(hexstr,16))[2:]
    if bsstr[1] != 'f':
        print fileName
    fh.close()

def eachFile(filePath):
    # pathDir = os.listdir(filePath)
    for dirPath, dirNames, fileNames in os.walk(filePath):
        for fileName in fileNames:
            if os.path.splitext(fileName)[1] == '.txt':
                # func(fileName)
                func(os.path.join(dirPath, fileName))

eachFile(os.getcwd())
