# 윤년 판단 프로그램
y = int(input('년도를 입력하시오: '))

if((y % 4 == 0 and y % 100 != 100) or y % 400 == 0):
    print(f'{y}년은 윤년입니다.')
else:
    print(f'{y}년은 평년입니다.')                   