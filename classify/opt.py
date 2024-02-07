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

def web_setting():
    # 옵션설정
    options = Options()
    # 최대 화면 조건
    options.add_argument('--start-maximized')
    # 자동화 인식을 무력화 하기 위한 수단
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    # 화면 꺼짐 방지 조건
    options.add_experimental_option("detach", True)
    # 불필요한 에러메시지 제거 조건
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    browser = webdriver.Chrome(options=options)
    # 크롤링 차단되었을 때
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})

    # 사이트 연결
    browser.get('https://search.shopping.naver.com/book/home')
    browser.page_source
    time.sleep(1)

    return (browser, )