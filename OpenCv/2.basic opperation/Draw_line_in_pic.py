import cv2

def main():
    path="C:/Users/nkkum/Desktop/project/standard_test_images/p.tif"
    #we have to use back / or \\ to get correct path as lenux system
    img= cv2.imread(path)
    #read the image from the above path
    cv2.imshow("image",img)
    #To show image in window
    cv2.line(img,(0,99),(99,0),(255,0,0),2)
    #code(image,(initial point),(final point),(color),thickness)
    cv2.rectangle(img,(140,160),(280,270),(0,255,0),3)
    cv2.circle(img,(160,160),67,(0,0,255),4)
    cv2.ellipse(img,(160,260),(50,20),0,0,360,(0,0,255),-1)
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyWindow('image')

if __name__ =="__main__":
    main()
