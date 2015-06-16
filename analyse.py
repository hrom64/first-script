#!/usr/bin/env python

import sys,re

class analyser:
    def __init__(self,desk):
        self.d=desk
        self.dic={}
        self.str_name=[sh[0] for sh in self.d]
    def parse(self,x):        
        for filename in x:  
            f=open(filename)
            for line in f:
                for sh in self.d:
                    name=sh[0]
                    string=sh[1]
                    m = re.search(string, line)
                    self.dic.setdefault(filename, {}).setdefault(name, [])
                    if m:
                        self.dic[filename][name].append(float(m.group(1)))
            f.close()
    def average(self,x):
        a=[z[x][y] for z in self.dic.values() for y in range(len(z[x]))]
        return sum(a)/len(a)    
 #   def column(self):
  #      a=[]
   #     for x in self.str_name:
    #        a.append("', '.join(map(str,(self.dic[filename][%s]))))" % (x)) #for x in self.str_name)] 
     #   return ', '.join(a) 
    def prn(self):
        print "%20s: %20s %20s" % ('Average',self.average(self.str_name[0]),self.average(self.str_name[1]))
    def sss(self):
        for filename in sorted(self.dic.keys()):
            print "%20s: %20s %20s" % (filename,', '.join(map(str,(self.dic[filename][self.str_name[0]]))),', '.join(map(str,(self.dic[filename][self.str_name[1]]))))
    def __str__(self):
        self.sss()
        self.prn()
        return "---------------------------------------------------------------"

data=analyser(   [ ("task-clock",'(\d+[.]?\d*)\s+task-clock'), ("seconds time elapsed",'(\d+[.]?\d*)\s+seconds time elapsed') ]   )        
data.parse (  sys.argv[1:])
print data


