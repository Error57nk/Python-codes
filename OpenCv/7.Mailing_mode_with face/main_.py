import cv2
import numpy as np
import ok

cap =cv2.VideoCapture(0)
text ='Sending..'
key = False
while(True):
    ret, img = cap.read()
    if(key == True):
        cv2.putText(img,text,(200,200),cv2.FONT_HERSHEY_TRIPLEX,2,(0,255,0))
    cv2.imshow('Mailing_screen',img)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        print('taking short and saving')
        ret,img=cap.read()
        cv2.imwrite("a.jpg" , img)
        cv2.imshow('Mailing_screen',img)
        #ok.sendit()
        key=True
        """ while(p<100):
            ret, new = cap.read()
            cv2.putText(new,text,(200,200),cv2.FONT_HERSHEY_TRIPLEX,2,(0,0,255))
            cv2.imshow('Mailing_screen',new)
            p=p+1
            print(p)"""
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
    p=0
       
cap.release()
cv2.destroyAllWindows()
