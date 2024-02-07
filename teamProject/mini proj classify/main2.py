import opt
import scroller
import crawling
import analyzing
import mailing

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ... (다른 모듈 및 라이브러리 import)

def main():
    # 웹 설정
    browser = opt.web_setting()
    scroller.scroll_down_max(browser[0])

    # 카테고리 선택 및 스크랩핑
    cate_result = crawling.choose_category(browser[0])
    scroller.scroll_down_max(browser[0])
    crawl_result = crawling.crawl(browser[0], get_url_exc_page=cate_result[0], input_category=cate_result[1])

    # 데이터 분석
    excel_file_name_with_graph = analyzing.data_analyze(
        base_path=crawl_result[1],
        csv_file_name=crawl_result[2],
        input_category=cate_result[1],
        data_num=crawl_result[3]
    )

    # 메일 전송
    mailing.send_email(
        browser=browser[0],
        base_path=crawl_result[1],
        excel_file_name_with_graph=excel_file_name_with_graph[0]
    )

if __name__ == "__main__":
    main()
