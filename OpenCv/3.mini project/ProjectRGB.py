import cv2
import numpy as np

def emptyfun():
    print('green')
    pass

def main():
    #creating a image
    img=np.zeros((512,512,3),np.uint8)
    wnidowName = 'Project BGR'
    cv2.namedWindow(wnidowName)

    cv2.createTrackbar('B',wnidowName,0,255,emptyfun())
    cv2.createTrackbar('G',wnidowName,0,255,emptyfun())
    cv2.createTrackbar('R',wnidowName,0,255,emptyfun())

    while(True):
        cv2.imshow(wnidowName, img)
        
        if cv2.waitKey(1) ==27:
            break

        blue =cv2.getTrackbarPos('B',wnidowName)
        green =cv2.getTrackbarPos('G',wnidowName)
        red =cv2.getTrackbarPos('R',wnidowName)
        img[:]=[blue,green,red]
    cv2.destroyAllWindows()



if __name__=="__main__":
    main()
