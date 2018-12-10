import cv2
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Id=raw_input('\n enter your id \n')
T_S = int(input(' \n How many sample you want to take \n'))
sampleNum=0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        #incrementing sample number 
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        sv = gray[y:y+h,x:x+w]
        cv2.imwrite("Pic/User."+Id +'.'+ str(sampleNum) + ".jpg", sv)
        cv2.putText(img,str(sampleNum),(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,100,0))
        cv2.imshow('frame',img)
    #wait for 100 miliseconds 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    elif sampleNum > T_S:
        break
cam.release()
print('Data Collected Succesfully')
cv2.destroyAllWindows()
