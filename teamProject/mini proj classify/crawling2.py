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
import scroller
import gspread

#_____________카테고리 자동화 기능_____________
def choose_category(browser = webdriver.Chrome):
    elem = browser.find_element(By.CLASS_NAME, 'category_list_category__DqGyx')
    category_list = elem.text.split('\n')
    print('_' * 30, '이하 카테고리 목럭입니다.', '_' * 30)
    print(category_list)
    print('_' * 80)
    print('원하는 카테고리를 <<위의 카테고리 종류>>를 참조하여 입력해주세요(복사붙여넣기)')
    input_category = input()
    div = browser.find_elements(By.CLASS_NAME, 'bookCard_card_wrap__Tx4e0')
    div_idx = int(len(div))
    print('보세요~~~~~~~~~~~div_idx ==================>', div_idx)
    xpath_idx = int(category_list.index(input_category)) + 1
    print('xpath_idx===>', xpath_idx)
    xpath = '//*[@id="container"]/div/div[{}]/div/ul/li[{}]/a'.format(div_idx, xpath_idx)
    print('xpath====>', xpath)
    # elem 덮어쓰기
    time.sleep(1)
    wait = WebDriverWait(browser, 20)
    elem = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    time.sleep(3 / 2)
    get_url_exc_page = elem.get_attribute('href')
    # 그냥 클릭하면 새로운 탭으로 연결되기 때문에 href 속성 값을 전부 변경 시킴
    browser.execute_script('''
        var elements = document.querySelectorAll(".category_link_category__XlcyC");
        elements.forEach(function(element) {
            element.setAttribute("target", "_self");
        });
    ''')
    time.sleep(1)
    elem.click()
    time.sleep(1)
    # 클릭 이후에 기존 탭에서 카테고리 창이 열렸는지 확인
    print('===================================browser===================================')
    print('현재url : ', browser.current_url)
    print('잠시 대기')
    return get_url_exc_page, input_category

#____________________스크랩________________________
def crawl(browser = '', get_url_exc_page = '' ,input_category = ''):
    data_result_2d = []  # 최종적으로 사용할 데이터 그릇(2차원 배열)
    print('=' * 50, '원하는 데이터의 갯수를 입력해주세요', '=' * 50)
    data_num = int(input())
    end_page = math.ceil(data_num / 40)
    # 엑셀열기
    # 슬래쉬를 경로로 인식하는 문제를 해결하기 위해 r과 replace함수 사용
    base_path = 'D:\\LSH\\workspace\\phthons\\teamProject\\'
    csv_file_name = '{}{}개.csv'.format(input_category, data_num).replace('/', '')
    f = open(base_path + csv_file_name, 'w', encoding='UTF-8-sig', newline='')
    writer = csv.writer(f, delimiter=',')
    # 엑셀에 컬럼입력하기
    col_list = '제목, 가격, e북가격, 연도, 등수'.split(', ')
    data_result_2d.append(col_list)

    # 1-end_page 반복
    for i in range(1, end_page + 1):
        # 연결테스트
        get_url = get_url_exc_page + '&pageIndex={}&pageSize=40'.format(i)
        user_agent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        res_data = requests.get(get_url, headers=user_agent)
        if res_data.status_code == requests.codes.OK:
            print('{}page 접속URL=====>[  {}  ]에 접속완료 '.format(i, get_url))
        else:
            print('권한이 없어 접속에 실패하였습니다.')

        # 데이터 가져오기(pagesize는 변경 불가 : 40)
        for j in range(1, 40 + 1):
            elem = browser.find_element(By.XPATH, '//*[@id="book_list"]/ul/li[{}]'.format(j))
            title = elem.find_elements(By.CSS_SELECTOR, '.bookListItem_title__X7f9_')
            price = elem.find_elements(By.CSS_SELECTOR, '.bookPrice_price__zr5dh>em')
            e_price = elem.find_elements(By.CSS_SELECTOR, '.bookListItem_sub_info__AfkOO em')
            date = elem.find_elements(By.CLASS_NAME, 'bookListItem_detail_date___byvG')
            rank = elem.find_elements(By.CSS_SELECTOR, '.bookListItem_feature__txTlp')
            print('________________' * 10)
            data_list_1d = []  # 2D그릇에 넣을 1D 데이터, 매번 초기화해야 하기 때문에 for문 안에 넣기
            if (len(data_result_2d)-1)< data_num:  # '='을 넣으면 마지막에 하나더 삽입 됨
                data_list_1d.append(title[0].text)
                data_list_1d.append(price[0].text.replace(',', ''))
                if len(e_price) == 2:
                    if e_price[1].text == '무료':
                        e_price[1] = 0
                        data_list_1d.append(e_price[1])
                    else:
                        data_list_1d.append(e_price[1].text.replace(',', ''))
                else:
                    data_list_1d.append(' ')
                data_list_1d.append(date[0].text)
                if len(rank) != 0:
                    data_list_1d.append(rank[0].text)
                else:
                    data_list_1d.append(' ')
                data_result_2d.append(data_list_1d)
                #writer.writerow(data_result_2d[int(j) - 1])
                print('dataList ===>', data_list_1d)
                print('>>>>>>>삽입한 개수 {}>>>>>>목표 개수 {}>>>>>>>'.format(len(data_result_2d)-1, data_num))
            else:
                print('--------------입력이 완료되었습니다.----------------')
                break

        # 다음 페이지로 넘어가기
        next_url = browser.current_url.replace('&pageIndex={}'.format(i), '&pageIndex={}'.format(i+1))
        # next_url = get_url_exc_page + '&pageIndex={}&pageSize=40'.format(i + 1)
        browser.get(next_url)
        # 스크롤 내리기
        scroller.scroll_down_max(browser)
        
    
    # 파일 저장
    writer.writerows(data_result_2d)
    f.close()
    print('=' * 30, 'csv파일 저장', '=' * 30)
    return data_result_2d, base_path, csv_file_name, data_num

#_______google sheet에 저장____________________
def gspread_fx(position='', data_result_2d=''):
    # json 파일이 위치한 경로를 값으로 줘야 합니다.
    json_file_path = r"D:\LSH\workspace\phthons\cred.json"
    gc = gspread.service_account(json_file_path)
    spreadsheet_url = "https://docs.google.com/spreadsheets/d/178r_LNfWGecOdvy36ehlYTpKN_tx1wE6ecXx9VlFcF8/edit?usp=sharing"
    doc = gc.open_by_url(spreadsheet_url)

    worksheet = doc.worksheet("시트1")
    worksheet.update(position, data_result_2d) 