price = int(input("물건 가격: "))
received_money = int(input("받은 금액: "))

change = received_money-price

print('*** 거스름 돈 ***')
print(f"10000원: {change//10000}장")
change %= 10000
print(f" 5000원: {change//5000}장")
change %= 5000
print(f" 1000원: {change//1000}장")