# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 21:18:18 2019
@author: Nitesh kumar
Git    : Error57nk
"""

#Singel level Inheritance // -Class level

class parent:
    def m1():             #class level method
        print("You are in M1 of Parent")
        return
    
class child(parent):
    def m2():             #class level method
        print("You are in M2 of Child")
        return
    
class single:
    def main():
        child.m2()
        child.m1()
        
        parent.m1()
        #parent.m2() #Error


single.main()