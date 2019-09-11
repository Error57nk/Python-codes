# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 23:29:01 2019
@author : Nitesh kumar
Git     : https://github.com/Error57nk
Linkedin: www.linkedin.com/in/nitesh-kr
"""

if __name__ == '__main__':
    arr=[]
    b=int(input())
    for _ in range(b):
        name = input()
        score = float(input())
        arr.append([name,score])
    arr.sort(key=lambda X:X[1],reverse=True)
    b=2
    second=arr[len(arr)-b][1]
    last=arr[len(arr)-1][1]
    print(arr)
    print(second)

    while(second==last):
        b=b+1
        second=arr[len(arr)-b][1]
    arr.sort()
    for i in range(len(arr)):
        if arr[i][1]==second:
            print(arr[i][0])
    


