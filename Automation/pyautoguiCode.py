import pyautogui
import time
import keyboard

#region 1. 마우스, 키보드 제어
# print(pyautogui.size())

# # 현재 마우스 좌표값 알아내기
# print(pyautogui.position())

# # 마우스 특정 좌표로 움직이기
# pyautogui.moveTo(100, 100, 2)  # 절대 좌표 움직임, 2초 동안
# pyautogui.moveRel(100, 0, 1)   # 상대 좌표 움직임, 1초 동안

# # 클릭
# pyautogui.click()               
# pyautogui.click(100, 100)       # 좌표를 넣을수도 있다.
# pyautogui.doubleClick()

# # 기다리기
# time.sleep(1)

# ## 키보드 제어
# # 글씨 쓰기
# pyautogui.typewrite('Hello')

# # Enter키 치기
# pyautogui.typewrite(['enter'])
#endregion

#region 2. 이미지로 화면에서 좌표를 알아내 마우스 클릭
# # pip install opencv-python 설치

# # 저장된 이미지로 화면에서 같은 이미지 찾기
# # 계산기에서 숫자 7 버튼을 찾아서 클릭하기
# # img = pyautogui.locateOnScreen('7.png')
# # img_center = pyautogui.center(img)
# # print('img : ', img)

# # 한번에 센터좌표까지 구해서 저장
# # img_center = pyautogui.locateCenterOnScreen('7.png')

# # pyautogui.click(img_center)

# # 화면 캡쳐로 이미지 저장하기
# # print(pyautogui.position())  # 계산기의 숫자1 위에서 실행
# pyautogui.screenshot('1.png', region=(570, 790, 50, 50))
# num1 = pyautogui.locateCenterOnScreen('1.png')
# pyautogui.click(num1)

# # 이미지 검색
# pyautogui.locateAllOnScreen('1.png', confidence=0.98)




#endregion

#region 3. 키보드 입력으로 제어
# pip install keyboard로 설치
# while True:
#     if keyboard.is_pressed("F4"):
#         pos = pyautogui.position()
#         print(pos)
#         time.sleep(0.5)
#         break

print(pyautogui.position())
