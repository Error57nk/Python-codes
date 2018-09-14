# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 19:44:53 2018

@author: nkkum
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

def main():
    imgpath="C:/Users/nkkum/Desktop/Workset/f.jpg"
    img=cv2.imread(imgpath,2)
    cv2.imshow('nitesh',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()
    