from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from pynput.keyboard import Controller
import pyautogui
import keyboard
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
driver.get('https://www.hira.or.kr/')

#건평원에서 동작
    #비급여 진료비 정보
elem = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="shortcut01"]/ul/li[2]/a'))
)
actionFoce = webdriver.ActionChains(driver)
actionFoce.move_to_element(elem).click().perform()


    #비급여 진료비용 정보
elem = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="uuid-1j"]/a/div'))
)
actionFoce = webdriver.ActionChains(driver)
actionFoce.move_to_element(elem).click().perform()


    #팝업 1
elem = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="uuid-ui"]/div/div/div/div[1]/div'))
)
actionFoce = webdriver.ActionChains(driver)
actionFoce.move_to_element(elem).click().perform()


    #팝업 2
elem = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="uuid-ul"]/div/a'))
)
actionFoce = webdriver.ActionChains(driver)
actionFoce.move_to_element(elem).click().perform()

    #지역
elem = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="uuid-ip"]/div/div[2]'))
)
actionFoce = webdriver.ActionChains(driver)
actionFoce.move_to_element(elem).click().perform()
keyboard.press('enter')
time.sleep(2)
    #시군구
elem = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="uuid-iq"]/div/div[2]'))
)
actionFoce = webdriver.ActionChains(driver)
actionFoce.move_to_element(elem).click().perform()
for i in range(1):
    keyboard.press('down')
keyboard.press('enter')
time.sleep(2)
    #음면동
elem = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="uuid-ir"]/div/div[2]'))
)
actionFoce = webdriver.ActionChains(driver)
actionFoce.move_to_element(elem).click().perform()
for i in range(2):
    keyboard.press('down')
keyboard.press('enter')
time.sleep(2)
    #정형외과
elem = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="uuid-j3"]/div/div[1]/input'))
)
actionFoce = webdriver.ActionChains(driver)
actionFoce.move_to_element(elem).click().perform()
searchBox = driver.find_element(By.XPATH, '//*[@id="uuid-j3"]/div/div[1]/input')
searchBox.send_keys('정형외과')
keyboard.press('enter')
time.sleep(1)
    #도수치료 검색
elem = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="uuid-j6"]/div/div/div[1]/input'))
)
actionFoce = webdriver.ActionChains(driver)
actionFoce.move_to_element(elem).click().perform()
searchBox = driver.find_element(By.XPATH, '//*[@id="uuid-j6"]/div/div/div[1]/input')
searchBox.send_keys('도수치료')
keyboard.press('enter')
time.sleep(3)
print('#################################################도수치료 선택하기##################################################')

    #도수치료 선택
elem = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="uuid-xk"]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div[2]'))
)
actionFoce = webdriver.ActionChains(driver)
actionFoce.move_to_element(elem).click().perform()
time.sleep(1)
print('#################################################도수치료 검색하기##################################################')
    #검색버튼 누르기
elem = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="uuid-xp"]/div/a'))
)
actionFoce = webdriver.ActionChains(driver)
actionFoce.move_to_element(elem).click().perform()
time.sleep(1)

print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
#데이터 가져오기
    #컬럼명 가져오기
i=1
colArr = []
for i in range(6):
    col = driver.find_element(By.XPATH , '//*[@id="uuid-k8"]/div/div/div[3]/div/div[1]/div/div[1]/div/div/div/div['+str(i+1)+']/div[1]/div/div/div/div')
    colName = col.get_attribute('textContent')
    colArr.append(colName)
    print('나오나요???')
    print(colArr)



#엑셀에서 저장
    #엑셀 오픈
xcPath = r'C:\Users\user\Desktop\pyTest.xlsx'
workbook = openpyxl.load_workbook(xcPath)
sheet = workbook['Sheet1']
print('########################################################################')
for i in range(len(colArr)):
    print(i)
    sheet['A'+str(i+1)]=colArr[i]
    print(sheet['A'+str(i+1)].value)
workbook.save(xcPath)
