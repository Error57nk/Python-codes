# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:40:40 2019
@author : Nitesh kumar
Git     : https://github.com/Error57nk
Linkedin: www.linkedin.com/in/nitesh-kr
"""
#n1=int(input())
l1=set(map(int,input().split()))
#n2=int(input())
l2=set(map(int,input().split()))

print(l1 | l2)
print(l1 - l2)
print(l1^l2)
    