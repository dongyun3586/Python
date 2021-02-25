print(1 == 1)       # True
print(1 > 2)        # False

# 자료형의 참과 거짓 
# -> 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있으면(" ", [ ], ( ), { }) 거짓
# -> 숫자에서는 그 값이 0일 때 거짓

if []:
    print("참")
else:
    print("거짓")   # 거짓
# -----------------------------------------
a = [1, 2, 3, 4]
while a:
    print(a.pop())
# 4
# 3
# 2
# 1

# 불 연산
print(bool('python'))   # True
print(bool(''))         # False
print(bool([1,2,3]))    # True
print(bool([]))         # False
print(bool(0))          # False
print(bool(3))          # True

print('a' in ('a', 'b', 'c'))   # True
print('j' not in 'python')      # True
