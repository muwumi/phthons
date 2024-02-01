import os, sys, time, csv, requests, math, pyperclip, pandas, seaborn, matplotlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas, os, sys, seaborn, matplotlib, csv, numpy
import matplotlib.pyplot as plt


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

#사이트 연결
browser.get('https://search.shopping.naver.com/book/home')
browser.page_source
time.sleep(1)


#스크롤 끝까지 내리기
def scrollDownMax():
    last_height = browser.execute_script("return document.documentElement.scrollHeight")
    while True :
        #스크롤 끝까지 내리기
        browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        print("Scrolled!")
        #스크롤 내린 후 페이지 로딩 시간 필요
        time.sleep(1)

        #스크롤 내린 후 페이지 높이
        new_height = browser.execute_script("return document.documentElement.scrollHeight")
        
        #더이상 스크롤이 내려가지 않을 때 까지 스크롤 내리는 반복문 멈추기
        if new_height == last_height :
            break
        #스크롤 내린 후 페이지 높이를 현재 페이지 높이 변수에 저장
        last_height = new_height
scrollDownMax()

#카테고리
    #카테고리 마저도 자동화 가능
elem = browser.find_element(By.CLASS_NAME, 'category_list_category__DqGyx')
categorylist = elem.text.split('\n')
print('_'*30,'이하 카테고리 목럭입니다.', '_'*30)
print(categorylist)
print('_'*80)
print('원하는 카테고리를 <<위의 카테고리 종류>>를 참조하여 입력해주세요(복사붙여넣기)')
inputCategory = input()
div = browser.find_elements(By.CLASS_NAME, 'bookCard_card_wrap__Tx4e0')
divIdx = int(len(div))
print('보세요~~~~~~~~~~~divIdx ==================>', divIdx)
xpathIdx = int(categorylist.index(inputCategory))+1
print('xpathIdx===>', xpathIdx)
xpath = '//*[@id="container"]/div/div[{}]/div/ul/li[{}]/a'.format(divIdx, xpathIdx)
print('xpath====>', xpath)
    #elem 덮어쓰기
time.sleep(1)
wait = WebDriverWait(browser, 20)
elem = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
#elem = browser.find_element(By.XPATH, xpath)
time.sleep(3/2)
getUrlExcPage = elem.get_attribute('href')
    #그냥 클릭하면 새로운 탭으로 연결되기 때문에 href 속성 값을 전부 변경 시킴
browser.execute_script('''
    var elements = document.querySelectorAll(".category_link_category__XlcyC");
    elements.forEach(function(element) {
        element.setAttribute("target", "_self");
    });
''')
time.sleep(1)
elem.click()
time.sleep(1)
    #클릭 이후에 기존 탭에서 카테고리 창이 열렸는지 확인
print('===================================browser===================================')
print('현재url : ', browser.current_url)
print('잠시 대기')
scrollDownMax()

#제목, 가격, 연도, 등수 추출
    #자료개수와 페이지 수
dataResult2D = []#최종적으로 사용할 데이터 그릇(2차원 배열)
print('='*50,'원하는 데이터의 갯수를 입력해주세요', '='*50)
dataNum = int(input())
endPage = math.ceil(dataNum/40)
    #엑셀열기
    # 슬래쉬를 경로로 인식하는 문제를 해결하기 위해 r과 replace함수 사용
fPath = r'D:\LSH\workspace\phthons\teamProject'
fName = r'\{}{}개.csv'.format(inputCategory, dataNum).replace('/', '')
f = open(fPath+fName, 'w', encoding='UTF-8-sig', newline='')
writer = csv.writer(f, delimiter=',')
    #엑셀에 컬럼입력하기
colList = '제목, 가격, e북가격, 연도, 등수'.split(', ')
writer.writerow(colList)

    #1-endpage 반복
