from selenium import webdriver as wb
from selenium.webdriver.chrome.options import Options
import time

options = Options()

#최대 화면 조건
options.add_argument('--start-maximized')

#화면 꺼짐 방지 조건
options.add_experimental_option("detach", True)

#불필요한 에러메세지 제거 조건
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = wb.Chrome(options=options)

try :

    driver.get("https://naver.com/")
    input()

except Exception as e:
    print(e)

finally:
    driver.quit()
