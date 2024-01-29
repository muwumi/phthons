from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


import time, csv


options = Options()
#최대 화면 조건
options.add_argument('--start-maximized')
#화면 꺼짐 방지 조건
options.add_experimental_option("detach",True)
#불필요한 에러메시지 제거 조건
options.add_experimental_option("excludeSwitches",["enable-logging"])
#wb는 webdriver

browser = webdriver.Chrome(options=options)
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})
#쿠팡 크롤링 차단되었을 때
browser.get("https://www.coupang.com/")
browser.page_source
elem = browser.find_element(By.ID,f'headerSearchKeyword')
time.sleep(3)
#검색
print('검색어를 입력하세요')
keyword = input()
elem.send_keys(keyword)
elem = browser.find_element(By.CSS_SELECTOR,'#headerSearchBtn')
elem.click()
time.sleep(3)
#정렬
elem = browser.find_element(By.XPATH, '//*[@id="searchSortingOrder"]/ul/li[2]/label')
elem.click()
time.sleep(5)

#항목번호
itemList = []
elems = browser.find_elements(By.CLASS_NAME, 'search-product ')
print('=======================================================')
for elem in elems:
    if len(itemList)==10:
        break
    value = elem.get_attribute('id')
    itemList.append(value)
    print(value)

#아이템 이름
print('========================top10List===========================')
top10itemList = []
for i in range(len(itemList)):
    id = itemList[i]
    getXpath = '//*[@id="{}"]/a/dl/dd/div/div[2]'.format(id)
    elem = browser.find_element(By.XPATH, getXpath)
    top10itemList.append(elem.text)
print(top10itemList)

#아이템 가격
print('========================top10List===========================')
top10priceList = []
for i in range(len(itemList)):
    id = itemList[i]
    getXpath = '//*[@id="{}"]/a/dl/dd/div/div[3]/div/div[1]/em/strong'.format(id)
    elem = browser.find_element(By.XPATH, getXpath)
    top10priceList.append(elem.text)
print(top10priceList)

#아이템 도착
print('========================top10List===========================')
top10arriveList = []
for i in range(len(itemList)):
    id = itemList[i]
    getXpath = '//*[@id="{}"]/a/dl/dd/div/div[3]/div/div[2]/span'.format(id)
    elem = browser.find_element(By.XPATH, getXpath)
    top10arriveList.append(elem.text)
print(top10arriveList)

#2차원 배열에 매칭시키기
top10_2D = []
for i in range(len(itemList)):
    top10 = []
    key = top10itemList[i]
    price = top10priceList[i]+'원'
    arrive = top10arriveList[i]
    top10.append(key)
    top10.append(price)
    top10.append(arrive)
    top10_2D.append(top10)
print(top10_2D)

#파일 저장 시스템
print('>>>>>>>>>>>>>>>>>>>>>>>>파일로 저장하시겠습니까? (예/아니오)')
answer = input()
if answer == '예':
    fileName = '{}.csv'.format(keyword)
    f = open(fileName, 'w', encoding='UTF-8-sig', newline='')
    writer = csv.writer(f, delimiter=',')
    titleList = ['item', 'price', '도착예정']
    for i in range(len(itemList)):
        if i == 0:
            writer.writerow(titleList)
        writer.writerow(top10_2D[i])
    print('저장이 완료되었습니다.')
elif answer == '아니오':
    print('아니오를 선택하셔서 그대로 종료합니다.')
else :
    print('입력이 올바르지 않아 그대로 종료합니다. 원하신다면 다시 실행해 주세요')
