import cv2, pafy # pafy 라이브러리 import

url = 'https://www.youtube.com/watch?v=u_Q7Dkl7AIk'
video = pafy.new(url)
print('title = ', video.title)
print('video.rating = ', video.rating)
print('video.duration = ', video.duration)
best = video.getbest(preftype='webm') # 'mp4','3gp'
print('best.resolution', best.resolution)

cap=cv2.VideoCapture(best.url)
while(True):
    retval, frame = cap.read()
    if not retval:
        break
    cv2.imshow('frame',frame)
    key = cv2.waitKey(25)
    if key == 27: # Esc
        break
    
cv2.destroyAllWindows()
