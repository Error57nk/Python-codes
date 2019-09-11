# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:15:23 2019
@author : Nitesh kumar
Git     : https://github.com/Error57nk
Linkedin: www.linkedin.com/in/nitesh-kr
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total=sum(student_marks.get(query_name))
    print("%.2f" %((total/300)*100))
    

