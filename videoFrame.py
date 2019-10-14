'''import cv2 #동영상 재생 코드

capture = cv2.VideoCapture("test2.mp4")

while True:
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("test2.mp4")

    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    if cv2.waitKey(500) > 0: break  #500ms(0.5초)마다 프레임 재생 (1초 == 1000ms)

capture.release()
cv2.destroyAllWindows()'''

import cv2
 
# 영상의 의미지를 연속적으로 캡쳐할 수 있게 하는 class
vidcap = cv2.VideoCapture("test2.mp4") #('파일 이름')
 
count = 0
 
while(vidcap.isOpened()):
    # read()는 grab()와 retrieve() 두 함수를 한 함수로 불러옴
    # 두 함수를 동시에 불러오는 이유는 프레임이 존재하지 않을 때
    # grab() 함수를 이용하여 return false 혹은 NULL 값을 넘겨 주기 때문
    ret, image = vidcap.read()
 
    # 캡쳐된 이미지를 저장하는 함수, 파일 이름 frame1,2,3 ---
    cv2.imwrite("frame%d.jpg" % count, image)
 
    print('Saved frame%d.jpg' % count)
    count += 1

#이미지  출력 장수 설정
    if count == 10:  #10장만 출력
        break
 
vidcap.release()

'''while(vidcap.isOpened()):
    ret, image = vidcap.read()
 
    if(int(vidcap.get(1)) % 20 == 0):
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv2.imwrite("frame%d.jpg" % count, image)
        print('Saved frame%d.jpg' % count)
        count += 1'''