for i in range(1, endPage+1):
            #연결테스트
    getUrl = getUrlExcPage+'&pageIndex={}&pageSize=40'.format(i)
    userAgent = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    resData = requests.get(getUrl, headers=userAgent)
    if resData.status_code == requests.codes.OK :
        print('{}page 접속URL=====>[  {}  ]에 접속완료 '.format(i, getUrl))
    else :
        print('권한이 없어 접속에 실패하였습니다.')
            
            #데이터 가져오기(pagesize는 변경 불가 : 40)
    for j in range (1, 40+1):
        elem = browser.find_element(By.XPATH, '//*[@id="book_list"]/ul/li[{}]'.format(j))
        title = elem.find_elements(By.CSS_SELECTOR, '.bookListItem_title__X7f9_')
        price = elem.find_elements(By.CSS_SELECTOR, '.bookPrice_price__zr5dh>em')
        ePrice = elem.find_elements(By.CSS_SELECTOR, '.bookListItem_sub_info__AfkOO em')
        date = elem.find_elements(By.CLASS_NAME, 'bookListItem_detail_date___byvG')
        rank = elem.find_elements(By.CSS_SELECTOR, '.bookListItem_feature__txTlp')
        print('________________'*10)
        dataList1D = []#2D그릇에 넣을 1D 데이터, 매번 초기화해야 하기 때문에 for문 안에 넣기
        if(len(dataResult2D)<dataNum): #'='을 넣으면 마지막에 하나더 삽입 됨
            dataList1D.append(title[0].text)
            dataList1D.append(price[0].text.replace(',', ''))
            if(len(ePrice)==2):
                dataList1D.append(ePrice[1].text.replace(',', ''))
            else :
                dataList1D.append(' ') 
            dataList1D.append(date[0].text)
            if (len(rank)!=0):
                dataList1D.append(rank[0].text)
            else :
                dataList1D.append(' ')            
            dataResult2D.append(dataList1D)
            writer.writerow(dataResult2D[int(j)-1])
            print('dataList ===>', dataList1D)
            print('>>>>>>>삽입한 개수 {}>>>>>>목표 개수 {}>>>>>>>'.format(len(dataResult2D), dataNum) )                
        else :
            print('--------------입력이 완료되었습니다.----------------')
            break
        
    #다음 페이지로 넘어가기
    nexUrl = getUrl = getUrlExcPage+'&pageIndex={}&pageSize=40'.format(i+1)
    browser.get(getUrl)
    #스크롤 내리기
    scrollDownMax()

#파일 저장
f.close()
print('='*30, 'csv파일 저장', '='*30)

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
myId = 'tkdgjs9528' #input()으로 변경
print('비번 입력')
myPwd = 'Nhalfturn0*' #input()으로 변경
pyperclip.copy(myId)
browser.find_element(By.ID,'id').send_keys('xcv')
browser.find_element(By.ID, 'id').send_keys(Keys.BACKSPACE)
time.sleep(1)
browser.find_element(By.ID, 'id').send_keys(Keys.BACKSPACE)
time.sleep(1/2)
browser.find_element(By.ID, 'id').send_keys(Keys.BACKSPACE)
time.sleep(3/2)
browser.find_element(By.ID,'id').send_keys(Keys.CONTROL,'v')
pyperclip.copy(myPwd)
time.sleep(2)
browser.find_element(By.ID,'pw').send_keys(Keys.CONTROL,'v')
browser.find_element(By.ID,'log.login').click()
curUrl = browser.current_url
if curUrl == 'https://www.naver.com/':
    print('curUrl=========>', curUrl)
    print('=====================로그인이 되었습니다======================')
    #메일보내기 페이지
browser.get('https://mail.naver.com/')
curUrl = browser.current_url
if curUrl == 'https://mail.naver.com/':
    print('curUrl=========>', curUrl)
    print('=====================메일 보내기 창으로 갔습니다======================')
    time.sleep(3/2)
    #새로운 메일 쓰기 버튼 누르기
writeBtn = browser.find_element(By.XPATH, '//*[@id="root"]/div/nav/div/div[1]/div[2]/a[1]')
writeBtn.click()
time.sleep(2)
print('================메일쓰기 버튼 눌렀음================')
    #메일작성
        #받는 사람
recipAdr = 'tkdgjs9528@naver.com' #input으로 대체 가능
recipInputElem = browser.find_element(By.ID, 'recipient_input_element')
recipInputElem.click()
recipInputElem.send_keys(recipAdr)
print('='*20, '받는사람', '='*20)
        #제목
title = '{} 파일 전송'.format(fName)
titleInputElem = browser.find_element(By.ID, 'subject_title')
titleInputElem.click()
titleInputElem.send_keys(title)
print('='*20, '제목', '='*20)
        #첨부파일
            # 파일 업로드
file_input = browser.find_element(By.ID, 'ATTACH_LOCAL_FILE_ELEMENT_ID')
file_input.send_keys(os.path.abspath(fPath+fName))

            # 첨부한 파일이 업로드될 때까지 대기
