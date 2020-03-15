#!/usr/bin/env python
# coding: utf-8
import sys, getopt
import glob
import os
from os.path import *
import shutil
#import win32api

root_addr = os.getcwd()
# root_addr = 'C:/Users/tom_h/Projects/cpyMake'
dir_list = os.listdir(root_addr)
dir_list

drives = []
for i in range(ord('a'), ord('z')+1):
    drive = chr(i)

    if(exists(drive +":\\")):
        drives.append(drive)



drives = list(map(lambda x: x +':/',drives))
print (drives)
drives.remove('c:/')

connected_dict = {}

for drive in drives:
    drive_dir = os.listdir(drive)
    print(drive_dir)
    for cpy_dir in dir_list:
        if cpy_dir+'.txt' in drive_dir:
    
            connected_dict[cpy_dir] = drive
            cpy_files =  os.listdir(root_addr+'/'+cpy_dir)
            connected_dict[cpy_dir] = {'drive': drive, 'files': cpy_files}
print(connected_dict)  
        
for cpy_dir in connected_dict.keys():
    print(cpy_dir)
    if cpy_dir+'.py' in connected_dict[cpy_dir]['files']:
        src_file = root_addr+'/'+cpy_dir+'/'+cpy_dir + '.py'
        dst_file = connected_dict[cpy_dir]['drive']+'code.py'
        print(src_file,dst_file)
        shutil.copy(src_file,dst_file)

