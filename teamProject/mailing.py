from io import BytesIO
import math
import os
import time
import csv
import requests
import pyperclip
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook, load_workbook
from openpyxl.drawing.image import Image
import numpy as np
import matplotlib.font_manager as fm
import statsmodels.api as sm

# 이메일 보내기
def send_email(excel_file_name_with_graph):
    browser.get('https://www.naver.com/')
    browser.page_source
    time.sleep(1)

    elem = browser.find_element(By.CSS_SELECTOR, '.MyView-module__link_login___HpHMW')
    time.sleep(1/2)
    elem.click()
    time.sleep(3/2)

    print('아이디 입력')
    my_id = 'tkdgjs9528'  # input()으로 변경
    print('비번 입력')
    my_pwd = 'Nhalfturn0*'  # input()으로 변경
    pyperclip.copy(my_id)
    browser.find_element(By.ID, 'id').send_keys('xcv')
    browser.find_element(By.ID, 'id').send_keys(Keys.BACKSPACE)
    time.sleep(1)
    browser.find_element(By.ID, 'id').send_keys(Keys.BACKSPACE)
    time.sleep(1/2)
    browser.find_element(By.ID, 'id').send_keys(Keys.BACKSPACE)
    time.sleep(3/2)
    browser.find_element(By.ID, 'id').send_keys(Keys.CONTROL, 'v')
    pyperclip.copy(my_pwd)
    time.sleep(2)
    browser.find_element(By.ID, 'pw').send_keys(Keys.CONTROL, 'v')
    browser.find_element(By.ID, 'log.login').click()
    cur_url = browser.current_url
    if cur_url == 'https://www.naver.com/':
        print('cur_url=========>', cur_url)
        print('=====================로그인이 되었습니다======================')

    browser.get('https://mail.naver.com/')
    cur_url = browser.current_url
    if cur_url == 'https://mail.naver.com/':
        print('cur_url=========>', cur_url)
        print('=====================메일 보내기 창으로 갔습니다======================')
        time.sleep(3/2)

    write_btn = browser.find_element(By.XPATH, '//*[@id="root"]/div/nav/div/div[1]/div[2]/a[1]')
    write_btn.click()
    time.sleep(2)
    print('================메일쓰기 버튼 눌렀음================')

    recip_adr = 'tkdgjs9528@naver.com'  # input으로 대체 가능
    recip_input_elem = browser.find_element(By.ID, 'recipient_input_element')
    recip_input_elem.click()
    recip_input_elem.send_keys(recip_adr)
    print('='*20, '받는사람', '='*20)

    title = '{} 파일 전송'.format(excel_file_name_with_graph)
    title_input_elem = browser.find_element(By.ID, 'subject_title')
    title_input_elem.click()
    title_input_elem.send_keys(title)
    print('='*20, '제목', '='*20)

    file_input = browser.find_element(By.ID, 'ATTACH_LOCAL_FILE_ELEMENT_ID')
    file_input.send_keys(os.path.abspath(base_path+excel_file_name_with_graph))

    wait = WebDriverWait(browser, 10)
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'file_upload_progress')))
    print('='*20, '첨부파일', '='*20)

    browser.find_element(By.CLASS_NAME, 'button_write_task').click()
    print('='*20, '전송하기', '='*20)

    return True