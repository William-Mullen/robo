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
    while not (touch_sensor.pressed()):
        motor1.run(100)
        motor2.run(100)
    motor1.run(0)
    motor2.run(0)
    motor1.run_target(-150, 200, wait=False)
    motor2.run_target(-150, 200, wait=True)   
    motor1.reset_angle(0)
    motor2.reset_angle(0) 
    #run left wheel 
        
    while (motor1.angle()< 3000)
        motor1.run(100)
        motor2.run(100)
        if(distance_sensor.distance > 20)
            motor1.run(0)
            motor2.reset_angle(0) 
            motor2.run_target(30, 100, wait=True)
        if(distance_sensor.distance < 15)
            motor1.run(0)
            motor2.reset_angle(0) 
            motor2.run_target(30, -100, wait=True)

    ev3.speaker.beep()
    program=0     


#Lab one

# while(program):  

#   #move forward 1.2 meters, stop, beep wait for button press
#     motor1.run_target(200, 2450, wait=False)
#     motor2.run_target(200, 2450, wait=True)
#     ev3.speaker.beep()
#     motor1.reset_angle(0)
#     motor2.reset_angle(0)


#     while True:
#         buttons = ev3.buttons.pressed()
#         if Button.CENTER in buttons:
#             while (distance_sensor.distance() >= 550):
#                 motor2.run(200)
#                 motor1.run(200)
#             motor1.run(0)
#             motor2.run(0)
#             ev3.speaker.beep()
#             break
            

#     while True:
#         buttons = ev3.buttons.pressed()
#         if Button.CENTER in buttons:
#             motor1.run(100)
#             motor2.run(100)
#             buttons.clear()
#         if (touch_sensor.pressed()):
#             while (distance_sensor.distance() <= 550):
#                 motor2.run(-100)
#                 motor1.run(-100)
#             break
 
            
#     #move forward until distantce to object is 50 cm, stop, beep wait for button press

  
