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
f = 0
#Start PWM
pwm.start(0)
pwm2.start(0)

#Roller turns to curl page
pwm.ChangeDutyCycle(0.5)
time.sleep(0.42)
pwm.ChangeDutyCycle(0)

"""#Flipper turns to flip page and flips back
pwm2.ChangeDutyCycle(14)
time.sleep(3)
pwm2.ChangeDutyCycle(2.4)
time.sleep(3)

#Roller turns back and end
pwm.ChangeDutyCycle(2.4)
time.sleep(5)"""
