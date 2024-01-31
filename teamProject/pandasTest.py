import pandas as pd

#전체 파일 딕셔너리
dataDict = {}
#컬럼명 리스트
colList = ['컬럼1', '컬럼2']
#컬럼내부에 해당하는 값 리스트
valList = ['어떤 값1', '어떤 값2', '어떤 값3']

#전체 파일 딕셔너리에 삽입
#형식설명
print( r'''dataDict['key로 컬럼명이 들어갑니다. string 배열로 만들어서 인덱스로 특정해준다면 for문 활용이 용이할 것입니다'] = '값으로 배열 <통채로> 들어갑니다' ''' )
dataDict[colList[0]] = valList
dataDict[colList[1]] = valList

#그냥 출력해보기
print('================={}===================='.format('그냥출력해보기'))
print(dataDict)

#데이트 프레임으로 출력
print('================={}===================='.format('데이터프레임으로'))
dataFrame = pd.DataFrame(dataDict)
print(dataFrame)

#cvs로 저장해보기
dataFrame.to_csv('dataFrame.csv', index=True, encoding='utf-8-sig')
print('================={}===================='.format('csv파일로'))