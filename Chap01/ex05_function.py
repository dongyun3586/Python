#region 1. 사용자 함수 기본

def 함수명():
    print("사용자 정의 함수")
    return True

def add(a, b):
    # global c
    # c = a+b     # 함수 밖의 c 변수값이 바뀐다.  
    return a+b

def subtract(a, b):
    return a-b

print(add(5, 10))           # 15
print(subtract(5, 10))      # -5
print(subtract(b=5, a=10))  # 5
#endregion

#region 2. 입력값이 몇 개가 될지 모를 때
def add_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add_many(1, 2))           # 3
print(add_many(1, 2, 3, 4, 5))  # 15

def add_mul(choice, *args):
    if choice == "add": 
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

print(add_mul('add', 1,2,3,4,5))    # 15
print(add_mul('mul', 1,2,3,4,5))    # 120
#endregion

#region 3. 키워드 파라미터 kwargs

def print_kwargs(**kwargs):         # **을 붙이면 매개변수 kwargs는 딕셔너리가 되고 모든 key=value 형태의 결괏값이 그 딕셔너리에 저장된다.
    print(kwargs)                   # 모두 딕셔너리로 만들어져서 출력된다

print_kwargs(a=1)                   # {'a': 1}
print_kwargs(name='foo', age=3)     # {'name': 'foo', 'age': 3}
#endregion

#region 4. 함수의 결괏값은 언제나 하나
def add_and_mul(a,b):
    return a+b, a*b

print(add_and_mul(5, 10))       # (15, 50) -> 함수의 결과값은 하나이기 때문에 튜플이 생성되어 반환된다.
sum, mul = add_and_mul(5, 10)
print(sum, mul)                 # 15 50
#endregion

#region 5. 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")

say_myself("이동윤", 27)
say_myself("정은선", 27, False)
#endregion

#region 6. lambda
# lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할
# def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.
# lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식

add = lambda a, b: a+b
print(add(5, 10))       # 15

#endregion








