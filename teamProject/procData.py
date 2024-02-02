import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook, load_workbook
from openpyxl.drawing.image import Image
import matplotlib.font_manager as fm
import tkinter as tk
from tkinter import ttk

# 바탕글꼴 경로 설정
font_path = 'C:/Windows/Fonts/batang.ttc'

# 폰트 이름 가져오기
font_name = fm.FontProperties(fname=font_path).get_name()

# 폰트 설정
plt.rc('font', family=font_name)

# csv 읽어오고 데이터 가져오기
csvPath = r'D:\LSH\workspace\phthons\teamProject\자기계발55개.csv'
csvDataFrame = pd.read_csv(csvPath, sep=',', encoding='utf-8-sig')

# 데이터 컨트롤(제목, 가격, e북가격, 등수)
bTitle = csvDataFrame.loc[:, ['제목']]
price = csvDataFrame.loc[:, ['가격']]
ePrice = csvDataFrame.loc[:, ['e북가격']]
rank = csvDataFrame.loc[:, ['등수']]

bTitleList = bTitle['제목'].tolist()
priceList = price['가격'].tolist()  
ePriceList = ePrice['e북가격'].tolist() 
rankList = rank['등수'].str.replace('위', '').tolist()
print(len(bTitleList))
print(bTitleList)
print(priceList)
print(ePriceList)
print(rankList)  


#e북 가격 비율 만들기
ratioList = []
bTitleWithEbook = []
for i in range(len(bTitle)):
    if ePriceList[i] != ' ':
        #이북이 있는 타이틀만 추출
        bTitleWithEbook.append(bTitleList[i])
        #ratio추출
        ratio = round(int(ePriceList[i])/int(priceList[i]), 3)
        ratioList.append(ratio)
        

# 산포도 그리기(e북가격비율)
plt.scatter(bTitleWithEbook, ratioList)
plt.title('Scatter')
plt.xlabel('book-title')
plt.ylabel('ratio : ebook-price / paper-price')
plt.xticks(rotation=90)  # X 축 라벨 회전
plt.tight_layout()  # 레이아웃 조정
graphFileName = '{}.png'.format('임시 그래프')
plt.savefig(graphFileName)
plt.show()

# 엑셀 파일로 변환
excelPath = r'D:\LSH\workspace\phthons\teamProject\자기계발55개.xlsx'
csvDataFrame.to_excel(excelPath, index=False)

# 엑셀 파일 읽어오기
workbook = load_workbook(excelPath)
sheet = workbook.active

# 이미지 파일 불러오기
imgPath = r'D:\LSH\workspace\phthons\teamProject\{}'.format(graphFileName)
image = Image(imgPath)

# 이미지 삽입할 위치 지정
position = 'K2'
sheet.add_image(image, position)

workbook.save('자기계발55개 그래프추가.xlsx')


# Tkinter 창 생성
window = tk.Tk()
window.title("데이터프레임 뷰어")

# 데이터프레임을 표시할 Treeview 위젯 생성
tree = ttk.Treeview(window)
tree["columns"] = tuple(csvDataFrame.columns)

# 열 제목 설정
for column in csvDataFrame.columns:
    tree.heading(column, text=column)

# Treeview에 데이터 삽입
for index, row in csvDataFrame.iterrows():
    tree.insert("", "end", values=tuple(row))

# Treeview를 창에 적절히 배치
tree.pack(expand=True, fill="both")

# 행의 수를 보여줄 레이블 생성
label = tk.Label(window, text=str(len(csvDataFrame)) + '개')
label.pack()

# Tkinter 이벤트 루프 실행
window.mainloop()
