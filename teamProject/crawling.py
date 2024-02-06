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

def navigate_to_category(browser, input_category):
    browser.get('https://search.shopping.naver.com/book/home')
    time.sleep(1)
    scroll_down_max(browser)
    category_list_elem = browser.find_element(By.CLASS_NAME, 'category_list_category__DqGyx')
    category_list = category_list_elem.text.split('\n')
    print('_'*30, '이하 카테고리 목록입니다.', '_'*30)
    print(category_list)
    print('_'*80)
    print('원하는 카테고리를 <<위의 카테고리 종류>>를 참조하여 입력해주세요(복사붙여넣기)')
    input_category = input()
    div_elements = browser.find_elements(By.CLASS_NAME, 'bookCard_card_wrap__Tx4e0')
    div_idx = len(div_elements)
    xpath_idx = category_list.index(input_category) + 1
    xpath = '//*[@id="container"]/div/div[{}]/div/ul/li[{}]/a'.format(div_idx, xpath_idx)
    time.sleep(1)
    wait = WebDriverWait(browser, 20)
    elem = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    time.sleep(3/2)
    get_url_exc_page = elem.get_attribute('href')
    browser.execute_script('''
        var elements = document.querySelectorAll(".category_link_category__XlcyC");
        elements.forEach(function(element) {
            element.setAttribute("target", "_self");
        });
    ''')
    time.sleep(1)
    elem.click()
    time.sleep(1)
    print('===================================browser===================================')
    print('현재url : ', browser.current_url)
    print('잠시 대기')
    scroll_down_max(browser)
    return get_url_exc_page

def scroll_down_max(browser):
    last_height = browser.execute_script("return document.documentElement.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        print("Scrolled!")
        time.sleep(1)
        new_height = browser.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
