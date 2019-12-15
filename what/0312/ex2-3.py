import cv2 # OpenCV 라이브러리 import
from matplotlib import pyplot as plt # matplotlib.pyplot 라이브러리 import

imageFile = '../data/lena.jpg' # 영상 파일 이름

imgBGR = cv2.imread(imageFile) # cv2.IMREAD_COLOR
imgRGB = cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(imgRGB)
plt.show()
