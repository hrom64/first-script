#!/usr/bin/env python
filenames = []
array={}
array1={}

import sys

for arg in sys.argv:
    filenames.append (arg)
del filenames[0]
for filename in filenames:
    for line in open(filename):
        if 'task-clock' in line:
            line = line.split()
            array[filename]=(float(line [0]))
        if 'seconds time elapsed' in line:
            line = line.split()
            array1[filename]=(float(line [0]))
filenames.append("Avarage")
array["Avarage"]= sum(array.values())/len(array.values())
array1["Avarage"]= sum(array1.values())/len(array1.values())
for filename in filenames:      
    print "%20s: %20s %20s" % (filename,array.setdefault(filename,[]),array1.setdefault(filename,[]))



        

