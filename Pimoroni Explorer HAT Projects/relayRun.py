import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(32,GPIO.OUT)
GPIO.output(32,GPIO.HIGH)

GPIO.setup(36,GPIO.OUT)
GPIO.output(36,GPIO.HIGH)

GPIO.setup(38,GPIO.OUT)
GPIO.output(38,GPIO.HIGH)

GPIO.setup(40,GPIO.OUT)
GPIO.output(40,GPIO.HIGH)

while True:
    GPIO.output(32,GPIO.LOW)
    #print("IN32 Active")
    time.sleep(.5)
    GPIO.output(32,GPIO.HIGH)
    GPIO.output(36,GPIO.LOW)
    #print("IN2 Active")
    time.sleep(.5)
    GPIO.output(36,GPIO.HIGH)
    GPIO.output(38,GPIO.LOW)
    #print("IN3 Active")
    time.sleep(.5)
    GPIO.output(38,GPIO.HIGH)
    GPIO.output(40,GPIO.LOW)
    #print("IN4 Active")
    time.sleep(.2)
    GPIO.output(40,GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(40,GPIO.LOW)
    #print("IN4 Active")
    time.sleep(.2)
    GPIO.output(40,GPIO.HIGH)
    time.sleep(.2)
    GPIO.cleanup()




