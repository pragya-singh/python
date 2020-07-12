#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 19:24:12 2019

@author: singg
"""

import os
import sys
# Some other standard libraries
# math, re(Regex), urllib.request, smtplib, datetime, 
# Data Compression Libraries : zlib, gzip, bz2, lzma, zipfile and tarfile
# For Unit Testing : doctest & unittest

def getSize(path):
    #print(path)
    size = 0.0
    if os.path.isfile(path):
        size = os.path.getsize(path)
    else:
        files = os.listdir(path)
        for f in files:    
            size = size + getSize(path+'/'+f)
            
    return size
            
        
if __name__ == '__main__':
    input_path = sys.argv[1]
    print(input_path)
    print(getSize(input_path))
