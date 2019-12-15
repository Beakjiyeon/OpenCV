import cv2
import numpy as np

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: #  마우스 왼쪽 버튼을 클릭하면
            cv2.circle(param[0], (x, y), 5, (255, 0, 0), 3) # 작은 원을 그림
            myX=param[1] # 클릭된 좌표의 x 좌표를 저장할 배열
            myY=param[2] # 클릭된 좌표의 y 좌표를 저장할 배열
            myX.append(x) # x 좌표를 저장함.
            myY.append(y) # y 좌표를 저장함.
            
            if len(param[1])==4: # x좌표를 저장하는 배열에 4개의 점이 저장되었다면
                rows, cols, channels = param[0].shape # 이미지의 높이, 너비, 채널을 반환
                
                # 좌측상단, 좌측하단, 우측하단, 우측상단의 순으로 좌표를 지정함
                src_points=np.float32([[myX[0],myY[0]],[myX[1],myY[1]],[myX[2],myY[2]],[myX[3],myY[3]]]) 
                dst_points=np.float32([[0,0],[0,rows],[cols,rows],[cols,0]])
                
                cv2.getPerspectiveTransform(src_points,dst_points) # 변환행렬 구함
                affineM=cv2.getPerspectiveTransform(src_points,dst_points) 
                img_sym=cv2.warpPerspective(param[0],affineM,(cols,rows)) # 비뚤어진 영상이 보정됨 

                # 보정된 결과에 로고 삽입
                src2 = cv2.imread('./data/duksung_symbol2.png') # 덕성 로고 이미지 읽음
                # 로고이미지의 크기를 100*100 로 변경 
                shrink = cv2.resize(src2, dsize=(100, 100), interpolation=cv2.INTER_AREA)
                rows,cols,channels = shrink.shape 
                roi = img_sym[0:rows, 0:cols]            
                gray = cv2.cvtColor(shrink,cv2.COLOR_BGR2GRAY)
                ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
                mask_inv = cv2.bitwise_not(mask)
                
                src1_bg = cv2.bitwise_and(roi, roi, mask = mask)
                src2_fg = cv2.bitwise_and(shrink, shrink, mask = mask_inv)
                dst = cv2.bitwise_or(src1_bg, src2_fg)
                img_sym[0:rows, 0:cols] = dst
                # 로고가 삽입된 보정된 영상을 화면에 띄움
                cv2.imshow('dst3',img_sym)
    cv2.imshow("img", param[0])

img = cv2.imread('./data/gal.png') # 원본 이미지 읽음
cv2.imshow('img', img) # 화면에 이미지 띄움
myXlist = [] # 마우스이벤트에 의해 얻는 x 좌표를 저장할 배열
myYlist = [] # 마우스이벤트에 의해 얻는 y 좌표를 저장할 배열
cv2.setMouseCallback('img', onMouse, [img,myXlist,myYlist])
cv2.waitKey()
cv2.destroyAllWindows()
