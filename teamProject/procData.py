import pandas, os, sys, seaborn, matplotlib, csv, numpy
import matplotlib.pyplot as plt

#csv 읽어오고 데이터 가져오기
    #csv 읽기
csvPath = r'D:\LSH\workspace\phthons\teamProject\종교95개.csv'
csvDataFrame = pandas.read_csv(csvPath, sep=',', encoding='utf-8-sig')
print(csvDataFrame)
print(type(csvDataFrame))
    #데이터 컨트롤
price = csvDataFrame.loc[0 : , ['가격']]
rank = csvDataFrame.loc[0 : , ['등수']]
priceList2D = price.values.tolist()
rankList2D = rank.values.tolist()

priceList = []
rankList = []
for i in range(len(priceList2D)):
    priceList.append(int(priceList2D[i][0].replace(',', '')))
    rankList.append(int(rankList2D[i][0].split(' ')[1].replace('위', '')))
    
print('='*50)
print(priceList)
print('='*50)
print(rankList)


#그래프 그려보기
    #plt.plot([x값인자], [y값인자])
    #데이터 정렬(가격)

    # x, y 설정
x = priceList
y = rankList

    # 산포도 그리기
plt.scatter(x, y, label='Unsorted Data', color='blue', marker='o')

    # 그래프에 제목과 축 레이블 추가
plt.title('scatter of price and rank')
plt.xlabel('price')
plt.ylabel('rank')

# 범례 추가
plt.legend()

# 그래프 표시
plt.show()