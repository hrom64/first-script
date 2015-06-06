#!/usr/bin/env python
dic={}
s=[]
s1=[]

import sys

for filename in sys.argv[1:]:
    dic[filename]={"task-clock":[],"seconds time elapsed":[]}    
    for line in open(filename):
        if 'task-clock' in line:
            line = line.split()
            s.append(float(line [0]))
            dic[filename]["task-clock"].append(float(line [0]))
        if 'seconds time elapsed' in line:
            line = line.split()
            s1.append(float(line [0]))
            dic[filename]["seconds time elapsed"].append(float(line [0]))
for filename in sorted(dic.keys()):
    print "%20s: %20s %20s" % (filename,', '.join(map(str,(dic[filename]["task-clock"]))),', '.join(map(str,(dic[filename]["seconds time elapsed"]))))
print "%20s: %20s %20s" % ('Average', sum(s)/len(s),sum(s1)/len(s1))
        

