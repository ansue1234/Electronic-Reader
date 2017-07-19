import RPi.GPIO as GPIO
import time
"""DutyCycle = 0.05*degrees + 2.4
   0 degree 2.4
   180 degree 11.5
   for 360 servo 180 = 0.42"""

#Setup all pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

GPIO.setup(40,GPIO.IN)
pwm = GPIO.PWM(12,50)
pwm2 = GPIO.PWM(11,50)
f = 0
#Start PWM
pwm.start(0)
pwm2.start(0)

def flip():
    """#Roller turns to curl page
    pwm.ChangeDutyCycle(11.5)
    time.sleep(1)"""
    #Roller turns to curl page
    pwm.ChangeDutyCycle(11)
    time.sleep(0.45)
    pwm.ChangeDutyCycle(0)
    time.sleep(3)
    print("Turned")

    #Roller turns to curl page
    pwm2.ChangeDutyCycle(11)
    time.sleep(1.1)
    pwm2.ChangeDutyCycle(0)
    time.sleep(3)

    """#Flipper turns to flip page and flips back
    pwm2.ChangeDutyCycle(4)
    time.sleep(0.2)
    pwm2.ChangeDutyCycle(8)
    time.sleep(0.2)
    pwm2.ChangeDutyCycle(12)
    time.sleep(0.2)
    pwm2.ChangeDutyCycle(13)
    time.sleep(3)
    pwm2.ChangeDutyCycle(2.4)
    time.sleep(5)"""

    """#Rollers turning back
    pwm.ChangeDutyCycle(1)
    time.sleep(0.2)
    pwm.ChangeDutyCycle(0)
    time.sleep(3)"""


                      
                    
while True:
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(40,GPIO.IN)
    #if GPIO.input(40)== True:
    flip()
    f= f+1
    print("continue ", f)


