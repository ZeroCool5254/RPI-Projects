import RPi.GPIO as GPIO
import time

print("starting GPIO cleanup")
time.sleep(1)
GPIO.cleanup()
print("GPIO cleanup completed.")
