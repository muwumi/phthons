import requests
from bs4 import BeautifulSoup
import csv #엑셀, 엑셀에 입력하기 위해서는 list가 되어야 함
import time, os, sys, math

print('원하는 자료의 개수를 숫자 형식으로 입력하세요')
dataNum = int(input())
endPage = math.ceil(dataNum/50)
print('endPage ====>', endPage)
userAgent = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}



for i in range(endPage):
    nowPage = int(i)+1
    print('=============={}연결테스트==============='.format(nowPage))
    print('nowPage ====>', nowPage)
    url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page={}'.format(nowPage)
    #url = f'https://finance.naver.com/sise/sise_market_sum.naver?&page={i}'
    print('접속 url ===> ', url)
    resData = requests.get(url, headers=userAgent)
    #print(resData.status_code)
    if resData.status_code == requests.codes.OK :
        print(nowPage,'page 접속====> 정상입니다')
        pass
    else :
        print('실패 권한이 없습니다')
    resData.raise_for_status() #에러가 발생하면 익셉션 발생시키고 종료시킴

    print('=================데이터 가져오기===============')
    soup = BeautifulSoup(resData.text, 'lxml')
    rows = soup.find('table', attrs={ 'class' : 'type_2' }).find('tbody').find_all('tr')
    titleList = 'N	종목명	현재가	전일비	등락률	액면가	시가총액(억원)	상장주식수	외국인비율	거래량	PER	ROE	토론실'.split()
    print('titleList : ', titleList)
    f = open('주식시총200.csv', 'w', encoding='UTF-8-sig', newline='')
    if i==0 :
        writer = csv.writer(f, delimiter=',')
        writer.writerow(titleList)
    print('=========가져온 rows를 출력해볼게요')
    for row in rows:
        colums = row.find_all('td')
        if len(colums) <= 1 : #불필요한 자료 제거 필터링
            continue #다시 앞으로 돌아가서 반복문 처음으로 돌아가라
        dataList = []
        for colum in colums :
            colTxt = colum.get_text().strip()
            dataList.append(colTxt)
        #원하는 데이터 갯수 초과시 클리어
        if int(dataList[0]) > dataNum :
            dataList.clear()
        writer.writerow(dataList[int(i)-1])
    print(dataList)
