import RPi.GPIO as GPIO
import time
"""DutyCycle = 0.05*degrees + 2.4
   0 degree 2.4
   180 degree 11.5"""

#Setup all pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

GPIO.setup(40,GPIO.IN)
pwm = GPIO.PWM(12,50)
pwm2 = GPIO.PWM(11,50)

#Start PWM
pwm.start(0)
pwm2.start(0)

def flip():
    #Roller turns to curl page
    pwm.ChangeDutyCycle(11.5)
    time.sleep(1)

    #Flipper turns to flip page and flips back
    pwm2.ChangeDutyCycle(11.5)
    time.sleep(1)
    pwm2.ChangeDutyCycle(2.4)
    time.sleep(1)

    #Roller turns back and end
    pwm.ChangeDutyCycle(2.4)
    time.sleep(5)
   # GPIO.cleanup()

while True:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(40,GPIO.IN)
    if GPIO.input(40)== True:
        
        flip()
        print("continue")


