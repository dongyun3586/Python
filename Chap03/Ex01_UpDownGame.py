import random
import os

# 입력값이 숫자인지 아닌지 체크하는 함수
def input_check(msg, casting=int):
    while True:
        try:
            user_input = casting(input(msg))
            return user_input
        except:
            print("숫자를 입력하세요")
            continue

os.system("cls")    # 콘솔 창의 내용을 깨끗하게 지워주는 도스 명령어
randNum = random.randint(1, 100)
count = 1
chance = 5

print("1 ~100 사이의 랜덤 숫자 맞추기 게임입니다.")
while count <= chance:
    user_input = input_check(f"{count}차 숫자는 무엇일까요? ")
    if randNum == user_input:
        break
    elif user_input < randNum:
        print(f"{user_input} 보다 큰 숫자 입니다.")
    elif user_input > randNum:
        print(f"{user_input} 보다 작은 숫자 입니다.")
    print()
    count += 1

if user_input == randNum:
    print(f"성공! 정답은 {randNum} 입니다.")
else:
    print(f"실패, 정답은 {randNum} 입니다.")