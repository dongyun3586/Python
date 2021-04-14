#!/usr/bin/env python3 
from time import sleep 
from ev3dev2.motor import MediumMotor, MoveTank, OUTPUT_B, OUTPUT_C 
from ev3dev2.sensor.lego import ColorSensor, TouchSensor, UltrasonicSensor, GyroSensor
from ev3dev2.sound import Sound
from sys import stderr 

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C) 
sound = Sound()
ts = TouchSensor() 
cl = ColorSensor()
us = UltrasonicSensor() 
# gy = GyroSensor()

sound.beep()    # 시작 비프음

#region 1.print EV3 LCD와 VS Code에 출력하기
while not ts.is_pressed:
    print("hello EV3")                  # print to EV3 LCD screen
    print("hello VS Code", file=stderr) # print to VS Code output panel
#endregion

# region 2.ColorSensor값 출력하기
while not ts.is_pressed:
    print(cl.reflected_light_intensity) 
    print(cl.reflected_light_intensity, file=stderr)              # 반사광 측정값 출력
    print("{}({})".format(cl.color_name, cl.color), file=stderr)  # 측정된 색상 이름(색상 번호) 출력
    sleep(0.5)
# endregion

# region  2.UltrasonicSensor 출력하기
while not ts.is_pressed:
    print(us.distance_centimeters, file=stderr)
    sleep(0.5)
# endregion

#region Test Code(GyroSensor)
targetAngle = 90
print ("start angle : {}".format(gy.angle), file=stderr)  # 회전 시작 각도

if targetAngle > 0:
    targetAngle = gy.angle + targetAngle
    print("target angel : {}".format(targetAngle), file=stderr)

    tank_drive.on(left_speed=20, right_speed=-20)

    while gy.angle < targetAngle:
        print('gy.angle : {}'.format(gy.angle), file=stderr)
        sleep(0.01)
else:
    targetAngle = gy.angle + targetAngle
    print("target angel : {}".format(targetAngle), file=stderr) 

    tank_drive.on(left_speed=-20, right_speed=20)

    while gy.angle > targetAngle:
        print('gy.angle : {}'.format(gy.angle), file=stderr)
        sleep(0.01)

tank_drive.off()
print ('end angle: {}'.format(gy.angle), file=stderr) 
#endregion

sound.beep()    # 종료 비프음