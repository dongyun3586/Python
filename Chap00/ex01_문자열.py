### 문자열 ###

#region 1. 백슬래시(\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
# 백슬래시(\) 뒤의 작은따옴표(')나 큰따옴표(")는 문자열을 둘러싸는 기호의 의미가 아니라 문자 ('), (") 그 자체를 의미한다.
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."   

print(food, '\n', say)
#endregion

#region 2. 여러 줄인 문자열을 변수에 대입하고 싶을 때
# 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
multiline = "Life is too short\nYou need python"

# 연속된 작은따옴표 3개(''') 또는 큰따옴표 3개(""") 사용하기
multiline='''
Life is too short 
You need python
'''
print(multiline)

multiline="""
Life is too short 
You need python
"""
print(multiline)    # 문자열이 여러 줄인 경우 이스케이프 코드를 쓰는 것보다 따옴표를 연속해서 쓰는 것이 훨씬 깔끔
#endregion

#region 3. 문자열 연산하기
# 문자열 더해서 연결하기(Concatenation)
head = "Python"
tail = " is fun!"
print(head + tail)  # Python is fun!

# 문자열 곱하기
print(head * 5)     # PythonPythonPythonPythonPython

# 문자열 길이 구하기
print(len(head)) # 6
#endregion

#region 4. 문자열 인덱싱과 슬라이싱
# 문자열 인덱싱
a = "Life is too short, You need Python"
print(a[3])     # e
print(a[-1])    # n

# 문자열 슬라이싱
print(a[0:4])   # Life  a[시작 번호:끝 번호]를 지정할 때 끝 번호에 해당하는 것은 포함하지 않는다.
print(a[19:])   # 끝 번호 부분을 생략하면 시작 번호부터 그 문자열의 끝까지 뽑아낸다.
print(a[:17])   # 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아낸다.
print(a[:])     # 시작 번호와 끝 번호를 생략하면 문자열의 처음부터 끝까지를 뽑아낸다.
print(a[19:-7]) # - 사용 가능
#endregion

#region 5. 문자열 포매팅(Formatting)
print("I eat %d apples." % 3)       # I eat 3 apples.
print("I eat %s apples." % "five")  # I eat five apples.
print("I ate %d apples. so I was sick for %s days." % (3, 'three')) # I ate 3 apples. so I was sick for three days.
print("Error is %d%%." % 98)        # Error is 98%. -> %를 출력할려면 %%를 사용

# 정렬과 공백
print("%10sjane." % "hi")       #         hijane. -> 문자열 왼쪽에 여백
print("%-10sjane." % 'hi')      # hi        jane. -> 문자열 오른쪽에 여백

# 소수점 표현하기
print("%0.4f" % 3.42134234)     # 3.4213
print("%10.4f" % 3.42134234)    #     3.4213

# format 함수를 사용한 포매팅
print("I eat {0} apples".format(3))
print("I ate {0} apples. so I was sick for {1} days.".format(10, 3))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))

# f 문자열 포매팅(파이썬 3.6 버전부터 사용 가능)
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')     # 나의 이름은 홍길동입니다. 나이는 30입니다.

# 딕셔너리는 f 문자열 포매팅
d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
#endregion

#region 6. 문자열 관련 함수들
# 문자 개수 세기(count)
a = "hobby"
print(a.count('b')) # 2 -> 문자열 중 문자 b의 개수

# 위치 알려주기1(find)
a = "Python is the best choice"
print(a.find('b'))  # 14 -> 문자열 중 문자 b가 처음으로 나온 위치를 반환
print(a.find('k'))  # -1 -> 찾는 문자나 문자열이 존재하지 않는다면 -1을 반환

# 위치 알려주기2(index)
a = "Life is too short"
print(a.index('t')) # 8 -> 문자열 중 문자 t가 맨 처음으로 나온 위치를 반환

# 문자열 삽입(join)
print(",".join('abcd'))                 # a,b,c,d -> abcd 문자열의 각각의 문자 사이에 ','를 삽입
print(",".join(['a', 'b', 'c', 'd']))   # a,b,c,d -> 문자열뿐만 아니라 앞으로 배울 리스트나 튜플에도 사용 가능

# 대/소문자로 바꾸기(upper, lower)
print(a.upper())    # LIFE IS TOO SHORT
print(a.lower())    # life is too short

# 공백 지우기
a = ' hi '
print(a.lstrip())   # 왼쪽 공백 지우기
print(a.rstrip())   # 오른쪽 공백 지우기
print(a.strip())    # 양쪽 공백 지우기

# 문자열 바꾸기(replace)
a = "Life is too short"
print(a.replace("Life", "Your leg"))    # Your leg is too short

# 문자열 나누기(split) -> list로 반환
a = "Life is too short"     # ['Life', 'is', 'too', 'short']
print(a.split())

b = "a:b:c:d"
print(b.split(':'))         # ['a', 'b', 'c', 'd']
#endregion






