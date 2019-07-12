from bluedot import BlueDot
from signal import pause
import explorerhat

speed = 50
direction = 0

def dpad(pos):
    global direction
    if pos.top:
        direction = 1
    elif pos.bottom:
        direction = 2
    elif pos.left:
        direction = 3
    elif pos.right:
        direction = 4
    continueMove()

def continueMove():
    global speed
    global direction
    if direction == 1:
        explorerhat.motor.forwards(speed)
    elif direction == 2:
        explorerhat.motor.backwards(speed)
    elif direction == 3:
        explorerhat.motor.one.forwards(speed)
        explorerhat.motor.two.backwards(speed)
    elif direction == 4:
        explorerhat.motor.one.backwards(speed)
        explorerhat.motor.two.forwards(speed)
    else
        explorerhat.motor.stop()

def stop():
    global direction
    direction = 0
    continueMove()

def rotated(rotation):
    global speed
    speed += rotation.value

bd = BlueDot()
bd.when_pressed = dpad
bd.when_moved = dpad
bd.when_released = stop
bd.when_rotated = rotated

pause()
