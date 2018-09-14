# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 20:13:46 2018

@author:Nitesh Kumar
 nkkumarnk7@gmail.com
"""

print ("Enter the String to remove vowel")
a=input("Yes \n")
v=('a','e','i','o','u')

for i in a:
    if i=="a" or i=="u" or i=="e" or i=="i" or i=="o" :
    
    # or use this
    
    # if i in v:
    
    
        a=a.replace(i,"#")
        
        
print(a)
		
    
    
    

