# 화면을 감시하다가 다음으로 넘어가라는 이미지가 발견되면 다음 버튼을 클릭한다.
import pyautogui as pag
import time
import keyboard
import os

# 1. 다음으로 넘어가는 버튼의 좌표 저장
print('다음으로 넘어가는 버튼의 위치에서 F4키를 누르시오')
while True:
    if keyboard.is_pressed("F4"):
        nextBtnPos = pag.position()
        print('nextBtnPos = ', nextBtnPos)
        time.sleep(0.5)
        break
time.sleep(1)

# 2. 화면 학습이 종료되었다는 메시지가 나타나면 다음 버튼 클릭
# 화면 종료 이미지 파일 이름 리스트 만들기
path_imgDir = '.\images'    # 현재 폴더의 하위 폴더 'images'
imgFile_list = os.listdir(path_imgDir)
print(imgFile_list)

while True:
    
    # 학습 종료 이미지 검색
    print('스크린에서 현재 페이지 학습완료 이미지 검색중') 
    while True:
        for imgFile in imgFile_list:
            nextImgList = list(pag.locateAllOnScreen('./images/' + imgFile, confidence=0.95))
            if nextImgList:
                break
        # for i in range(1, 6):
        #     nextImgList = list(pag.locateAllOnScreen('./images/next{}.png'.format(i), confidence=0.95))
        #     if nextImgList:
        #         break
        # 빈 리스트가 아니라면 True
        if nextImgList:
            nextImg_pos = nextImgList[0]
            print('해당 화면의 학습완료 이미지 발견')
            print('nextImgList = ', nextImgList)
            print('nextImg_pos = ', nextImg_pos)
            break
        
    # [다음 버튼] 클릭    
    # pag.moveTo(nextBtnPos, duration=2)  # 2초 동안 [다음 버튼] 위로 이동
    pag.click(nextBtnPos)
    
    # 마우스 포인터를 대기 위치로 옮기기
    pag.moveTo(500, 500, 1)




# pag.moveTo(nextBtnPos, duration=2)  # 2초 동안 [다음 버튼] 위로 이동
# pag.click()
# pag.moveTo(0, 0, 2)
# pag.moveTo(nextBtnPos.x, nextBtnPos.y, duration=2)
# pag.click()
# while True:
#     # 1. 다음으로 넘어가는 버튼의 좌표 알아내기
#     print(pag.position())
    
    # # 1. 화면에서 다음으로 넘어가는 이미지 찾기
    # nextImg_pos = pyautogui.locateCenterOnScreen('next1.png')
    # pyautogui.click(nextImg_pos)