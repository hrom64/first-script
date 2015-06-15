#!/usr/bin/env python

import sys,re

class analyser:
    def __init__(self,name,string):
        self.name=name
        self.string=string
        self.dic={}
    def search(self,filename,line):
        m = re.search(self.string, line)
        if m:
            self.dic.setdefault(filename, []).append(float(m.group(1)))        
    def average(self):
        a=[z[y] for z in self.dic.values() for y in range(len(z))]
        return sum(a)/len(a)    
    def prn(self,filename):
        return ', '.join(map(str,(self.dic.setdefault(filename,[]))))

task=analyser("task-clock",'(\d+[.]?\d*)\s+task-clock')
seconds=analyser("seconds time elapsed",'(\d+[.]?\d*)\s+seconds time elapsed')


for filename in sys.argv[1:]:  
    f=open(filename)
    for line in f:
        task.search(filename,line)
        seconds.search(filename,line)

    f.close()                    
for filename in sorted(task.dic.keys()):
    print "%20s: %20s %20s" % (filename,task.prn(filename),seconds.prn(filename))

print "%20s: %20s %20s" % ('Average',task.average(),seconds.average())

