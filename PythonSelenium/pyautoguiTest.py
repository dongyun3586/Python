import pyautogui as pag

# 마우스의 x, y 위치 알아내기
x, y = pag.position()
print(x, y)

# 로그인 버튼 마우스 클릭
pag.click(847, 646)

# 로그인 버튼 마우스 클릭
pag.click(857, 547)

# 시/도
pag.click(854, 366)

# 학교급
pag.click(751, 455)

# # 아이디 입력하기
# pag.typewrite("id")

# # Enter키 누르기
# pag.press("enter")