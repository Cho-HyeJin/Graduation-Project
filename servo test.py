import RPi.GPIO as GPIO
import time
from random import randint

pin =18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p= GPIO.PWM(pin, 50)
p.start(0)

isOwner = 3


for i in range(3):
    #initial point
    p.ChangeDutyCycle(12.5)
    time.sleep(3)
        
    isOwner = randint(0,1)
    print(i, '-> ', isOwner, '\n')
    
    if(isOwner == 0):
        print("no")
        p.ChangeDutyCycle(12.5)
        time.sleep(2)
        p.ChangeDutyCycle(7.5)
        time.sleep(2)
        p.ChangeDutyCycle(2.5)
        time.sleep(3)
    else:
    print("owner!")
    time.sleep(3)


