# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:04:07 2019
@author : Nitesh kumar
Git     : https://github.com/Error57nk
Linkedin: www.linkedin.com/in/nitesh-kr
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
        l=len(arr)
        sumr=0
        suml=0
        for i in range(l):
            sumr=sumr+arr[i][i]
        for i in range(l):
            suml=suml+arr[l-i-1][i]
        res=suml-sumr
        return abs(res)
        

if __name__ == '__main__':
    

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

   

