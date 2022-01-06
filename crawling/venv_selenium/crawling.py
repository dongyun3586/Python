from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import urllib.request

driver = webdriver.Chrome()    
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl") 

elem = driver.find_element_by_name("q")
elem.send_keys("iu")
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector('.mye4qd').click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
img_number = 1
    
for image in images:
    try:
        image.click()
        time.sleep(2)
        image_url = driver.find_element_by_css_selector("#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.qdnLaf.isv-id > div > a > img").get_attribute("src")
        r = requests.get(image_url)
        image_name = f'./download_images/img{img_number}.jpg'
        with open(image_name, 'wb') as f:
            f.write(r.content)
        img_number += 1
    except Exception as e:
        print('에러 발생', e)

driver.close()