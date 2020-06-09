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
    print("Relay1 on")
    time.sleep(.5)
    GPIO.output(32,GPIO.HIGH)
    print("Relay1 off")
    time.sleep(.5)
    GPIO.output(36,GPIO.LOW)
    print("Relay2 on")
    time.sleep(.5)
    GPIO.output(36,GPIO.HIGH)
    print("Relay2 off")
    time.sleep(.5)
    GPIO.output(38,GPIO.LOW)
    print("Relay3 on")
    time.sleep(.5)
    GPIO.output(38,GPIO.HIGH)
    print("Relay3 off")
    time.sleep(.5)
    GPIO.output(40,GPIO.LOW)
    print("Relay4 on")
    time.sleep(.5)
    GPIO.output(40,GPIO.HIGH)
    print("Relay4 off")
    GPIO.cleanup()
    print("cleanup done")
