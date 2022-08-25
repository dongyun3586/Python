# # 2. 파일을 쓰기 모드로 열어 출력값 작성하기
# f = open("test/hello_world.txt", 'w', encoding='utf-8')
# for i in range(1, 11):
#     f.write(f"{i} 번째 Hello World\n")
# f.close()

path = "test"

# 6. with문 사용하여 파일 읽기(자동으로 자원을 닫아준다.)
with open(f"{path}/새파일.txt", mode="w", encoding="utf-8") as f:
    f.write("Hello World\nHello World")