# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 23:23:26 2019
@author : Nitesh kumar
Git     : https://github.com/Error57nk
Linkedin: www.linkedin.com/in/nitesh-kr
"""

def main():
    a=[]
    n=int(input())
    for i in range(n):
        cmd=input().split()
        if cmd[0] =='insert':
            a.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0]=='print':
            print(a)
        elif cmd[0]=='sort':
            a.sort()
        elif cmd[0]=='append':
            a.append(int(cmd[1]))
        elif cmd[0]=='pop':
            a.pop()
        elif cmd[0]=='reverse':
            a.reverse()
        elif cmd[0]=='remove':
            a.remove(int(cmd[1]))
        
main()    
                
    
    
    

