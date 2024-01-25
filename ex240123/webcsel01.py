from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

browser = webdriver.Chrome()
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})
browser.get("https://www.coupang.com/")
browser.page_source
elem = browser.find_element(By.ID, 'headerSearchKeyword')
time.sleep(2)
elem.send_keys("고구마")
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '#headerSearchBtn').click() #elem.send_keys(Keys.ENTER)

#10번라인부터 14번라인까지 하나의 명령으로 만듬(동작하지 않을 수도 있다.네트워크 상황이나 속도문제 등)
#browser.find_element(By.ID, 'headerSearchKeyword').send_keys("고구마").send_keys(Keys.ENTER)
time.sleep(2)
browser.find_element(By.XPATH,'//*[@id="searchSortingOrder"]/ul/li[2]/label').click() #싼 가격순으로 정렬

#여기까지가 자료를 얻고자 하는 페이지가 된다.
# 현재 페이지에서 데이터 추출이 완료된다면
#1. beautifulsoup을이용  <= browser.page_source
#2.  browser.get을 새롭게 현재 url을 가져오는 방법

titles = []
prices = []
ar_dates = []
# 반복문이 들어간다.n페이지만큼 
url = 'https://www.coupang.com/np/search?q=%EA%B3%A0%EA%B5%AC%EB%A7%88&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=salePriceAsc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor='

browser.get(url)
elems = browser.find_elements(By.CSS_SELECTOR, '.search-product .name')
for (index, elem) in enumerate(elems):
    if index >= 12:
        break
    titles.append(elem.text)

elems = browser.find_elements(By.CSS_SELECTOR, '.search-product .price-value')
for index, elem in enumerate(elems):
    if index >= 12:
        break
    prices.append(elem.text)

elems = browser.find_elements(By.CSS_SELECTOR, '.search-product .arrival-info')
for index, elem in enumerate(elems):
    if index >= 12:
        break
    ar_dates.append(elem.text)

print(titles , "\n" , prices, "\n", ar_dates)