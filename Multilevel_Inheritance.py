# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 21:28:15 2019
@author: Nitesh kumar
Git    : Error57nk
"""
class grand:
    def m3():
        print("You are in grand M3")  #class level method
        return
    
class parent(grand):
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
        child.m3()
        
        parent.m1()
        #parent.m2() #Error
        parent.m3()
        
        grand.m3()
        #grand.m2() #error
        #grand.m1() #error


single.main()