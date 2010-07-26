#!/usr/bin/python

#configure me
unite_folder = '/home/gdr/tmp/unite'
unite_drop_folder = '/home/gdr/tmp/unite/drop'
unite_url = 'http://desktop.gdr.operaunite.com/file_sharing/content/'

# imports
import os
import os.path
import shutil
import sys
import time

# original file name
file = sys.argv[1]

# remove protocol part
proto = 'file://'
if file[:len(proto)] == proto:
    file = file[len(proto):]

# check if the file is in drop folder
if len(os.path.commonprefix([file, unite_folder])) < len(unite_folder):
    # copy the file to unite drop folder
    if not os.path.exists(unite_drop_folder):
        os.mkdir(unite_drop_folder)

    new_file = os.path.join(unite_drop_folder, os.path.basename(file))
    if os.path.exists(new_file):
        (base, ext) = os.path.splitext(new_file)
        new_file = base + '.' + str(time.time()) + ext
    shutil.copy2(file, new_file)
    file = new_file

relfile = os.path.relpath(file, unite_folder)
print unite_url + relfile
