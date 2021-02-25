import random
import os

#region 중복없는 야구 숫자 3개 생성 및 저장(randNums 리스트에 저장)
randNums = []
randNum = str(random.randint(0, 9))     # 문자열이 인덱싱하기 편하기 때문에 문자열로 저장

for i in range(3):
    while randNum in randNums:
        randNum = str(random.randint(0, 9))
    randNums.append(randNum)
# print(randNums) # 정답 확인
#endregion

#region 변수 초기화, 게임 시작 알림 문자열 출력
count_strike = 0
count_ball = 0
count_try = 0           # 시도한 횟수
all_given_counts = 15   # 주어진 횟수

os.system("cls")
print("*" * 60)
print("야구 게임을 시작합니다.")
print("*" * 60)
#endregion

#region strike이 3개 될 때 까지 반복
while count_strike < 3:
    count_strike = count_ball = 0   # strike, ball 변수값 초기화
    count_try += 1

    inputNum = str(input(f"{count_try}회 시도 : 3자리 숫자를 입력하세요> "))
    if len(inputNum) == 3:
        for i in range(0, 3):
            for j in range(0, 3):
                if inputNum[i] == randNums[j] and i == j:   # 숫자와 자릿수도 같으면 스트라잌
                    count_strike += 1
                elif inputNum[i] == randNums[j] and i !=j:  # 숫자는 같은데 자릿수가 다르면 볼
                    count_ball += 1

    print("{} 스트라잌, {} 볼".format(count_strike, count_ball))
#endregion

if(count_strike == 3):
    print(f"성공!!! {count_try}번 만에 성공!!!")
else:
    print(f"실패!!! 주어진 기회 {all_given_counts}번을 모두 사용하셨습니다. \n 정답은{randNums}입니다.")
    

