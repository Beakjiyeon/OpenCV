import cv2                  # OpenCV 라이브러리 import

imageFile = '../data/lena.jpg'  # 영상 파일 이름

img = cv2.imread(imageFile) # cv2.IMREAD_COLOR
img2 = cv2.imread(imageFile, 0) # cv2.IMREAD_GRAYSCALE

cv2.imshow('Lena color',img)
cv2.imshow('Lena grayscale',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
