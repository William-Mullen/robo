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

# Write your program here.

while(program):  

  #move forward 1.2 meters, stop, beep wait for button press
    motor1.run_target(400, 5000, wait=False)
    motor2.run_target(400, 5000, wait=False)
    wait(8000)
    ev3.speaker.beep()
    motor1.reset_angle(0)
    motor2.reset_angle(0)


    while True:
        buttons = ev3.buttons.pressed()
        if Button.CENTER in buttons:
            while (distance_sensor.distance() >= 500):
                motor2.run(200)
                motor1.run(200)
            motor1.run(0)
            motor2.run(0)
            ev3.speaker.beep()
            break
     
    motor1.reset_angle(0)
    motor2.reset_angle(0)
    while True:
        buttons = ev3.buttons.pressed()
        if Button.CENTER in buttons:
            motor2.run(100)
            motor1.run(100)
            motor1.reset_angle(0)
            motor2.reset_angle(0)
        if (touch_sensor.pressed()):
            motor2.run_target(100, -1022, wait=False)
            motor1.run_target(100, -1022, wait=False)
            motor1.run(0)
            motor2.run(0)
            break
  
            
    #move forward until distantce to object is 50 cm, stop, beep wait for button press

    program=0