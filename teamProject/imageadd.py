from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

# 새로운 엑셀 파일 생성
filePath = r'D:\LSH\workspace\phthons\teamProject\소설22개.xlsx'
workbook = load_workbook(filePath)  
sheet = workbook.active

# 이미지 파일 불러오기
imgPath = r'D:\LSH\workspace\phthons\teamProject\graph.png'
image = Image(imgPath)

# 이미지 삽입할 위치 지정
position = 'K2'
sheet.add_image(image, position)

workbook.save('소설22개 그래프추가.xlsx')
