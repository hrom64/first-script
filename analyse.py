#!/usr/bin/env python
filenames = []
array={}
array1={}
s=[]
s1=[]

import sys

for arg in sys.argv:
    filenames.append (arg)
del filenames[0]
for filename in filenames:
    for line in open(filename):
        if 'task-clock' in line:
            line = line.split()
            a=array.setdefault(filename,[])
            a.append(float(line [0]))
            array[filename]=(a)
        if 'seconds time elapsed' in line:
            line = line.split()
            a=array1.setdefault(filename,[])
            a.append(float(line [0]))
            array1[filename]=(a)
for key in array.keys():
    s+=array[key]
for key in array1.keys():
    s1+=array1[key]
filenames.append("Avarage")
array["Avarage"]= [sum(s)/len(s)]
array1["Avarage"]= [sum(s1)/len(s1)]
for filename in filenames:      
    print "%20s: %20s %20s" % (filename,', '.join(map(str,(array.setdefault(filename,[])))),', '.join(map(str,(array1.setdefault(filename,[])))))



        

