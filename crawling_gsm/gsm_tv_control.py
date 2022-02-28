from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

options = webdriver.ChromeOptions()
# options.add_argument('headless')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
url_list = ["http://10.122.2.80:1011/", "http://10.122.2.80:1012/", "http://10.122.2.80:1014/", "http://10.122.2.80:1015/"]

def turn_on_tvs():
    for i in range(4):
        # tv 상태 페이지 소스 페이지 가져오기 & 파싱
        driver.get(url_list[i])

        # 버튼 객체 연결 및 TV Status 버튼 클릭
        btn_status = driver.find_element_by_name('btn1')
        btn_power = driver.find_element_by_name('btn2')
        print('btn_status ', btn_status)
        print('btn_power ', btn_power)

        # tv 상태버튼 클릭
        time.sleep(1)
        btn_status.click()
        time.sleep(3)

        # tv 전압값 저장 
        soup = BeautifulSoup(driver.page_source, 'lxml')
        tv_status = soup.find_all('h4')
        tv_voltage = int(re.sub(r'[^0-9]', '', tv_status[1].get_text()))  # 문자열에서 숫자가 아닌 문자를 모두 제거하고 숫자로 구성된 문자열
        print(f'{i+1}번 tv 전압: ', tv_voltage)

        # tv가 꺼져있는지 확인하고 켜기
        if tv_voltage < 200:
            print(f'{i+1}번 TV 켜기')
            btn_power.click()
            time.sleep(3)
            
def turn_off_tvs():
    for i in range(4):
        # tv 상태 페이지 소스 페이지 가져오기 & 파싱
        driver.get(url_list[i])

        # 버튼 객체 연결 및 TV Status 버튼 클릭
        btn_status = driver.find_element_by_name('btn1')
        btn_power = driver.find_element_by_name('btn2')

        # tv 상태버튼 클릭
        btn_status.click()
        time.sleep(1)

        # tv 전압값 저장 
        soup = BeautifulSoup(driver.page_source, 'lxml')
        tv_status = soup.find_all('h4')
        tv_voltage = int(re.sub(r'[^0-9]', '', tv_status[1].get_text()))  # 문자열에서 숫자가 아닌 문자를 모두 제거하고 숫자로 구성된 문자열
        print(f'{i+1}번 tv 전압: ', tv_voltage)

        # tv가 꺼져있는지 확인하고 켜기
        if tv_voltage > 100:
            print(f'{i+1}번 TV 끄기')
            btn_power.click()
            
def check_tvIsOn():
    count = 0
    for i in range(4):
        driver.get(url_list[i])
        btn_status = driver.find_element_by_name('btn1')
        btn_status.click()
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        tv_status = soup.find_all('h4')
        tv_voltage = int(re.sub(r'[^0-9]', '', tv_status[1].get_text()))
        print(f'{i+1}번 tv 전압: ', tv_voltage)
        if tv_voltage > 200:
            print(f'{i+1}번 tv 켜져있음')
            count += 1
        else:
            print(f'{i+1}번 tv 꺼져있음')
    return count

# 급식실의 모든 TV 켜기
while True:
    turn_on_tvs()        # 1. TV가 꺼져있으면 켜기
    
    # 2. TV가 모두 켜져있는지 확인 => TV가 모두 켜져있으면 프로그램 종료
    if check_tvIsOn() == 4:
        break

print("프로그램 종료")
# driver.quit()