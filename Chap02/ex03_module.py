# 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파일
# 모듈 불러오기
# ※ import는 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있다.
# 파이썬 라이브러리는 파이썬을 설치할 때 자동으로 설치되는 파이썬 모듈을 말한다.

import Calculator   # import 모듈이름
a = 3
b = 4
print(f"{a} + {b} = {Calculator.add(3, 4)}")
print(f"{a} - {b} = {Calculator.subtract(3, 4)}")

from Calculator import add, subtract    # from 모듈이름 import 모듈함수
a = 3
b = 4
print(f"{a} + {b} = {add(3, 4)}")
print(f"{a} - {b} = {subtract(3, 4)}")

# sys 모듈 : 파이썬을 설치할 때 함께 설치되는 라이브러리 모듈
import sys
# print(sys.path) # sys.path는 파이썬 라이브러리가 설치되어 있는 디렉터리를 보여 준다.

for m in sys.path:  # sys.path는 리스트 append() 함수로 새로운 경로를 추가할 수도 있다.
    print(m)

# import ex02_class as f      

# a = 3
# b = 4
# print(f"{a} + {b} = {f.add(3, 4)}")
# print(f"{a} - {b} = {f.subtract(3, 4)}")

# fish1 = f.FishCakeMaker()  
# fish2 = f.FishCakeMaker(size=20, price=1000)  
# fish3 = f.FishCakeMaker(size=15, price=2000, flavor="초콜릿")  

# fish1.show_name()
# fish2.show_name()
# fish3.show_name()

# print(fish1)
# print(fish2)
# print(fish3)


