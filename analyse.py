#!/usr/bin/env python
a = {}
b = {}
filenames = []
array=[]
array1=[]

import sys

for arg in sys.argv:
    filenames.append (arg)
del filenames[0]
for filename in filenames:
    for line in open(filename):
        if 'task-clock' in line:
            line = line.split()
            array.append ([filename,(float(line [0]))])
        if 'seconds time elapsed' in line:
            line = line.split()
            array1.append ([filename,(float(line [0]))])
a=array
b=array1

print a 



        

