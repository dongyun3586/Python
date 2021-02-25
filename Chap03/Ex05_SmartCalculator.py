import os

operator = ['+', '-', '*', '/', '=']
# user_input = '500 + 5 * 10'

def string_calculator(user_input):
    string_list = []
    indexLastOperator = 0   # 마지막 연산자의 위치 index값 저장 변수

    #region enumerate(iterable, start=0) 설명
    '''
    - iterable : 시퀀스, 이터레이터 또는 이터레이션을 지원하는 다른 객체
    - 반환값 : 카운트 (기본값 0을 갖는 start 부터)와 iterable 을 이터레이션 해서 얻어지는 값을 포함하는 튜플 반환

    <예시>
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    list(enumerate(seasons))
    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    list(enumerate(seasons, start=1))
    [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
    '''
    #endregion

    # 사용자 입력 연산식의 마지막에 "=" 추가(마지막 숫자까지 string_list에 저장하기 위해 )
    if user_input[-1] not in operator:
        user_input += "="

    # 연산자 이전의 숫자와 연산자를 저장하는 반복문 '500 + 5 * 10'
    for i, s in enumerate(user_input):      
        # print(i, s)
        if s in operator:   # 연산자 이면
            prevNum = user_input[indexLastOperator:i].strip()   # 연산자 이전까지의 문자를 공백을 제거하여 저장
            if prevNum != "":               
                string_list.append(prevNum)     # string_list에 연산자 이전의 숫자 추가
                string_list.append(s)           # string_list에 연산자 추가
                indexLastOperator = i + 1       # 저장된 연산자 이후의 index 넘버로 변경

    string_list = string_list[:-1]  # 마지막에 추가한 "=" 제거
    # print(string_list)

    #region 반복문 연산 과정
    # ['10', '+', '20', '+', '30', '+', '40']
    # ['30', '+', '30', '+', '40']
    # ['60', '+', '40']
    # ['100']
    #endregion 
    pos = 0
    while True:
        # 리스트에 하나의 아이템만 남으면 반복 종료
        if len(string_list) == 1:   
            break
        
        if string_list[pos] in operator:            # 리스트의 아이템이 연산자이면
            temp = string_list[pos-1] + string_list[pos] + string_list[pos + 1]     # 피연산자+연산자+피연산자의 문자열 완성
            del string_list[0:3]                    # temp에 저장된 피연산자+연산자+피연산자 아이템 제거
            string_list.insert(0, str(eval(temp)))  # 리스트의 0번째 위치에 temp의 계산 결과 저장
            pos = 0         # pos 초기화
        pos += 1            # pos를 1 증가시켜 다음 아이템을 가리키는 index값으로 변경
        # print(string_list)  # 리스트의 값 출력

    if len(string_list) > 0:
        result = float(string_list[0])  # 최종 계산 결과를 result에 저장

    return round(result, 4)     # 결과를 소수점 이하 4자리까지로하여 반환

while True:
    os.system("cls")

    user_input = input("계산식을 입력하세요> ")
    if user_input == "/exit":
        break

    result = string_calculator(user_input)
    print("결과: {}".format(result))

    os.system("pause")

