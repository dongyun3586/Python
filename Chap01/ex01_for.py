#반복문 for

# 1~10까지 2 간격으로 출력
for i in range(1, 10, 2):
    print(i)

# 리스트 안의 튜플의 모든 요소 차례대로 출력
a = [(1,2), (3,4), (5,6)]
for i in a:         # i==(1,2)
    for j in i: 
        print(j)

# 딕셔너리와 반복문
student = [{"홍길동": 100}, {"가제트": 200}, {"가가멜": 300}]
for i in student:
    print(i)                    # {'홍길동': 100}
    print(i.items())            # dict_items([('홍길동', 100)])
    print(list(i.items()))      # [('홍길동', 100)] -> 리스트 안에 튜플
    print(list(i.items())[0])   # ('홍길동', 100) -> 튜플만 꺼내기

    data = list(i.items())[0]   # ('홍길동', 100)
    key = data[0]               # '홍길동'
    value = data[1]             # '100'
    print("key: {}, value: {}".format(key, value))  # key: 홍길동, value: 100

# 시퀀스를 루핑할 때, enumerate() 함수를 사용하면 위치 인덱스와 대응하는 값을 동시에 얻을 수 있다.
# for, enumerate(요소, [start=1])
student = [{"홍길동": 100}, {"가제트": 200}, {"가가멜": 300}]
for index, value in enumerate(student, start=1):
    data = list(i.items())[0]   # ('홍길동', 100)
    key = data[0]               # '홍길동'
    value = data[1]             # '100'
    print("{}. key: {}, value: {}".format(index, key, value))  # 1. key: 가가멜, value: 300

# 리스트 컴프리헨션
result = []
for num in range(1, 6):
    result.append(num+5)
print(result)     # [6, 7, 8, 9, 10]

result = [num+5 for num in range(1, 6)]
print(result)     # [6, 7, 8, 9, 10]

result = []
for num in range(1, 10):
    if num%2 == 0:
        result.append(num+5)
print(result)   # [7, 9, 11, 13]

result = [num+5 for num in range(1, 10) if num%2 == 0]
print(result)   # [7, 9, 11, 13]

