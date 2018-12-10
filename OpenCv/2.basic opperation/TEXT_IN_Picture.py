import cv2

def main():
    path="C:/Users/nkkum/Desktop/project/standard_test_images/p.tif"
    #we have to use back / or \\ to get correct path as lenux system
    img= cv2.imread(path)
    t='Nitesh'
    cv2.putText(img,t,(100,100),cv2.FONT_HERSHEY_SIMPLEX,.3,(255,100,0))
    #code(image,text,(location),fontstyle,size,(color))
    
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyWindow('image')

if __name__ =="__main__":
    main()
