import random
import os

# 영단어 리스트 원본(한글단어가 key값, 영단어가 value값)
words_dict = {"사자": "lion", "호랑이": "tiger", "사과": "apple", "비행기": "airplane"}

#region 영단어 리스트 복제, 아이템 순서 섞기
words = []
for word in words_dict:
    words.append(word)
random.shuffle(words)   # 리스트의 아이템 순서 섞기
#endregion

#region 변수 초기화, 게임 시작 알림 문자열 출력
right_answer = 0
wrong_answer = 0
quiz_num = 0

os.system("cls")
print("*" * 60)
print("영어 스펠링 게임을 시작합니다.")
print("틀려도 1번의 기회가 더 주어집니다.")
print("*" * 60, '\n')
#endregion

# 한글 단어를 영어 스펠링으로 작성하는 문제 풀이
chance = 2
for i in range(0, len(words)):      # 리스트에 저장된 영단어 개수만큼 반복
    quiz_num += 1                   # 문제 번호 1 증가
    questionWord = words[i]         # 영단어의 한글 뜻 저장
    for j in range(0, chance):      # 틀려도 1번의 기회를 더 제공
        user_input = str(input(f"{quiz_num}번 문제 : {questionWord}의 영어 단어를 입력하세요> "))
        english = words_dict[questionWord]  # key값(한글)으로 value값(영단어) 가져오기

        # 사용자 입력에서 공백을 제거하고 소문자로 변환하여 스펠링 비교
        if user_input.strip().lower() == english.lower():  
            right_answer += 1 
            print("정답 입니다.\n")
            break
        else:
            wrong_answer += 1
            print("틀렸습니다.\n")

    # 같은 단어를 3번 틀리면 정답을 알려준다.
    if user_input.strip().lower() != english.lower():
        print(f"정답은 {english} 입니다.")

print("더 이상 문제가 없습니다.")
print(f"정답 {right_answer}개, 오답 {wrong_answer}개")