from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()    
driver.get("https://hcs.eduro.go.kr/#/loginHome") 

def find_id(elem):
    time.sleep(1)
    driver.find_element_by_id(elem).click()

find_id('btnConfirm2')
find_id('schul_name_input')

# 시/도 목록에서 '광주광역시' 선택
# ID가있는 드롭 다운 요소를 Select 클래스 객채로 만든다.abs(n)
select = Select(driver.find_element_by_id('sidolabel'))
select.select_by_visible_text('광주광역시')

# 학교급
select = Select(driver.find_element_by_id('crseScCode'))
select.select_by_visible_text('고등학교')

# 학교명
school = driver.find_element_by_id('orgname')
school.click()
school.send_keys('광주과학고등학교')
school.send_keys(Keys.RETURN)

# 학교선택 버튼 클릭
time.sleep(1)
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a/em').click()
time.sleep(1)
driver.find_element_by_class_name('layerFullBtn').click()

# 성명 입력
user_name = driver.find_element_by_id('user_name_input')
user_name.click()
user_name.send_keys("이동윤")
user_name.send_keys(Keys.RETURN)

# 생년월일 입력
user_name = driver.find_element_by_id('birthday_input')
user_name.click()
user_name.send_keys("790204")
user_name.send_keys(Keys.RETURN)
time.sleep(1)
driver.find_element_by_class_name('btnConfirm').click()

# 비밀번호 입력
find_id('password')
time.sleep(1)
pwd = driver.find_element_by_xpath('//*[@id="password"]')
pwd.click()
time.sleep(1)
pw_numbers = driver.find_elements_by_class_name('transkey_div_3_2')

for i in pw_numbers:
    print(i.get_attribute("aria-label"))

# elem = driver.find_element_by_name("q")
# elem.send_keys("iu")
# elem.send_keys(Keys.RETURN)

# SCROLL_PAUSE_TIME = 1

# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         try:
#             driver.find_element_by_css_selector('.mye4qd').click()
#         except:
#             break
#     last_height = new_height

# images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
# img_number = 1
    
# for image in images:
#     try:
#         image.click()
#         time.sleep(2)
#         image_url = driver.find_element_by_css_selector("#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.qdnLaf.isv-id > div > a > img").get_attribute("src")
#         r = requests.get(image_url)
#         image_name = f'./download_images/img{img_number}.jpg'
#         with open(image_name, 'wb') as f:
#             f.write(r.content)
#         img_number += 1
#     except Exception as e:
#         print('에러 발생', e)

time.sleep(3)
driver.close()