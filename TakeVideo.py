#Take video
#import library
import picamera
import time
import datetime


'''#Taking pictures
with picamera.PiCamera() as camera: #Create a PyCamera Object
    camera.resolution = (1024,768)  #Camera quality settings
    now = datetime.datetime.now()
    fileName = now.strftime('%Y-%m-%d %H:&M:&s')
    camera.start_preview()  #Startpreview
    time.sleep(2)
    camera.stop_preview()  #Stop preview
    camera.capture(fileName + '.jpg') #Save a picture as a 'fileName.jpg' after taking it
'''


#Taking videos
with picamera.PiCamera() as camera: #Create a PyCamera Object
    camera.resolution = (640,480)  #Camera quality settings
    now = datetime.datetime.now()
    fileName = now.strftime('%Y-%m-%d %H:&M:&s')
    camera.start_recording(output = fileName + '.h264')  #Start recoding
    camera.wait_recording(5) #during 5 sec
    camera.stop_recording() #Stop recoding
