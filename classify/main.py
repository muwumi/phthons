import opt, scroller, crawling, analyzing, mailing
import global_variation as gb
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

#________________________________________웹에 접속_______________________________________
browser = opt.web_setting()
scroller.scroll_down_max(browser[0])
#__________________________________________크롤링________________________________________
#카테고리
cate_result = crawling.choose_category(browser[0])
#스크랩핑
scroller.scroll_down_max(browser[0])
crawl_result = crawling.crawl(browser[0], get_url_exc_page= cate_result[0], input_category= cate_result[1])

#___________________________________________데이터 분석___________________________________
excel_file_name_with_graph = analyzing.data_analyze(base_path=crawl_result[1], csv_file_name= crawl_result[2], input_category=cate_result[1], data_num=crawl_result[3])

#___________________________________________메일링________________________________________
mailing.send_email(browser=browser[0], base_path=crawl_result[1], excel_file_name_with_graph=excel_file_name_with_graph[0])
