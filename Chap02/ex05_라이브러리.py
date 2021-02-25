#region sys -> 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

# 자신이 만든 모듈 불러와 사용하기 - sys.path
# 이 위치에 있는 파이썬 모듈은 경로에 상관없이 어디에서나 불러올 수 있다.
# import sys
# print(sys.path)     # 파이썬 모듈들이 저장되어 있는 위치
# sys.path.append("C:/doit/mymod")
# 이렇게 하고 난 후에는 C:/doit/Mymod 디렉터리에 있는 파이썬 모듈을 불러와서 사용할 수 있다.

#endregion

#region pickle -> 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
'''
import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)    # dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장
f.close()

f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)             # {2:'you need', 1:'python'}
'''
#endregion

#region os -> 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈

#endregion

#region shutil -> 파일을 복사해 주는 파이썬 모듈
# import shutil
# shutil.copy("src.txt", "dst.txt")
#endregion

#region time ->
import time
print(time.time())  # UTC(Universal Time Coordinated 협정 세계 표준시)를 사용하여 현재 시간을 실수 형태로 돌려주는 함수
print(time.localtime(time.time()))  # time.time()이 돌려준 실수 값을 사용해서 연도, 월, 일, 시, 분, 초, ... 의 형태로 바꾸어 주는 함수
print(time.asctime(time.localtime(time.time())))    # Sun Jul 12 21:57:34 2020 -> time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수
print(time.ctime())     # time.asctime(time.localtime(time.time()))과 같다
# time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))
print(time.strftime('%x', time.localtime(time.time())))     # 07/12/20
print(time.strftime('%c', time.localtime(time.time())))     # Sun Jul 12 22:00:25 2020

# time.sleep -> 주로 루프 안에서 많이 사용, 일정한 시간 간격
for i in range(10):
    print(i)
    # time.sleep(1)   # 1초 기다림

#endregion

#region calendar ->
import calendar
print(calendar.calendar(2020))      # 2020년 달력 출력
print(calendar.prmonth(2020, 7))    # 2020년 7월 달력 출력

# weekday(연도, 월, 일) 함수는 그 날짜에 해당하는 요일 정보를 돌려준다.
# 월요일은 0, 화요일은 1, 수요일은 2, 목요일은 3, 금요일은 4, 토요일은 5, 일요일은 6
print(calendar.weekday(2020,7,12))  # 6

# monthrange(연도, 월) 함수는 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지를 튜플 형태로 돌려준다.
print(calendar.monthrange(2020,7))  # (2, 31)
#endregion

#region random -> 난수(규칙이 없는 임의의 수)를 발생시키는 모듈
import random
print(random.random())  # 0.4288163561737126

# 1에서 10 사이의 정수 중에서 난수
print(random.randint(1, 10))   

# random_pop 함수는 리스트의 요소 중에서 무작위로 하나를 선택하여 꺼낸 다음 그 값을 돌려준다.
# 물론 꺼낸 요소는 pop 메서드에 의해 사라진다.
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: 
        print(random_pop(data))

data = [1, 2, 3, 4, 5]
random.shuffle(data)    # 리스트의 항목을 무작위로 섞고 싶을 때는 random.shuffle 함수를 사용
print(data)


#endregion

#region webbrowser -> 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈

import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com")    # 이미 웹 브라우저가 실행된 상태이더라도 새로운 창으로 해당 주소가 열리게 한다.

#endregion
















