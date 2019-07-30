# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class info:
    def add(*arr):
        res=sum(arr)
        print("The result is ",res)
        return
    def main():
        try:
            x=int(input("Enter 1st Number: "))
            y=int(input("Enter 2nd Number: "))
            t[]=int(input("Enter 3nd Number: "))
            info.add(x,y)
        except ValueError:
            print("Invalid Input")
            info.main()
            
        return

info.main()