wait = WebDriverWait(browser, 10)
wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'file_upload_progress')))
print('='*20, '첨부파일', '='*20)
'''
        #내용작성
conInput = '임시로 내용을 작성해 봅니다'
conBox = browser.find_element(By.ID, 'sender_input')
conBox.send_keys(conInput)
time.sleep(2)
print('='*20, '내용', '='*20)
'''
        #전송버튼
browser.find_element(By.CLASS_NAME, 'button_write_task').click()
print('='*20, '전송하기', '='*20)

#csv 읽어오고 데이터 가져오기
    #csv 읽기
csvPath = r'D:\LSH\workspace\phthons\teamProject\{}'.format(fName)
csvDataFrame = pandas.read_csv(csvPath, sep=',', encoding='utf-8-sig')
print(csvDataFrame)
print(type(csvDataFrame))
    #데이터 컨트롤
price = csvDataFrame.loc[0 : , ['가격']]
ePrice = csvDataFrame.loc[0 : , ['e북가격']]
rank = csvDataFrame.loc[0 : , ['등수']]
priceList2D = price.values.tolist()
ePriceList2D = ePrice.values.tolist()
rankList2D = rank.values.tolist()

priceList = []
ePriceList = []
rankList = []
for i in range(len(priceList2D)):
    #e북 가격이 없는 경우 별도로 처리를 해줘야함
    if(ePriceList2D[i][0]!=' '):
        priceList.append(int(priceList2D[i][0]))
        ePriceList.append(int(ePriceList2D[i][0]))
        rankList.append(int(rankList2D[i][0].split(' ')[1].replace('위', '')))
    
print('='*50, 'priceList')
print(priceList)
print('='*50, 'ePriceList')
print(ePriceList)
print('='*50, 'rankList')
print(rankList)

#csv 읽어오고 데이터 가져오기
    #csv 읽기
csvPath = r'D:\LSH\workspace\phthons\teamProject{}'.format(fName)
csvDataFrame = pandas.read_csv(csvPath, sep=',', encoding='utf-8-sig')
print(csvDataFrame)
print(type(csvDataFrame))
    #데이터 컨트롤
bTitle = csvDataFrame.loc[0 : , ['제목']]
price = csvDataFrame.loc[0 : , ['가격']]
ePrice = csvDataFrame.loc[0 : , ['e북가격']]
rank = csvDataFrame.loc[0 : , ['등수']]
bTitleList2D = bTitle.values.tolist()
priceList2D = price.values.tolist()
ePriceList2D = ePrice.values.tolist()
rankList2D = rank.values.tolist()

bTitleList = []
priceList = []
ePriceList = []
rankList = []
for i in range(len(priceList2D)):
    #e북 가격이 없는 경우 별도로 처리를 해줘야함
    if(ePriceList2D[i][0]!=' '):
        bTitleList.append(bTitleList2D[i][0])
        priceList.append(int(priceList2D[i][0].replace(',', '')))
        ePriceList.append(int(ePriceList2D[i][0].replace(',', '')))
        rankList.append(int(rankList2D[i][0].split(' ')[1].replace('위', '')))

print('='*50, 'bTitleList')
print(bTitleList)    
print('='*50, 'priceList')
print(priceList)
print('='*50, 'ePriceList')
print(ePriceList)
print('='*50, 'rankList')
print(rankList)

#그래프 그려보기
    #plt.plot([x값인자], [y값인자])
    #데이터 정렬(가격)

    # x, y 설정
x = priceList
y = rankList
z = ePriceList
rate = []
for i in range(len(priceList)):
    print(i)
    rate.append(round(int(ePriceList[i])/int(priceList[i]), 3)) 
print('=======>rate : {}, {}개'.format(rate, len(rate)))

sortedPriceList = sorted(priceList)
maxX = sortedPriceList[len(priceList)-1]
minX = sortedPriceList[0]
print('=======>priceList : {}, {}'.format(priceList, len(priceList)))
print('=======>epriceList : {}, {}'.format(ePriceList, len(ePriceList)))


# 데이터 생성
categories = []
for i in range(len(priceList)):
    strInput = '[{}] {}'.format(i, priceList[i])
    categories.append(strInput)
print(categories)
plt.scatter(categories, rate, s=5)


# 그래프에 제목과 축 레이블 추가
plt.title('Sum of Paper Price, Ebook Price, and Rank')
plt.xlabel('Categories')
plt.ylabel('Values')

# 그래프 표시
plt.show()
