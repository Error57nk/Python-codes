# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 21:03:31 2019
@author: Nitesh kumar
Git    : Error57nk
"""

#Encapsulation class level/Object level

class Emp:
    __x=20
    
    def __init__(self,a):  #object level
        self.__name=a
        return
    
    def getName(self):     #object level
        return self.__name
    
    def setName(self,name):        #object level
        self.__name=name
        return
    
    def setX(a):           #class level
        Emp.__x=a
        return
    
    def getX():           #class level
        return Emp.__x
    
    
class view:
    def main():
        obj=Emp('Nitesh')
        print("Name : ",obj.getName())
        obj.setName("Suresh")
        print("After Set Name : ",obj.getName())
        print("val X:",Emp.getX())
        Emp.setX(256)
        print("After Set val X:",Emp.getX())
        return

view.main()
        