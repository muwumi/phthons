from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import re
import time


#옵션 설정
options = Options()

    #화면 크기와 위치
options.add_argument("--window-size=1000,800")
options.add_argument("--window-position=800,0")

    #화면 꺼짐 방지 조건
options.add_experimental_option("detach", True)

    #불필요한 에러메세지 제거 조건
options.add_experimental_option("excludeSwitches", ["enable-logging"])

#드라이버
    #크롬에 드라이버 세팅
driver = webdriver.Chrome(options=options)

    #드라이버에서 주소세팅 후 접속
driver.get('https://www.opinet.co.kr/')

#오피넷에서 동작
    #경남 선택하기(기다려주는 장치 삽입 후 성공)
elem = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SIDO09_AVG_P"]'))
)
actionFoce = webdriver.ActionChains(driver)
actionFoce.move_to_element(elem).click().perform()
time.sleep(2)

    #함안군 선택
        #셀렉트 박스 찾아들어가기
selectBoxCity = driver.find_element(By.XPATH, '//*[@id="selected1"]')
selectCity = Select(selectBoxCity)
        #셀렉트에서 함안군 선택
selectCity.select_by_visible_text('함안군')
        #셀렉트에서 저가순
selectBoxPrice = driver.find_element(By.XPATH, '//*[@id="selected2"]')
selectPrice = Select(selectBoxPrice)
selectPrice.select_by_visible_text('저가순')
time.sleep(1)

    #top5 데이터 긁어오기
tbody = driver.find_element(By.XPATH, '//*[@id="os_t1"]/tbody')
cheap5tag = tbody.find_elements(By.TAG_NAME, 'a')
cheap5List = []
for cheap5 in cheap5tag:
    cheap5TXT = cheap5.get_attribute('text')
    cheap5List.append(cheap5TXT)

    #하위 first 선택
first = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="os_t1"]/tbody/tr[1]/td[2]/a'))
)
actionFoce = webdriver.ActionChains(driver)
actionFoce.move_to_element(first).click().perform()
time.sleep(1)

print('VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV 여기까지 성공!!!')

    #보통휘발유, 지역평균 가격(휘,경)+상위5개(휘,경) 데이터 가져오기
detailBox = driver.find_element(By.XPATH, '//*[@id="os_price1"]')
stationNameS = detailBox.find_elements(By.TAG_NAME, 'a')
priceS = detailBox.find_elements(By.CLASS_NAME, 'price')
time.sleep(1)
print('===========================================================')
nameList = []
for name in stationNameS:
    nameTxt = name.get_attribute('textContent').strip()
    nameTxt = ' '.join(nameTxt.split())
    nameList.append(nameTxt)
    if len(nameList) == 5:
        break
print(nameList)
time.sleep(1)
print('VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
priceList = []
for price in priceS:
    priceVal = price.get_attribute('textContent').strip()
    priceList.append(priceVal)
    if (len(priceList)/2) == 5:
        break
print(priceList)
time.sleep(1)
print('VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
dataDict = {}
for i in range(len(nameList)):
    key = nameList[i]
    priceList2P = []
    priceList2P.append(priceList[i])
    priceList2P.append(priceList[2*i])
    print(key)
    dataDict[key]= priceList2P
print(dataDict)
print('VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV 여기까지 성공!!!')

#엑셀에서 저장
    #엑셀 오픈
xcPath = r'C:\Users\user\Desktop\pyTest.xlsx'
workbook = openpyxl.load_workbook(xcPath)
sheet = workbook['Sheet1']

    #입력하기
#sheet['A1'] = dataDict.keys[1]
keys = list(dataDict.keys())
values = list( dataDict.values())
type = type(values)

print(type)
print(values)
