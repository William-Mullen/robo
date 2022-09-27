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
motor1 = Motor(port = Port.B, positive_direction = Direction.CLOCKWISE)
motor2 = Motor(port = Port.C, positive_direction = Direction.CLOCKWISE)
distance_sensor = UltrasonicSensor(Port.S4)
touch_sensor = TouchSensor(Port.S1)
program = 1
buttons = ev3.buttons.pressed()

# Write your program here.

while(program):  

    #move forward 1.2 meters, stop, beep wait for button press
    motor2.run(10000)
    motor1.run(10000)
    ev3.speaker.beep()

    wait(5000)
    
    motor1.stop()
    motor2.stop()
    motor2.run(0)
    motor1.run(0)
    wait(5000)

    #move forward until distantce to object is 50 cm, stop, beep wait for button press
    if Button.CENTER in buttons:
       motor1.run(100000000)
       motor2.run(100000000)
       if (distance_sensor.distance <= 500):
           motor1.run(0)
           moror2.run(0)
           ev3.speaker.beep()
       buttons.clear

    program=0
    
#     # move forward until bump sensor is pressed stop and go in reverse 50 cm
#    if Button.CENTER in buttons:
#        while (not touch_sensor.pressed):
#            motor1.run(500)
#            motor2.run(500)
#        ev3.speaker.beep()ls

#        while (distance_sensor <= 500):
#            motor1.run(-500)
#            motor2.run(-500)
#         motor1.run(0)
#         motor2.run(0)
    
    #if Button.CENTER in self.ev3.buttons.pressed() returns a list of pressed butto