#!/usr/bin/env python
dic={}

import sys

for filename in sys.argv[1:]:
    dic[filename]={"task-clock":[],"seconds time elapsed":[]}    
    f=open(filename)
    for line in f:
        if 'task-clock' in line:
            line = line.split()
            dic[filename]["task-clock"].append(float(line [0]))
        if 'seconds time elapsed' in line:
            line = line.split()
            dic[filename]["seconds time elapsed"].append(float(line [0]))
    f.close()                    
for filename in sorted(dic.keys()):
    print "%20s: %20s %20s" % (filename,', '.join(map(str,(dic[filename]["task-clock"]))),', '.join(map(str,(dic[filename]["seconds time elapsed"]))))

def averagedic(x):
    a=[z[x][y] for z in dic.values() for y in range(len(z[x]))]
    return sum(a)/len(a)

print "%20s: %20s %20s" % ('Average',averagedic('task-clock'),averagedic('task-clock'))
