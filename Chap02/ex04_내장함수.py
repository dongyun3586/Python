# 파이썬 내장 함수는 외부 모듈과 달리 import가 필요하지 않기 때문에 아무런 설정 없이 바로 사용할 수 있다.
# abs() -> 절댓값 반환 함수
print(abs(-3))  # 3 

#region enumerate() -> 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아
#  인덱스 값을 포함하는 enumerate 객체를 돌려준다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)  # 0 body ~ 2 bar
#endregion

#region eval -> 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수
print(eval('1+2'))              # 3
print(eval("'hi' + ' five'"))   # hi five
print(eval('divmod(7, 3)'))     # (2, 1)
#endregion

#region list(s) -> 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수
# list 함수에 리스트를 입력으로 주면 똑같은 리스트를 복사하여 돌려준다.
print(list("python"))   # ['p', 'y', 't', 'h', 'o', 'n']
print(list((1,2,3)))    # [1, 2, 3]
#endregion

#region filter() -> 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다.
#  두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서(걸러 내서) 돌려준다.
def positive(x):
    return x > 0

print(filter(positive, [1, -3, 2, 0, -5, 6]))           # <filter object at 0x0000021E7DDEA4C8>
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))     # [1, 2, 6]

# 앞의 함수는 lambda를 사용하면 positive() 함수 정의없이 코드를 작성할 수 있다.
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))  # [1, 2, 6]
#endregion

#region id() -> 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수
a = 3
print(id(a))   # 140708776082560
#endregion

#region input([prompt]) -> 사용자 입력을 받는 함수
b = input("Enter: ")
print(b)
#endregion

#region int() -> 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수
print(int('3'), int(3.4))   # 3 3
#endregion

#region isinstance(object, class ) -> 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.
# 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다. 
class Person : pass
a = Person()
print(isinstance(a, Person))    # True
#endregion

#region map(f, iterable) -> 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수
# 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. 
def two_times(x):
    return x*2

print(list(map(two_times, [1, 2, 3, 4])))       # [2, 4, 6, 8]
print(list(map(lambda x: x*2, [1, 2, 3, 4])))   # [2, 4, 6, 8]
#endregion

#region max(iterable) -> 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수
print(max([1, 2, 3]), max("python"))    # 3 y
print(min([1, 2, 3]), min("python"))    # 1 h
#endregion

#region open(filename, [mode]) -> "파일 이름"과 "읽기 방법"을 입력받아 파일 객체를 돌려주는 함수
# 읽기 방법(mode)을 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다.
# f = open("binary_file", "rb")     # rb는 "바이너리 읽기 모드"를 의미
# fread = open("read_mode.txt", 'r')와 fread2 = open("read_mode.txt")는 동일하다.
# fappend = open("append_mode.txt", 'a')    # 추가 모드(a)
#endregion

#region pow(x, y) -> x의 y 제곱한 결괏값을 돌려주는 함수
print(pow(2, 4), pow(3, 3))     # 16 27
#endregion  

#region range([start,] stop [,step] ) -> 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다.
# for문과 함께 자주 사용하는 함수
print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(5, 10)))       # [5, 6, 7, 8, 9]
print(list(range(1, 10, 2)))    # [1, 3, 5, 7, 9]
#endregion

#region round(number[, ndigits]) -> 숫자를 입력받아 반올림해 주는 함수
print(round(4.6))       # 5 
print(round(4.2))       # 4
print(round(5.678, 2))  # 5.68
#endregion

#region sorted(iterable) -> 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수
print(sorted([3, 1, 2]))        # [1, 2, 3]
print(sorted(['a', 'c', 'b']))  # ['a', 'b', 'c']
print(sorted("zero"))           # ['e', 'o', 'r', 'z']
#endregion

#region str(object) -> 문자열 형태로 객체를 변환하여 돌려주는 함수
print(str(3), str('hi'.upper()))    # 3 HI
#endregion

#region sum(iterable) -> 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수
print(sum([1,2,3]), sum((1,2,3)))   # 6 6
#endregion 

#region tuple(iterable) -> 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수
print(tuple("abc"))         # ('a', 'b', 'c')
print(tuple([1, 2, 3]))     # (1, 2, 3)
#endregion

#region type(object) -> 입력값의 자료형이 무엇인지 알려 주는 함수
print(type("abc"))      # <class 'str'>
print(type([ ]))        # <class 'list'>
#endregion



