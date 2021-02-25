## 입력받기1
# name = input("이름을 입력하세요 : ")
# print(name)

## 입력받기2
# num1 = int(input("숫자1: "))
# num2 = int(input("숫자2: "))
# print(num1 + num2)

# 입력받기 3
langs = ["한국어", "English"]
for i, l in enumerate(langs, start=1):
    print("{}. {}".format(i, l))

while True:
    sel = input("언어를 선택하세요 : ")

    if not sel.isnumeric(): # 입력 데이터가 숫자가 아니면 다시 반복
        continue

    sel = int(sel)          # sel을 정수로 캐스팅
    if 0 < sel < 3:         # sel값이 1, 2중 하나라면
        break

print("사용자가 선택한 언어는 {}입니다.".format(langs[sel - 1]))

# 한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end=' ')   # 0 1 2 3 4 5 6 7 8 9