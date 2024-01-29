import os, sys, time, csv, requests, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#옵션설정
options = Options()
    #최대 화면 조건
options.add_argument('--start-maximized')
    #화면 꺼짐 방지 조건
options.add_experimental_option("detach",True)
    #불필요한 에러메시지 제거 조건
options.add_experimental_option("excludeSwitches",["enable-logging"])


browser = webdriver.Chrome(options=options)
#크롤링 차단되었을 때
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})

#사이트 연결
browser.get('https://search.shopping.naver.com/book/home')
browser.page_source
time.sleep(2)
for i in range(10):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1/2)

#카테고리
    #카테고리 마저도 자동화 가능
elem = browser.find_element(By.CLASS_NAME, 'category_list_category__DqGyx')
categorylist = elem.text.split('\n')
print(categorylist)
print('W'*60)
print('원하는 카테고리를 위의 카테고리 종류를 참조하여 입력해주세요(복사붙여넣기)')
inputCategory = input()
xpathIdx = int(categorylist.index(inputCategory))+1
print('xpathIdx===>', xpathIdx)
xpath = '//*[@id="container"]/div/div[11]/div/ul/li[{}]/a'.format(xpathIdx)
print('xpath====>', xpath)
    #elem 덮어쓰기
elem = browser.find_element(By.XPATH, xpath)
elem.click()
time.sleep(2)

#제목, 가격, 연도, 등수 추출
    #엑셀에 컬럼입력하기
colList = '제목, 가격, 연도, 등수'.split(', ')
print(colList)
    #자료개수와 페이지 수
print('='*50,'원하는 데이터의 갯수를 입력해주세요', '='*50)
dataNum = int(input())
endPage = math.ceil(dataNum/40)
print('endPage ====>', endPage)
curUrl = browser.current_url
print(curUrl)
    #연결테스트
    #자료가져오기