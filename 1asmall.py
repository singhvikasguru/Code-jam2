# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 16:37:02 2018

@author: PRAVESH
"""
f=open('A-small-practice.in', 'r')
if f.mode!='r':
    exit

n=int(f.readline())
ml=list();
#for i in range(0, n):
a, b=(f.readline().split());
a=int(a)
b=int(b)
ln=list()
for i in range(a):
    ln.append(f.readline().split()[0])
    
f2=open('out.txt', 'w')    
f2.write(str(1211))  
f.close()
    
