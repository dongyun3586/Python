#region 1. 집합 자료형의 특징
# 1. 중복을 허용하지 않는다.
# 2. 순서가 없다(Unordered).
# ※ 중복을 허용하지 않는 set의 특징은 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용하기도 한다.


# 집합 자료형 만들기
s1 = set([1,2,3])   # 집합 자료형은 set 키워드를 사용해 만들 수 있다.
print(s1)           # {1, 2, 3}

s2 = set("Hello")
print(s2)           # {'o', 'l', 'e', 'H'}

# 만약 set 자료형에 저장된 값을 인덱싱으로 접근하려면, 리스트나 튜플로 변환한후 해야 한다.
l1 = list(s1)
print(l1)       # [1, 2, 3]

t1 = tuple(s1)
print(t1)       # (1, 2, 3)
#endregion

#region 2. 교집합, 합집합, 차집합 구하기
# set 자료형을 정말 유용하게 사용하는 경우는 교집합, 합집합, 차집합을 구할 때이다.

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 1. 교집합
print(s1 & s2)              # {4, 5, 6}
print(s1.intersection(s2))  # {4, 5, 6} -> intersection 함수도 같은 결과

# 2. 합집합
print(s1 | s2)              # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2))         # {1, 2, 3, 4, 5, 6, 7, 8, 9} -> union 함수도 같은 결과

# 3. 차집합
print(s1 - s2)              # {1, 2, 3}
print(s1.difference(s2))    # {1, 2, 3} -> difference 함수도 같은 결과

#endregion

#region 3. 집합 자료형 관련 함수들

# 값 1개 추가하기(add)
s1 = set([1, 2, 3])
s1.add(4)
print(s1)       # {1, 2, 3, 4}

# 값 여러 개 추가하기(update)
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)       # {1, 2, 3, 4, 5, 6}

# 특정 값 제거하기(remove)
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)       # {1, 3}

#endregion













