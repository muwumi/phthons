import requests
from bs4 import BeautifulSoup
import time

print('================연결 테스트===============')
'''
searchList = ['new', 'genre']
for search in searchList:
    url = 'https://comic.naver.com/webtoon?tab=' + search

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

    resData = requests.get(url, headers=headers)

    print(resData.status_code)

    if resData.status_code == requests.codes.OK :
        print('정상입니다')
        pass
    else :
        print('실패 권한이 없습니다')

    resData.raise_for_status() #에러가 발생하면 종료시킴
'''
url = 'https://news.naver.com/'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
resData = requests.get(url, headers=headers)
resData.raise_for_status()

print('=========뷰티풀숲=============')
print(url)
soup = BeautifulSoup(resData.text, 'lxml')
print(soup.a)
with open('result.html', 'w', encoding='utf-8') as htmlf:
    htmlf.write(soup.get_text())
#seldiv = soup.find_all("div", attrs={'class' : 'cjs_news_tw'})
seldiv = soup.select('div.cjs_news_tw')

print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'*3)
print(seldiv)
print('type=>>>>>>>>', type(seldiv))
for seldata in seldiv:
    print('===============================================')
    print( seldata)
    print( seldata.a)
    print( seldata.p)



parent = seldata.parents
print('^$^$^$^$^$^====>', parent)
#print('=====>', parent.a['href'])