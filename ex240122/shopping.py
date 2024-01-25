import requests
from bs4 import BeautifulSoup
import time

print('원하는 페이지를 숫자 형식으로 입력하세요')
page=input()
url = 'https://search.shopping.naver.com/search/all?adQuery=%EC%BB%B4%ED%93%A8%ED%84%B0&frm=NVSHATC&origQuery=%EC%BB%B4%ED%93%A8%ED%84%B0&pagingIndex='+str(page)+'&pagingSize=40&productSet=total&query=%EC%BB%B4%ED%93%A8%ED%84%B0&sort=price_asc&timestamp=&viewType=list'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

resData = requests.get(url, headers=headers)

print('=============연결테스트===========')
print(resData.status_code)

if resData.status_code == requests.codes.OK :
    print('정상입니다')
    pass
else :
    print('실패 권한이 없습니다')

resData.raise_for_status() #에러가 발생하면 종료시킴

print('==============data 가져오기=============')
soup = BeautifulSoup(resData.text, 'lxml')
priceList = soup.find_all('span', attrs={'class' : 'price_num__S2p_v'})

for i in range(len(priceList)):
    price = (priceList[i].em).text
    print('price'+str(i)+' =====>', price)

