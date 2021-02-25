# 파이썬 예외 처리
# val = "10.4"
# n = int(val)

# 예외 처리1
try:
    val = "10.4"
    n = int(val)
except ValueError as e:
    print("오류 발생 : {}".format(e))

# 예외 처리2
try:
    idx = []
    idx[0] = 100
except IndexError as e:
    print("오류 발생 : {}".format(e))

# 예외 처리3
try:
    val = "10.4"
    n = int(val)
    idx = []
    idx[0] = 100
except Exception as e:
    print("오류 발생 : {}".format(e))

# 예외 처리4
try:
    val = "10"
    n = int(val)
except:
    print("오류 발생 : {}".format(e))
else:
    print("정상 동작")
finally:
    print("finally 코드 동작")
