# 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
print(a)        # {1: 'a', 2: 'b'}

a['name'] = 'pey'
print(a)        # {1: 'a', 2: 'b', 'name': 'pey'}

a[3] = [1,2,3]
print(a)        # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 딕셔너리 요소 삭제하기
del a[1]
print(a)        # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 딕셔너리에서 Key 사용해 Value 얻기
a = {'a':1, 'b':2}
print(a['a'], a['b'])   # 1 2

#region 딕셔너리 관련 함수들

# Key 리스트 만들기(keys)
# 파이썬 3.0 이후 버전에서는 이러한 메모리 낭비를 줄이기 위해 dict_keys 객체를 돌려준다.
# 만약 3.0 이후 버전에서 반환 값으로 리스트가 필요한 경우에는 list(a.keys())를 사용하면 된다.
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())     # dict_keys(['name', 'phone', 'birth']) 

for k in a.keys():
    print(k, end=' ')   # name phone birth
print()

print(list(a.keys()))   # ['name', 'phone', 'birth']

# Value 리스트 만들기(values)
print(a.values())       # dict_values(['pey', '0119993323', '1118'])

# Key, Value 쌍 얻기(items)
print(a.items())        # dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')]

# Key: Value 쌍 모두 지우기(clear)
a.clear()
print(a)        # {}

# Key로 Value얻기(get)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))    # pey -> a.get('name')은 a['name']을 사용했을 때와 동일한 결괏값을 돌려준다.

# a['nokey']처럼 존재하지 않는 키(nokey)로 값을 가져오려고 할 경우 a['nokey']는 Key 오류를 발생시키고 a.get('nokey')는 None을 돌려준다
print(a.get('soft'))    # None

print(a.get('foo', 'bar'))  # bar -> 딕셔너리 안에 찾으려는 Key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져온다.

# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in a)  # True
print('email' in a) # False

#endregion






