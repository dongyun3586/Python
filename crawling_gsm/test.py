# 검색창에 원하는 키워드 입력하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()    
driver.get("https://www.dbpia.co.kr/")

elem = driver.find_element_by_id('keyword')
elem.send_keys("인공지능 교육")
elem.send_keys(Keys.RETURN)