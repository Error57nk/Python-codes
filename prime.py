# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:40:00 2019
@author: Nitesh kumar
Git    : Error57nk
"""

print("Enter the Number For Prime Verification - " )
k=0
num =int(input())

for i in range(1,num):
    
    if(num % i == 0):
        k=k+1
        

if(k<2):
    print("The Number " + str(num) + " is Prime")
    
else:
    print("This is not a prime number as it is divisible by " + str(k + 1) +" number")
    