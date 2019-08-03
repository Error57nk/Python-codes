# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 14:07:29 2019
@author: Nitesh kumar
Git    : Error57nk
"""
class OP:
    def NSum(*obj):
        # l=len(obj)
        result=0
        for i in obj:
            result=int(i)+result
        return result
    
    def NSub(*obj):
        # l=len(obj)
        result=0
        for i in obj:
            result=int(i)-result
        return result
    
    def NMul(*obj):
        # l=len(obj)
        result=1
        for i in obj:
            result=result*int(i)
        return result
    def NDiv(*obj):
        # l=len(obj)
        result=1
        for i in obj:
            result=int(i)/result
        return result
        
        
