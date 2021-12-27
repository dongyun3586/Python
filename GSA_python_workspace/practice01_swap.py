a = input("첫 번째 숫자 입력: ")
b = input("두 번째 숫자 입력: ")
print(f'a={a}, b={b}')

a, b = b, a
print(f'a={a}, b={b}')