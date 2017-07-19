#!/usr/bin/env python
###################################################################################
#bookreader.py
#Takes a picture of a page of printed text, performs Optical Character Recognition (ORC) 
#on the image, and then reads it aloud.
#
#Karan Nayan
#29 Jan,2014
#Dexter Industries
#www.dexterindustries.com/BrickPi
#Altered by Andrew Sue
#july 13,2017
#You may use this code as you wish, provided you give credit where it's due.
###################################################################################
import time
from subprocess import call
import re

import RPi.GPIO as GPIO
#from BrickPi import * 

#Setup all pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

GPIO.setup(40,GPIO.IN)
pwm = GPIO.PWM(12,50)
pwm2 = GPIO.PWM(11,50)
t = 0
#Start PWM
pwm.start(0)
pwm2.start(0)

#Function splits a big paragraph into smaller sentences for easy TTS
def splitParagraphIntoSentences(paragraph):
    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList

#Function that control servos
def flip():
    """#Roller turns to curl page
    pwm.ChangeDutyCycle(11.5)
    time.sleep(1)"""
    #Roller turns to curl page
    pwm.ChangeDutyCycle(11)
    time.sleep(0.45)
    pwm.ChangeDutyCycle(0)
    time.sleep(3)

    #flipper flips
    pwm2.ChangeDutyCycle(11)
    time.sleep(1.1)
    pwm2.ChangeDutyCycle(0)
    time.sleep(3)

    

    """#Rollers turning back
    pwm.ChangeDutyCycle(1)
    time.sleep(0.2)
    pwm.ChangeDutyCycle(0)
    time.sleep(3)"""

#Calls the Espeak TTS Engine to read aloud a sentence
#	-ven+m7:	Male voice
#	-s180:		set reading to 180 Words per minute
#	-k20:		Emphasis on Capital letters
def sound(spk):
    cmd_beg=" espeak -ven+m7 -s180 -k20 --stdout '"
    cmd_end="' | aplay"
    print cmd_beg+spk+cmd_end
    call ([cmd_beg+spk+cmd_end], shell=True)

#Setting up the BrickPi for the page rotating arm
"""roller =PORT_A
arm= PORT_B
BrickPiSetup()  				#setup the serial port for communication
BrickPi.MotorEnable[roller] = 1 #Enable the Motor A
BrickPi.MotorEnable[arm] = 1 #Enable the Motor B
BrickPiSetupSensors()   		#Send the properties of sensors to BrickPi

speed_roller=100
speed_arm=100
t1=.3
t2=.9"""

while True:
    #Take an image from the RaspberryPi camera with sharpness 100(increases the readability of the text for OCR)
    call ("raspistill -o j2.jpg -t 1 -sh 100", shell=True)
    print "Image taken"
	
    #Start the Tesseract OCR and save the text to out1.txt
    call ("tesseract j2.jpg out1", shell=True)
    print "OCR complete"
    
    #Open the text file and split the paragraph to Sentences
    fname="out1.txt"
    f=open(fname)
    content=f.read()
    print content
    sentences = splitParagraphIntoSentences(content)

    #Speak aloud each sentence in the paragraph one by one
    for s in sentences:
        print s.strip()
        call ("./speech.sh "+s.strip(), shell=True)
        sound(s.strip())
    print ("Working")	

    #Move the motor arm to turn the page
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(40,GPIO.IN)
    #if GPIO.input(40)== True:
    flip()
    t= t+1
    print("continue ", t)
