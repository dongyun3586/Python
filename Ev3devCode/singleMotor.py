#!/usr/bin/env python3
from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM

lm = LargeMotor(OUTPUT_C)   # 연결 포트를 지정 안하면 기본 포트로 동작

#region 시간으로 제어 => on_for_seconds(speed, seconds, brake=True, block=True)
#region 1.시간으로 제어
lm.on_for_seconds(speed = 50, seconds=3)    # maximum speed(1050 deg/s)의 50% 속도로 3초 동안 회전
sleep(1)
lm.on_for_seconds(50, 3)   # 매개 변수 이름을 명시하지 않아도 된다. 
sleep(1)
#endregion

#region 2.시간당 각도로 제어
lm.on_for_seconds(speed=SpeedDPS(300), seconds=3)   # DPS(degrees per second) 초당 300도를 도는 속도로 3초 동안 회전
sleep(1)
lm.on_for_seconds(speed=SpeedDPM(36000), seconds=3) # DPM(degrees per minute) 분당 36000도
sleep(1)
#endregion

#region 3.시간당 회전수로 제어 
lm.on_for_seconds(speed=SpeedRPS(1), seconds=2)     # RPS(rotations per second) 초당 1바퀴를 도는 속도로 seconds 초 동안 회전
sleep(1)    
lm.on_for_seconds(speed=SpeedRPM(100), seconds=3)   # RPM(rotations per minute) 분당 100바퀴를 도는 속도 seconds 초 동안 회전
sleep(1)
#endregion
#endregion

#region 바퀴 회전으로 제어 => on_for_rotations(speed, rotations, brake=True, block=True)
#region 1.모터의 정격 스피드의 비율로 동작 
lm.on_for_rotations(speed=50, rotations=3)  # 정격 최대 속도(1050 deg/s)의 50%의 속도로 3바퀴 회전 
sleep(1)
lm.on_for_rotations(50, 3)  # 매개 변수 이름을 명시하지 않아도 된다. 
sleep(1)
#endregion

#region 2.시간당 지정된 스피드로 rotations 바퀴만큼 회전 
lm.on_for_rotations(speed=SpeedDPS(500), rotations=3)   # DPS(degrees per second) 초당 500도를 도는 속도로 3바퀴 회전
sleep(1) 
lm.on_for_rotations(speed=SpeedRPS(1), rotations=3)     # RPS(rotations per second) 초당 1 바퀴를 도는 속도로 3바퀴 회전
sleep(1)
#endregion
#endregion

#region break, block
# break : True 인 경우 모터가 동작을 완료하면 모터를 고정위치에 붙잡는다.
# block : 현재 명령이 완료 될 때까지 프로그램 실행을 일시 중지
#endregion

#region 계속 회전하기 => on(speed, brake=True, block=False)
lm.on(speed=80, brake=False) # 정격 최고 속도의 45 %의 속도로 계속 회전
sleep(2)
lm.off()        # 정지
#endregion

#region Run a single motor until it stops moving
# # 그리퍼의 팔이 바닥까지 내려갈 때 어떤 각도 또는 시간동안 내려가야하는지 정확히 알 수 없다.
# # 이 명령은 일반적으로이 on() 명령 다음에 실행된다.
# # 움직이는 휠을 잡고 멈 추면 스크립트가 종료된다.
lm.on(speed=20)
lm.wait_until_not_moving()
#endregion