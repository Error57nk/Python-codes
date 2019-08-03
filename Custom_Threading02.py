# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 14:41:36 2019
@author: Nitesh kumar
Git    : Error57nk
"""
from threading import Thread
import time

class Custom(Thread):
    def run(self):
        for i in range(1,11):
            print("Custom Thread"+str(i),end='\n')
            time.sleep(0.3)   #This will take less time and complet first
            
        print("Custom Thread Ended")
        return

class Default:
    def main():
        obj=Custom()
        obj.start()
        
        print("Default Thread of Main")
        for i in range(1,11):
            print("*Default Thread"+str(i),end='\n')
            time.sleep(1)   #This will take time to complet 
        print("Default Thread of Main Ended")
             
        return

Default.main()
