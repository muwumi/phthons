import os, sys, time, csv, requests, math
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

#스크롤 끝까지 내리기
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
getUrlExcPage = elem.get_attribute('href')
print('================>', getUrlExcPage, type(getUrlExcPage))
# print('getUrl =======>', getUrl)
# print(type(getUrl))
#그냥 클릭하면 새로운 탭으로 연결됨. 이는 브라우저의 url을 변동시키지 못함.
browser.execute_script('''
    var elements = document.querySelectorAll(".category_link_category__XlcyC");
    elements.forEach(function(element) {
        element.setAttribute("target", "_self");
    });
''')
time.sleep(2)
elem.click()
time.sleep(2)
browser.refresh()
time.sleep(1)
print('W'*100) 
# 스크롤 끝까지 내리기
print('===================================browser===================================')
print(browser, type(browser))
print('현재url', browser.current_url)
print('잠시 대기')
for i in range(10):
    # 대기 시간 추가
    time.sleep(1/4)
    
    # 스크롤 명령을 WebDriverWait로 감싸기, end키를 활용하여 body태그가 나올 때까지 기다리기
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body'))).send_keys(Keys.END)



#제목, 가격, 연도, 등수 추출
    #자료개수와 페이지 수
dataResult2D = []
print('='*50,'원하는 데이터의 갯수를 입력해주세요', '='*50)
dataNum = int(input())
endPage = math.ceil(dataNum/40)
    #엑셀열기
f = open(('{}{}개.csv'.format(inputCategory, dataNum)), 'w', encoding='UTF-8-sig', newline='')
writer = csv.writer(f, delimiter=',')
    #엑셀에 컬럼입력하기
colList = '제목, 가격, 연도, 등수'.split(', ')
writer.writerow(colList)

    #1-endpage 반복
for i in range(1, endPage+1):
            #연결테스트
    getUrl = getUrlExcPage+'&pageIndex={}&pageSize=40'.format(i)
    userAgent = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    resData = requests.get(getUrl, headers=userAgent)
    if resData.status_code == requests.codes.OK :
        print('page{} 접속URL=====>[  {}  ]에 접속완료 '.format(i, getUrl))
    else :
        print('권한이 없어 접속에 실패하였습니다.')
            
            #데이터 가져오기
    for j in range (1, 40+1):
        print('============@@@@@@@=====>>>>>>>>{}번째'.format(j))
        elem = browser.find_element(By.XPATH, '//*[@id="book_list"]/ul/li[{}]'.format(j))
        title = elem.find_elements(By.CSS_SELECTOR, '.bookListItem_title__X7f9_')
        price = elem.find_elements(By.CSS_SELECTOR, '.bookPrice_price__zr5dh>em')
        date = elem.find_elements(By.CLASS_NAME, 'bookListItem_detail_date___byvG')
        rank = elem.find_elements(By.CSS_SELECTOR, '.bookListItem_feature__txTlp')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@'*6)
        dataList1D = []
        if(len(dataResult2D)<dataNum):
            dataList1D.append(title[0].text)
            dataList1D.append(price[0].text)
            dataList1D.append(date[0].text)
            dataList1D.append(rank[0].text)
            dataResult2D.append(dataList1D)
            writer.writerow(dataResult2D[int(j)-1])
            print('dataList ===>', dataList1D)
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',len(dataResult2D), dataNum )
        else :
            break
        
    #다음 페이지로 넘어가기
    nexUrl = getUrl = getUrlExcPage+'&pageIndex={}&pageSize=40'.format(i+1)
    browser.get(getUrl)
    #스크롤 내리기
    for k in range(10):
    # 대기 시간 추가
        time.sleep(1/4)
        # 스크롤 명령을 WebDriverWait로 감싸기, end키를 활용하여 body태그가 나올 때까지 기다리기
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body'))).send_keys(Keys.END)