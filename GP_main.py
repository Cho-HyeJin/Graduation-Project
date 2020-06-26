# Library
import picamera
import time
import datetime

import cv2

import RPi.GPIO as GPIO
import time


pin =18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p= GPIO.PWM(pin, 50)
p.start(0)

isOwner = 1


while(1)
    #Taking videos
    with picamera.PiCamera() as camera: #Create a PyCamera Object
        camera.resolution = (640,480)  #Camera quality settings
        now = datetime.datetime.now()
        fileName = now.strftime('%Y-%m-%d %H:&M:&s') #Set file name
        camera.start_recording(output = fileName + '.h264')  #Start recoding
        camera.wait_recording(5) #during 5 sec
        camera.stop_recording() #Stop recoding


    #Continuous capture class
    vidcap = cv2.VideoCapture("fileName.mp4") #('file name')
    vidcap.set(cv2.CAP_PROP_POS_MSEC, 10000) #1sec = 1000ms
 
    count = 0
 
    while(vidcap.isOpened()):
        ret, image = vidcap.read()
 
        #Save Captured Image
        cv2.imwrite("Frame%d.jpg" % count, image)
 
        print('Saved frame%d.jpg' % count)
        count += 1
 
    vidcap.release()

    

    #여기 딥러닝 코드 
    #
    #
    #결과 TRUE FALSE

    p.ChangeDutyCycle(12.5)
    time.sleep(3)
        
    isOwner = 1 #true

    # If not owner, block 
    if(isOwner == 0):
        print("No")
        p.ChangeDutyCycle(12.5)
        time.sleep(2)
        p.ChangeDutyCycle(7.5)
        time.sleep(2)
        p.ChangeDutyCycle(2.5)
        time.sleep(3)
    else:
    print("Owner!")
    time.sleep(3)

    
