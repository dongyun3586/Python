#region 1. 리스트의 인덱싱과 슬라이싱

# 리스트의 인덱싱
a = [1, 2, 3]
print(a[0], a[-1])  # 1 3

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1], a[-1][0])  # ['a', 'b', 'c'] a

a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])   # Life

#endregion

#region 2. 리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])   # [1, 2]

a = "12345"
print(a[0:2])   # [1, 2]
#endregion

#region 3. 리스트 연산하기

# 리스트 더하기
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)      # [1, 2, 3, 4, 5, 6]

# 리스트 반복하기(*)
print(a*3)      # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 리스트 길이구하기
print(len(a))   # 3

#endregion

#region 4. 리스트의 수정과 삭제

# 리스트에서 값 수정하기
a = [1, 2, 3]
a[2] = 4
print(a)    # [1, 2, 4]

# del 함수 사용해 리스트 요소 삭제하기
a = [1, 2, 3, 4, 5]
del a[1]
print(a)    # [1, 3, 4, 5]

del a[2:]
print(a)    # [1, 3]

#endregion

#region 5. 리스트 관련 함수들

# 리스트에 요소 추가(append)
a = [1, 2, 3]
a.append(4)
print(a)    # [1, 2, 3, 4]

a.append([5,6])
print(a)    # [1, 2, 3, 4, [5, 6]]

# 리스트 정렬(sort)
a = [1, 4, 3, 2]
a.sort()
print(a)    # [1, 2, 3, 4]

a = ['a', 'c', 'b']
a.sort()
print(a)    # ['a', 'b', 'c']

# 리스트 뒤집기(reverse)
a = ['a', 'c', 'b']
a.reverse()
print(a)    # ['b', 'c', 'a']

# 위치 반환(index)
a = [1,2,3]
print(a.index(3))   # 2 -> 리스트에 x 값이 있으면 x의 위치 값을 돌려준다.
print(a.index(1))   # 0

# 리스트에 요소 삽입(insert)
a = [1, 2, 3]
a.insert(0, 4)
print(a)        # [4, 1, 2, 3]

a.insert(3, 5)
print(a)        # [4, 1, 2, 5, 3]

# 리스트 요소 제거(remove)
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)        # [1, 2, 1, 2, 3] -> 리스트에서 첫 번째로 나오는 x를 삭제하는 함수

# 리스트 요소 끄집어내기(pop)
a = [1,2,3]
print(a.pop())  # 3
print(a)        # [1, 2]

a = [1,2,3]
print(a.pop(1)) # 2
print(a)        # [1, 3]

# 리스트에 포함된 요소 x의 개수 세기(count)
a = [1,2,3,1]
print(a.count(1))   # 2 -> 리스트 안에 x가 몇 개 있는지 조사하여 그 개수를 돌려주는 함수

# 리스트 확장(extend)
a = [1,2,3]
a.extend([4,5])
print(a)        # [1, 2, 3, 4, 5] -> xtend(x)에서 x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더하게 된다.

#endregion













