import time
from selenium import webdriver                          # sudo apt install python3-selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# 에러 코드 제거usb_device_handle_win.cc:1020 Failed to read descriptor from node connection:  시스템에 부착된 장치가 작동하지 않습니다. (0x1F)
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

path = '/home/ldy/pythonCode/chromedriver_linux64/chromedriver'
s = Service(executable_path=path)
driver = webdriver.Chrome(service=s)
url = "https://hcs.eduro.go.kr"

# 셀레늄/Chromedriver로 웹 페이지 자동 새로 고침 중지

driver.get(url)     # 이 url을 크롬 웹브라우저에서 열기

# 크롬 개발자 도구로 [자가진단 참여하기 GO] 버튼의 id값 알아내기 => btnConfirm2
# 버튼의 xpath값으로 [자가진단 참여하기 GO] 버튼 클릭하기 
driver.find_element_by_xpath('//*[@id="btnConfirm2"]').click()

# '학교' 입력창 클릭하기 
driver.find_element_by_xpath('//*[@id="schul_name_input"]').click()

# 시/도 선택하기 '광주광역시'
driver.find_element_by_xpath('//*[@id="sidolabel"]/option[6]').click()

# 학교급 선택하기 '고등학교'
driver.find_element_by_xpath('//*[@id="crseScCode"]/option[5]').click()

# 학교명 입력하기
driver.find_element_by_xpath('//*[@id="orgname"]').send_keys('광주과학고')

# [검색(Search)] 버튼 클릭하기
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()

time.sleep(1)
# 검색으로 생성된 [광주과학고등학교] 선택하기
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul').click()

# [학교선택/Select School] 버튼 클릭하기
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()

# 이름 입력하기
driver.find_element_by_xpath('//*[@id="user_name_input"]').send_keys('이동윤')

# 생년월일 입력하기
driver.find_element_by_xpath('//*[@id="birthday_input"]').send_keys('790204')
# [Enter] 치기
driver.find_element_by_xpath('//*[@id="birthday_input"]').send_keys(Keys.ENTER)

time.sleep(1)
# 비밀번호(Password) 입력하기
driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/input').send_keys('0509')

time.sleep(1)
# [Enter] 치기
driver.find_element_by_xpath('//*[@id="btnConfirm"]').send_keys(Keys.ENTER)
time.sleep(3)

# 사용자 계정의 버튼 클릭하기
# driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul').click()
# driver.find_element()
driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a/span[1]').click()

time.sleep(3)
# 1번 라디오 버튼 선택하기
driver.find_element_by_xpath('//*[@id="survey_q1a1"]').click()

time.sleep(1)
# 2번 라디오 버튼 선택하기
driver.find_element_by_xpath('//*[@id="survey_q2a1"]').click()

time.sleep(1)
# 3번 라디오 버튼 선택하기
driver.find_element_by_xpath('//*[@id="survey_q3a1"]').click()

time.sleep(1)
# [제출 / Submit] 버튼 클릭하기
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

time.sleep(2)

# quit all webdriver
driver.quit() 

