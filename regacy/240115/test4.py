from selenium import webdriver as wb
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#최대 화면 조건
options = Options()

#화면 꺼짐 방지 조건
options.add_argument('--start-maximized')

#불필요한 에러메세지 제거 조건
options.add_experimental_option("detach", True)

options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = wb.Chrome(options=options)


'''
driver.get("https://cafe.naver.com/joonggonara")

elem = driver.find_element(By.XPATH, '//*[@id="topLayerQueryInput"]')

elem.send_keys('빔프로젝트')
elem.send_keys(Keys.ENTER)
iframe = driver.find_element(By.ID, 'cafe_main')
driver.switch_to.frame(iframe)

elem = driver.find_element("xpath", '//*[@id="main-area"]/div[5]/table/tbody')

print(elem.text, end='')

'''

#네이버 접속
driver.get("https://www.naver.com/")

#검색창 접근
elem = driver.find_element(By.XPATH, '//*[@id="query"]')

#김장훈 검색
elem.send_keys('김장훈')

#엔터 누르기
elem.send_keys(Keys.ENTER)

#프로필 요소 가져오기
profile = driver.find_element(By.XPATH, '//*[@id="main_pack"]/section[1]/div[2]/div[1]/div[2]')

#프로필을 텍스트로 변환하여 출력
print(profile.text)
    



