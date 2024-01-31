import os, sys, time, csv, requests, math, pyperclip, pyautogui
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
recipAdr = 'tkdgjs9528@naver.com'
recipInputElem = browser.find_element(By.ID, 'recipient_input_element')
recipInputElem.click()
recipInputElem.send_keys(recipAdr)
print('='*20, '받는사람', '='*20)
        #제목
title = '타이틀 input'
titleInputElem = browser.find_element(By.ID, 'subject_title')
titleInputElem.click()
titleInputElem.send_keys(title)
print('='*20, '제목', '='*20)
        #첨부파일
            # 엑셀 파일 경로
excel_file_path =  r'D:\LSH\workspace\phthons\teamProject\건강_취미151개.csv'#이부분 나중에 수정
            # 파일 업로드
file_input = browser.find_element(By.ID, 'ATTACH_LOCAL_FILE_ELEMENT_ID')
file_input.send_keys(os.path.abspath(excel_file_path))

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