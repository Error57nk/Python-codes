# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 20:41:01 2019
@author: Nitesh kumar
Git    : Error57nk
"""

#Access Modifiers 1: Class lavel private variable
class First:
    X=10       #public variables
    __Y=20     #private variables
    
class Second:
    def main():
        print("X val: ",First.X)
        print("Y val: ",First.__Y) #Error Not accessable
        return

Second.main()
