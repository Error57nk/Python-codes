import cv2

def main():
    path="C:/Users/nkkum/Desktop/project/standard_test_images/lena_gray_256.tif"
    #we have to use back / or \\ to get correct path as lenux system
    img= cv2.imread(path)
    print(img)
    print(img.dtype)
    cv2.waitKey(0)
    cv2.destroyWindow('image')

if __name__ =="__main__":
    main()
