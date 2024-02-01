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
