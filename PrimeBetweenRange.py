# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 21:04:41 2018

@author: Nitesh Kumar
   m@il: nkkumarnk7@gmail.com
"""

n=int(input("Enter the range from 1 to ? \n"))
i=2
j=2
key=0

for i in range(i, n+1):
    j=2
    for j in range(j, i):
        if(i%j==0):
            key=1
            #print("j",j)
            
    
        
    #print("\n***   ",i)
    #print(i)
    if(key==0):
        print(i)
    key=0
    
print("done") 
    