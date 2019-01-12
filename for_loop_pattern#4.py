# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 23:06:58 2019

@author: nkkum
"""

#for pattern

n=int(input('enter range'))
print(" pattern 1")
for i in range (1,n+1):
    for j in range(1,i):
        print("*",end=' ')
        
    print(' ')
    

#pattern 2
    
print(" pattern 2")
for i in range (1,n+1):
    for j in range(i,n):
        print("*",end=' ')
        
    print(' ')