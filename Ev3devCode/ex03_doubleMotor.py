# 원하는 거리만큼 움직이기

# 1.스피드 20으로 1초동안 움직인 거리
tank_drive.on_for_seconds(left_speed=20, right_speed=20, seconds=1, brake=True, block=True)

distanceForOneSecond = 10   # 1초 동안 움직인 거리가 10cm 라면

def moveTheDistanceUsingSeconds(distance):
    tank_drive.on_for_seconds(20, 20, seconds=distance/distanceForOneSecond)

moveTheDistanceUsingSeconds(10)

# 2.각도로 원하는 거리만큼 이동시키는 함수
def moveTheDistanceUsingDegrees(distance):
    tank_drive.on_for_degrees(20, 20, degrees = 20.48 * distance)   # 360도 = 17.58cm, 1cm = 20.47도

moveTheDistanceUsingDegrees(10)

# 원하는 거리만큼 움직이기
def move(direction, distance):
    if direction == 'forward':
        tank_drive.on_for_degrees(20, 20, degrees = 20.48 * distance)   # 360도 = 17.58cm, 1cm = 20.47도
    elif direction == 'backward':
        tank_drive.on_for_degrees(-20, -20, degrees = 20.48 * distance)


move('forward', 10)
move('backward', 10)

# 원하는 각도만큼 회전하기
def rotate(direction, degrees):
    if direction == 'turnToLeft':
        tank_drive.on_for_seconds(-20, 20, degrees/100)  # 100 = 1초 동안 회전한 각도가 100도라면
    elif direction == 'turnToRight':
        tank_drive.on_for_seconds(20, -20, degrees/100)

rotate('turnToLeft', 180)
rotate('turnToRight', 180)
