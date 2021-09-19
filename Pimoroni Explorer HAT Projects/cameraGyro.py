from bluedot import BlueDot
from signal import pause
import explorerhat

speed = 40 
i = speed

def dpad(pos):
    if pos.top:
        explorerhat.motor.one.forwards(speed)
    elif pos.bottom:
        explorerhat.motor.one.backwards(speed)
    elif pos.left:
        explorerhat.motor.two.backwards(speed)
    elif pos.right:
        explorerhat.motor.two.forwards(speed)
        
def stop():
    explorerhat.motor.stop()
    #print("motor stopped")
    
    
bd = BlueDot()
bd.when_pressed = dpad
bd.when_moved = dpad
bd.when_released = stop

pause()

