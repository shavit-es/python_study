from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

# def downImage(img_url, img_name):
#     dir = 'C:/Users/shavi/Desktop/CodingResult/crawling/selenium/images/'
#     urllib.request.urlretrieve(img_url, dir + img_name +'/'+ img_name + '.jpg')

driver = webdriver.Chrome(r'#chromedriver위치')
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
search_list = ["#검색어목록"]
for search_element in search_list:
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys(search_element)
    elem.send_keys(Keys.RETURN)
    #스크롤해서 더 많은 이미지 불러오기
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight") 
    #자바스크립트 코드를 실행하는 코드(브라우저의 높이를 찾아서 받아옴)
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #브라우저 끝까지 스크롤을 내리겠다
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height
    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    i=1
    for image in images[:200]:
        try:
            image.click()
            time.sleep(3)
            # image_url = driver.find_element_by_css_selector('.n3VNCb').get_attribute("src")
            image_url = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img').get_attribute('src')
            image_dir = 'C:/Users/shavi/Desktop/CodingResult/crawling/selenium/images/'+search_element+'/' #저장위치
            if not os.path.exists(image_dir):
                os.makedirs(image_dir)
            urllib.request.urlretrieve(image_url, image_dir + search_element+ str(i) +'.jpg')
            i=i+1
        except:
            pass

driver.close()
