# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 22:13:40 2018

@author: Nitesh Kumar
   m@il: nkkumarnk7@gmail.com
"""

name=input("Enter the Name\n")
b=int(len(name))
b=b-1
print(name[2])
n=name
print(n)
for i in name:
    n=n.replace(b,name[2])
    b=b-1
    print(n)