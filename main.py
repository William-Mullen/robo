#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
motor1 = Motor(port = Port.B, positive_direction = Direction.COUNTERCLOCKWISE)
motor2 = Motor(port = Port.C, positive_direction = Direction.COUNTERCLOCKWISE)
program = 1

# Write your program here.

while(program):  
    motor1.run(1200)
    motor2.run(1200)
    wait(5000) 
    ev3.speaker.beep()
    program = 0
    #test