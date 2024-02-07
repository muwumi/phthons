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

def scroll_down_max(browser = webdriver.Chrome):
    last_height = browser.execute_script("return document.documentElement.scrollHeight")
    while True:
        # 스크롤 끝까지 내리기
        browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        print("Scrolled!")
        # 스크롤 내린 후 페이지 로딩 시간 필요
        time.sleep(1)

        # 스크롤 내린 후 페이지 높이
        new_height = browser.execute_script("return document.documentElement.scrollHeight")

        # 더이상 스크롤이 내려가지 않을 때 까지 스크롤 내리는 반복문 멈추기
        if new_height == last_height:
            break
        # 스크롤 내린 후 페이지 높이를 현재 페이지 높이 변수에 저장
        last_height = new_height

