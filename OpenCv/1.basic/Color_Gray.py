import cv2

def main():
    path="C:/Users/nkkum/Desktop/project/standard_test_images/lena_gray_256.tif"
    #we have to use back / or \\ to get correct path as lenux system
    img= cv2.imread(path,0)
    #read the image from the above path
    cv2.imshow("image",img)
    #To show image in window
    cv2.waitKey(0)
    cv2.destroyWindow('image')

if __name__ =="__main__":
    main()
