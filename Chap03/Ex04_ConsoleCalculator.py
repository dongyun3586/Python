import os

while True:
    os.system("cls")
    s = input("계산식 입력> ")
    print("결과: {}".format(eval(s)))   # eval(string) 입력된 string에서 계산식을 인식하여 계산 결과를 반환함.
    os.system("pause")