import requests
from bs4 import BeautifulSoup
import time
import re

url_list = ["http://10.122.2.80:1011/?sw=", "http://10.122.2.80:1012/?sw=", "http://10.122.2.80:1014/?sw=", "http://10.122.2.80:1015/?sw="]

def turn_off_tvs():
    for i in range(4):
        # tv 상태 페이지 소스 페이지 가져오기 & 파싱
        res = requests.get(url_list[i]+'1')
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'lxml')

        tv_status = soup.find_all('h4')
        tv_voltage = int(re.sub(r'[^0-9]', '', tv_status[1].get_text()))  # 문자열에서 숫자가 아닌 문자를 모두 제거하고 숫자로 구성된 문자열
        print(f'{i+1}번 tv 전압: ', tv_voltage)

        # tv가 꺼져있는지 확인하고 켜기
        if tv_voltage > 200:
                print(f'{i+1}번 TV 끄기')
                requests.get(url_list[i]+'2')
            
def check_tvIsOn():
    count = 0
    for i in range(4):
        time.sleep(3)
        res = requests.get(url_list[i]+'1')
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'lxml')

        tv_status = soup.find_all('h4')
        tv_voltage = int(re.sub(r'[^0-9]', '', tv_status[1].get_text()))  # 문자열에서 숫자가 아닌 문자를 모두 제거하고 숫자로 구성된 문자열
        print(f'{i+1}번 tv 전압: ', tv_voltage)

        # tv가 꺼져있는지 확인하고 켜기
        if tv_voltage < 200:
            print(f'{i+1}번 TV 꺼져있음')
            count += 1
        else:
            print(f'{i+1}번 TV 켜져있음')
            
    return count

while True:
    turn_off_tvs()
    if check_tvIsOn() == 4:
        break