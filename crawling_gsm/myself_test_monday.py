from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
from random import randint 

nowTime = datetime.datetime.now()
print('자가진단 셀프 체크 프로그램 시작 시간: ', nowTime)

# # 랜덤 대기시간
# waitTime = randint(10, 150)
# print(f'random waitTime: {waitTime}')
# time.sleep(waitTime)

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# driver = webdriver.Chrome()   # 옵션을 적용하지 않는 경우

driver.get("https://hcs.eduro.go.kr/#/loginHome")

# 1. [자가진단 참여하기 GO] 버튼 클릭
driver.find_element(By.ID, "btnConfirm2").click()

#region 2. 학교 정보 입력
# 학교 입력창 선택
driver.find_element(By.ID, "schul_name_input").click()

# 시/도에서 '광주광역시' 선택하기
driver.implicitly_wait(0.5)
time.sleep(1)
select_object = Select(driver.find_element(By.ID,'sidolabel'))
select_object.select_by_value('05')

# 학교급에서 '고등학교' 선택하기
driver.implicitly_wait(0.5)
select_object = Select(driver.find_element(By.ID,'crseScCode'))
select_object.select_by_value('4')

# 학교명 입력하기
driver.implicitly_wait(0.5)
driver.find_element(By.ID,'orgname').send_keys("광주과학고" + Keys.ENTER)

# 학교명 클릭
driver.implicitly_wait(0.5)
driver.find_element(By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a').click()

# [학교선택/Select School] 버튼 클릭
driver.implicitly_wait(0.5)
driver.find_element(By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
#endregion

#region 3. 성명 및 생년월일 입력
# 성명 입력
driver.implicitly_wait(0.5)
driver.find_element(By.ID, 'user_name_input').send_keys("이동윤" + Keys.ENTER)

# 생년월일 입력
driver.implicitly_wait(0.5)
driver.find_element(By.ID, 'birthday_input').send_keys("790204" + Keys.ENTER)
#endregion

#region 4. 가상키보드 비번 입력
# 가상키보드 아이콘 클릭
driver.implicitly_wait(1)
imgBtn = driver.find_element(By.XPATH, '//*[@id="WriteInfoForm"]/table/tbody/tr/td/div/button/img')
ActionChains(driver).move_to_element(imgBtn).click().perform()  # imgBtn 위로 마우스 이동

# 가상키보드 숫자 선택
# print(driver.find_element(By.ID, 'password_mainDiv').find_element(By.CSS_SELECTOR, ''))
# v_num = driver.find_element(By.XPATH, '//*[@id="password_mainDiv"]/div[4]/a')
# print("aria-label = ", v_num.get_attribute('aria-label'))

nums = ['[4]/a','[5]/a[1]','[5]/a[2]','[5]/a[3]','[5]/a[4]','[6]/a','[7]/a','[8]/a[1]','[8]/a[2]','[8]/a[3]','[8]/a[4]','[9]/a']
v_object = []

for i in nums:
    obj = driver.find_element(By.XPATH, '//*[@id="password_mainDiv"]/div'+i)
    if obj.get_attribute('aria-label'):
        v_object.append(obj)
        print(obj.get_attribute('aria-label'), end=' ')

print('\n비밀번호 요소 리스트에 저장 성공')
print('v_object length: ', len(v_object))
print('클릭: ')
for i in '0509':
    for obj in v_object:
        v_num_value = obj.get_attribute('aria-label')
        if v_num_value == i:
            print(v_num_value, end=' ')
            obj.click()
            driver.implicitly_wait(1)
            break
        
# 확인 버튼 클릭
print('가상 패스워드 입력 성공')
driver.find_element(By.ID, 'btnConfirm').click() 
#endregion

#region 5. 자가진담 참여 및 질문지 체크
# 자가진단 참여버튼 클릭
time.sleep(5)
driver.implicitly_wait(1)
driver.find_element(By.XPATH, '//*[@id="container"]/div/section[2]/div[2]/ul/li/a/em').click()
    
# 자가진단 질문지 체크
time.sleep(0.5)
driver.find_element(By.ID, 'survey_q1a1').click()
driver.find_element(By.ID, 'survey_q2a1').click()  # survey_q2a1
driver.find_element(By.ID, 'survey_q3a1').click()
driver.find_element(By.ID, 'btnConfirm').click()
#endregion

#region 6. 브라우저 종료  
print('*** 자가진단 셀프 체크 프로그램 종료 ***') 
time.sleep(2)
driver.quit()
#endregion