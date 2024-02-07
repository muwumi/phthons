import opt
import scroller
import crawling
import analyzing
import mailing
import file_saving

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
모든 메서드의 결과값은 튜플로 반환 : 데이터를 복수 이상 반환하기
'''
#________________________________________웹에 접속_______________________________________
browser = opt.web_setting()
scroller.scroll_down_max(browser[0])
#__________________________________________크롤링________________________________________

    #카테고리 선택
cate_result = crawling.choose_category(browser[0])
    #스크롤 내리기
scroller.scroll_down_max(browser=browser[0])
    #크롤링
crawl_result = crawling.crawl(browser[0], get_url_exc_page= cate_result[0], input_category= cate_result[1])
    #데이터를 csv 파일로 저장
file_saving.csv_save(base_path=crawl_result[1], csv_file_name='{}{}개.csv'.format(cate_result[1], crawl_result[3]), data_result_2d=crawl_result[0])
    #데이터를 구글스프레드에 저장
position = 'A1'
spreadsheet_url = "https://docs.google.com/spreadsheets/d/178r_LNfWGecOdvy36ehlYTpKN_tx1wE6ecXx9VlFcF8/edit?usp=sharing"
file_saving.gspread_fx(spreadsheet_url=spreadsheet_url, position=position , data_result_2d= crawl_result[0])

#___________________________________________데이터 분석___________________________________
analyze = analyzing.data_analyze(base_path=crawl_result[1], csv_file_name= crawl_result[2], input_category=cate_result[1], data_num=crawl_result[3])
exc_save = file_saving.exc_save(input_category=cate_result[1], base_path=crawl_result[1], data_num=crawl_result[3], csv_data_frame=analyze[0], graph_list=analyze[1])

#___________________________________________메일링________________________________________
mailing.send_email(browser=browser[0], base_path=crawl_result[1], excel_file_name_with_graph=exc_save[0])
