import os, sys, time, csv, requests, math, pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

#옵션설정
options = Options()
    #최대 화면 조건
options.add_argument('--start-maximized')
    #자동화 인식을 무력화 하기 위한 수단
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    #화면 꺼짐 방지 조건
options.add_experimental_option("detach",True)
    #불필요한 에러메시지 제거 조건
options.add_experimental_option("excludeSwitches",["enable-logging"])


browser = webdriver.Chrome(options=options)
#크롤링 차단되었을 때
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})


#이메일 보내기
    #네이버에 접속
browser.get('https://www.naver.com/')
browser.page_source
time.sleep(1)

    #로그인
elem = browser.find_element(By.CSS_SELECTOR, '.MyView-module__link_login___HpHMW')
time.sleep(1/2)
elem.click()
time.sleep(3/2)
        #아이디 비번 입력
print('아이디 입력')
my_id = input()
print('비번 입력')
my_pwd = input()
pyperclip.copy(my_id)
browser.find_element(By.ID,'id').send_keys('xcv')
browser.find_element(By.ID, 'id').send_keys(Keys.BACKSPACE)
time.sleep(1)
browser.find_element(By.ID, 'id').send_keys(Keys.BACKSPACE)
time.sleep(1/2)
browser.find_element(By.ID, 'id').send_keys(Keys.BACKSPACE)
time.sleep(3/2)
browser.find_element(By.ID,'id').send_keys(Keys.CONTROL,'v')
pyperclip.copy(my_pwd)
time.sleep(2)
browser.find_element(By.ID,'pw').send_keys(Keys.CONTROL,'v')
browser.find_element(By.ID,'log.login').click()

    #메일보내기 페이지
    #첨부파일
