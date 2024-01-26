import requests
from bs4 import BeautifulSoup
import time

print('================필수요소================')
print('원하는 페이지를 숫자 형식으로 입력하세요')
url = 'https://finance.naver.com/'
userAgent = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
resData = requests.get(url, headers=userAgent)

print('=============연결테스트===========')
print(resData.status_code)

if resData.status_code == requests.codes.OK :
    print('정상입니다')
    pass
else :
    print('실패 권한이 없습니다')

resData.raise_for_status() #에러가 발생하면 종료시킴

print('=================데이터 가져오기===============')
soup = BeautifulSoup(resData.text, 'lxml')
sel = soup.select('tbody#_topItems1')
print(sel)
print(len(sel))
for i in range(len(sel)):
    print('===============>', sel[i].td)