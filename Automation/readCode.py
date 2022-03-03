import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip


f = open("suhang1_1101.c", mode="r", encoding="utf-8")
data = f.read()     # f.read()는 파일의 내용 전체를 문자열로 돌려준다.
f.close()

# 온라인 컴파일러 사이트 실행시키기
driver = webdriver.Chrome(executable_path='chromedriver')   # 드라이버 로드
URL = 'https://www.onlinegdb.com/'
driver.get(url=URL) # 브라우저 띄우기
time.sleep(2) #로딩 대기

# 온라인 컴파일러 우측 상단의 Language 부분을 C로 선택
driver.find_element_by_xpath('//*[@id="lang-select"]/option[2]').click()
time.sleep(1)

# 코드창 선택
codeBox = driver.find_element_by_xpath('//*[@id="editor_1"]/textarea')
codeBox.Clear()
time.sleep(1)

# # 코드 붙여넣기
# pyperclip.copy("Hello World")
# driver.find_element_by_xpath('//*[@id="editor_1"]/textarea').send_keys(Keys.CONTROL, 'v')


