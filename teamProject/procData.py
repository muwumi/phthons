import pandas, os, sys, seaborn, matplotlib, csv, numpy
import matplotlib.pyplot as plt

#csv 읽어오고 데이터 가져오기
    #csv 읽기
csvPath = r'D:\LSH\workspace\phthons\teamProject\소설50개.csv'
csvDataFrame = pandas.read_csv(csvPath, sep=',', encoding='utf-8-sig')
print(csvDataFrame)
print(type(csvDataFrame))
    #데이터 컨트롤
price = csvDataFrame.loc[0 : , ['가격']]
ePrice = csvDataFrame.loc[0 : , ['e북가격']]
rank = csvDataFrame.loc[0 : , ['등수']]
priceList2D = price.values.tolist()
ePriceList2D = ePrice.values.tolist()
rankList2D = rank.values.tolist()

priceList = []
ePriceList = []
rankList = []
for i in range(len(priceList2D)):
    #e북 가격이 없는 경우 별도로 처리를 해줘야함
    if(ePriceList2D[i][0]!=' '):
        priceList.append(int(priceList2D[i][0].replace(',', '')))
        ePriceList.append(int(ePriceList2D[i][0].replace(',', '')))
        rankList.append(int(rankList2D[i][0].split(' ')[1].replace('위', '')))
    
print('='*50, 'priceList')
print(priceList)
print('='*50, 'ePriceList')
print(ePriceList)
print('='*50, 'rankList')
print(rankList)

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
    rate.append(int(z[i])/int(x[i])) 
print('=======>rate : ' ,rate, len(rate))

sortedPriceList = sorted(priceList)
maxX = sortedPriceList[len(priceList)-1]
minX = sortedPriceList[0]
print(priceList)

'''
    # 산포도 그리기
plt.scatter(x, y, label='Unsorted Data', color='blue', marker='o')

    # 그래프에 제목과 축 레이블 추가
plt.title('scatter of price and rank')
plt.xlabel('price')
plt.ylabel('rank')
'''
'''
    # 산포도 그리기
plt.scatter(x, z, label='Unsorted Data', color='blue', marker='o')

    # 그래프에 제목과 축 레이블 추가
plt.title('scatter of price and ebookPrice')
plt.xlabel('price')
plt.ylabel('ePrice')
'''
'''
    #히스토그램그리기(빈도)
plt.hist(x, label='paper-price',color='blue')

plt.hist(z, label='ebook-price', color='yellow')
'''

plt.scatter(x, rate)
plt.title('ebookPrice/paperPrice')
plt.xlabel('paper book price')
plt.ylabel('rate(ebook/paper)')
plt.xlim(minX-100, maxX+100)
plt.ylim(0, 1)


# 범례 추가
plt.legend()

# 그래프 표시
plt.show()

