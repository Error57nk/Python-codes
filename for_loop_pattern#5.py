# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 23:29:49 2019

@author: nkkum
"""
n=int(input('enter range'))
'''
print(" pattern 2")
for i in range (1,n+1):
    for j in range(i,n):
        print("*",end=' ')
        
    print(' ')'''
    
for i in range(1,int(n/2)+1):
    for j in range(1,n+1):
        if(j<=i):
            print('*',end=' ')
        elif(j>n-i):
            print('*',end=' ')
        else:
            print(" ",end=' ')
    print(' ')