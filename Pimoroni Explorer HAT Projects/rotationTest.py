from bluedot import BlueDot
from signal import pause

speed = 0

def rotated(rotation):
    global speed
    speed += rotation.value
    
    print("{} {} {}".format(speed,
                            rotation.clockwise,
                            rotation.anti_clockwise))
bd = BlueDot
bd.when_rotated = rotated
    
pause()
