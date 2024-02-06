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

# 크롤링 및 데이터 저장 관련 함수
def extract_data(browser, get_url_exc_page, input_category, data_num):
    data_result_2d = []  # 최종적으로 사용할 데이터 그릇(2차원 배열)
    print('='*50, '원하는 데이터의 갯수를 입력해주세요', '='*50)
    data_num = int(input())
    end_page = math.ceil(data_num/40)

    base_path = 'D:\\LSH\\workspace\\phthons\\teamProject\\'
    csv_file_name = '{}{}개.csv'.format(input_category, data_num).replace('/', '')
    f = open(base_path + csv_file_name, 'w', encoding='UTF-8-sig', newline='')
    writer = csv.writer(f, delimiter=',')
    col_list = '제목, 가격, e북가격, 연도, 등수'.split(', ')
    writer.writerow(col_list)

    for i in range(1, end_page+1):
        get_url = get_url_exc_page + '&pageIndex={}&pageSize=40'.format(i)
        user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        res_data = requests.get(get_url, headers=user_agent)

        if res_data.status_code == requests.codes.OK:
            print('{}page 접속URL=====>[  {}  ]에 접속완료 '.format(i, get_url))
        else:
            print('권한이 없어 접속에 실패하였습니다.')

        for j in range(1, 40+1):
            elem = browser.find_element(By.XPATH, '//*[@id="book_list"]/ul/li[{}]'.format(j))
            title = elem.find_elements(By.CSS_SELECTOR, '.bookListItem_title__X7f9_')
            price = elem.find_elements(By.CSS_SELECTOR, '.bookPrice_price__zr5dh>em')
            e_price = elem.find_elements(By.CSS_SELECTOR, '.bookListItem_sub_info__AfkOO em')
            date = elem.find_elements(By.CLASS_NAME, 'bookListItem_detail_date___byvG')
            rank = elem.find_elements(By.CSS_SELECTOR, '.bookListItem_feature__txTlp')
            print('________________'*10)
            data_list_1d = []  # 2D그릇에 넣을 1D 데이터, 매번 초기화해야 하기 때문에 for문 안에 넣기

            if len(data_result_2d) < data_num:
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
                writer.writerow(data_result_2d[int(j)-1])
                print('data_list ===>', data_list_1d)
                print('>>>>>>>삽입한 개수 {}>>>>>>목표 개수 {}>>>>>>>'.format(len(data_result_2d), data_num))
            else:
                print('--------------입력이 완료되었습니다.----------------')
                break

        nex_url = get_url = get_url_exc_page+'&pageIndex={}&pageSize=40'.format(i+1)
        browser.get(get_url)
        scroll_down_max(browser)

    f.close()
    print('='*30, 'csv파일 저장', '='*30)
    return csv_file_name
