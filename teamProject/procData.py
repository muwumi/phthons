import math
import pandas, os, sys, seaborn, matplotlib, csv, numpy
import matplotlib.pyplot as plt

#csv 읽어오고 데이터 가져오기
    #csv 읽기
csvPath = r'D:\LSH\workspace\phthons\teamProject\소설50개.csv'
csvDataFrame = pandas.read_csv(csvPath, sep=',', encoding='utf-8-sig')
print(csvDataFrame)
print(type(csvDataFrame))
    #데이터 컨트롤
bTitle = csvDataFrame.loc[0 : , ['제목']]
price = csvDataFrame.loc[0 : , ['가격']]
ePrice = csvDataFrame.loc[0 : , ['e북가격']]
rank = csvDataFrame.loc[0 : , ['등수']]
bTitleList2D = bTitle.values.tolist()
priceList2D = price.values.tolist()
ePriceList2D = ePrice.values.tolist()
rankList2D = rank.values.tolist()

bTitleList = []
priceList = []
ePriceList = []
rankList = []
for i in range(len(priceList2D)):
    #e북 가격이 없는 경우 별도로 처리를 해줘야함
    if(ePriceList2D[i][0]!=' '):
        bTitleList.append(bTitleList2D[i][0])
        priceList.append(int(priceList2D[i][0].replace(',', '')))
        ePriceList.append(int(ePriceList2D[i][0].replace(',', '')))
        rankList.append(int(rankList2D[i][0].split(' ')[1].replace('위', '')))

print('='*50, 'bTitleList')
print(bTitleList)    
print('='*50, 'priceList')
print(priceList)
print('='*50, 'ePriceList')
print(ePriceList)
print('='*50, 'rankList')
print(rankList)

'''
#그래프 그려보기
    #plt.plot([x값인자], [y값인자])
    #데이터 정렬(가격)

    # x, y 설정
x = priceList
y = rankList
z = ePriceList
rate = []
for i in range(len(priceList)):
    print(i)
    rate.append(round(int(ePriceList[i])/int(priceList[i]), 3)) 
print('=======>rate : {}, {}개'.format(rate, len(rate)))

sortedPriceList = sorted(priceList)
maxX = sortedPriceList[len(priceList)-1]
minX = sortedPriceList[0]
print('=======>priceList : {}, {}'.format(priceList, len(priceList)))
print('=======>epriceList : {}, {}'.format(ePriceList, len(ePriceList)))


# 데이터 생성
categories = []
for i in range(len(priceList)):
    strInput = '[{}] {}'.format(i, priceList[i])
    categories.append(strInput)
print(categories)
plt.scatter(categories, rate, s=5)


# 그래프에 제목과 축 레이블 추가
plt.title('Sum of Paper Price, Ebook Price, and Rank')
plt.xlabel('Categories')
plt.ylabel('Values')

# 그래프 표시
plt.show()'''

import pandas as pd
import matplotlib.pyplot as plt



# DataFrame의 plot() 메서드를 사용하여 선 그래프 그리기
csvDataFrame.plot(x='제목', y='가격', kind='line', marker='o', linestyle='-', color='blue', label='Line Plot')

# 그래프에 제목과 축 레이블 추가
plt.title('Line Plot using pandas')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 범례 추가
plt.legend()

# 그래프 표시
plt.show()
