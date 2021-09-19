from gpiozero import Button, LED, OutputDevice
import time
import os

#RELAYS
IN1 = OutputDevice(12, active_high=True, initial_value=True)
IN2 = OutputDevice(16, active_high=True, initial_value=True)
IN3 = OutputDevice(20, active_high=True, initial_value=True)
IN4 = OutputDevice(21, active_high=True, initial_value=True)
#BUTTON
BTN = Button(26, hold_time=2)
#LED
LED = LED(19)
#WAIT FOR SHUTDOWN
def shutdown():
    LED.on()
    time.sleep(.2)
    check_call(['sudo', 'poweroff'])

while True:
    LED.on()
    sleep(1)
    LED.off()
    IN1.on()
    
               
