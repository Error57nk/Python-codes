import cv2
import numpy as np

cap =cv2.VideoCapture(0)
path = "C:\\Users\\nkkum\\Desktop\\project\\5.working withopencv"
i = 0
while(True):
    b = raw_input("Enter followingc \n 1. c to caputure & save\n 2. v to show image \n 3. q to exit \n")
    if(b == 'c'):
       print('taking short and saving')
       ret, img=cap.read()
       cv2.imwrite("smpl" + str(i) +".jpg" , img)
       i=i+1

    elif(b == 'v'):
        ret, img=cap.read()
        print('showing on new window \n')
        pt =path +'\\' + "smpl" + str(i) +".jpg"
        print(pt)
        p = cv2.imread(pt)
        cv2.imshow('image',p)
        cv2.waitKey(0)
        cv2.destroyWindow('image')

    elif(b== 'q'):
       break


       
cap.release()
cv2.destroyAllWindows()
