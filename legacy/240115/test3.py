from selenium import webdriver as wb
from selenium.webdriver.chrome.options import Options
import time

#최대 화면 조건
options = Options()

#화면 꺼짐 방지 조건
options.add_argument('--start-maximized')

#불필요한 에러메세지 제거 조건
options.add_experimental_option("detach", True)

options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = wb.Chrome(options=options)

try :

    driver.get("https://news.naver.com/main/ranking/popularDay.naver")
    elems = driver.find_elements("class name", "rankingnews_box")

    for elem in elems:
        name = elem.find_element("class name", "rankingnews_name")
        tex = elem.find_element("class name", "rankingnews_list")
        print(tex.text, end='')
    input()

except Exception as e:
    print(e)

finally:
    driver.quit()
