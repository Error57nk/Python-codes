# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

def main():
    imgpath="C:/Users/NITESH/Desktop/wheelfile/s0.jpg"
    img=cv2.imread(imgpath, 0)
    cv2.imshow('nitesh',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()
    