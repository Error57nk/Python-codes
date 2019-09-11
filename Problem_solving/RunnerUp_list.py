# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 12:32:19 2019
@author : Nitesh kumar
Git     : https://github.com/Error57nk
Linkedin: www.linkedin.com/in/nitesh-kr
"""

n = int(input())
arr=map(int,input().split())
arr=list(arr)
arr.sort()
print(arr)
l=len(arr)
b=2
winner=arr[l-1]
runner=arr[l-b]

while(winner==runner):
    b=b+1
    runner=arr[l-b]

print(runner)
