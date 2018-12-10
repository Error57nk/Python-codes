import ok
import cv2
import numpy as np
recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('trainedData/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

trig = True
msId=0
cam = cv2.VideoCapture(0)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        print(conf)
        if(conf<50):
            
            cv2.imwrite("a.jpg" , im)
            
            if(Id==1):
                Id="NITESH"
                msId=1
                cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font,(255,0,0))
                if(cv2.waitKey(1) & trig == True):
                    print('Sending Pic')
                    ok.sendit(msId)
                    trig = False
            elif(Id==2):
                Id="Avisek anand"
                msId=2
                cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font,(255,0,0))
                if(cv2.waitKey(1) & trig == True):
                    print('Sending Pic')
                    ok.sendit(msId)
                    trig = False
            elif(Id==3):
                Id="Joydip"
                msId=3
                cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font,(255,0,0))
                if(cv2.waitKey(1) & trig == True):
                    print('Sending Pic')
                    ok.sendit(msId)
                    trig = False
            else:
                Id="Mactching data waiting For Conformation"
                cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font,(255,0,0))
                
        else:
            Id="Unknown No data found"
            msId=4
            cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font,(255,0,0))
            if(cv2.waitKey(1) & trig == True):
                    print('Sending Pic')
                    ok.sendit(msId)
                    trig = False
        
    cv2.imshow('im',im)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        trig = True
        print("MAIL reset ...redy to send new pic")
        
    elif (cv2.waitKey(2)& 0xFF == ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
