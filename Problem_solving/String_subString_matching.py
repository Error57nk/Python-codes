# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 23:46:13 2019
@author : Nitesh kumar
Git     : https://github.com/Error57nk
Linkedin: www.linkedin.com/in/nitesh-kr
"""
#Matching 2 string
A="pythoguaguanisascriptinglanguage"
l1=len(A)
print("length of st1:",l1)
S="gua"
l2=len(S)
print("length of st2:",l2)

c=0
ct=0
for i in range(0,l1):
    if(A[i]==S[0]):
        print("%d matching" %i)
        a=i
        b=0
        ct=0
        while(True):
            if(A[a]==S[b]):
                print("%d %d matching %c %c" %(a,b,A[a],S[b]))
                a=a+1
                b=b+1
                ct=ct+1
                if(ct==l2):
                    c=c+1
                    break
            else:
                break
    elif(i==l1-1):
        break
print(c)
            
    