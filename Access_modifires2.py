# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 20:51:23 2019
@author: Nitesh kumar
Git    : Error57nk
"""

#Access Modifiers 2: Object lavel private variable
class First:
    X=10       #public variables  class level
    __Y=20     #private variables class level
    def __init__(self):
        self.A=20    #public variable  object level
        self.__B=30  #private variable object level
    def printq(self):
        print("X val: ",First.X)
        print("Y val: ",First.__Y)
        print("A val: ",self.A)
        print("B val: ",self.__B)
        
class Second:
    def main():
        
        obj=First()
        obj.printq()
        print("X val: ",First.X)
        # print("Y val: ",First.__Y) #Error Not accessable
        print("Val of A",obj.A)
        #print("Val of B",obj.__B) #Error cant Access
        return

Second.main()