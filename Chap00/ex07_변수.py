# 변수가 가리키는 메모리의 주소 확인
a = [1, 2, 3]
print(id(a))    # 2130600743432

#region 리스트를 복사
# 1. 얉은 복사
b = a           # 참조에 의한 복사(주소값 복사)
print(id(b))    # 2130600743432
print(a is b)   # True

a[1] = 4
print(a, b)     # [1, 4, 3] [1, 4, 3]

# 2. 깊은 복사
a = [1, 2, 3]
b = a[:]

a[1] = 4
print(a, b)     # [1, 4, 3] [1, 2, 3]

from copy import copy
b = copy(a)
print(a is b)   # False

#endregion

#region 변수를 만드는 여러 가지 방법

a, b = ('python', 'life')   # 튜플로 a, b에 값을 동시에 대입할 수 있다
print(a, b)                 # python life

a, b = 'hello', 'world'     # 튜플 부분에서도 언급했지만 튜플은 괄호를 생략해도 된다.
print(a, b)                 # hello world

[a,b] = ['python', 'life']  # 리스트로 변수 만들기
print(a, b)                 # python life

a = b = 'python'            # 여러 개의 변수에 같은 값 대입
print(a, b)                 # python python

a, b = 'hello', 'world'     # 위 방법으로 두 변수의 값 간단하게 바꾸기
a, b = b, a
print(a, b)                 # world hello

#endregion


















