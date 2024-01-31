import pandas as pd

#전체 파일 딕셔너리
dataDict = {}
#컬럼명 리스트
colList = ['컬럼1', '컬럼2']
#컬럼내부에 해당하는 값 리스트
valList = [['어떤 값1', '어떤 값2', '어떤 값3'], ['VALUE 1', 'VALUE 2', 'VALUE 3']]

#전체 파일 딕셔너리에 삽입
#형식설명
print( r'''dataDict['key로 컬럼명이 들어갑니다. string 배열로 만들어서 인덱스로 특정해준다면 for문 활용이 용이할 것입니다'] = '값으로 배열 <통채로> 들어갑니다' ''' )
print( r'''값으로 배열 <통채로> 들어가기에 이중 배열로 만든다면 for문 활용이 더욱 용이할 것입니다. ''' )
for i in range(len(colList)):
    dataDict[colList[i]] = valList[i]
    

#그냥 출력해보기
print('================={}===================='.format('그냥출력해보기'))
print(dataDict)

#데이트 프레임으로 출력
print('================={}===================='.format('데이터프레임으로'))
dataFrame = pd.DataFrame(dataDict)
print(dataFrame)

#cvs로 저장해보기
dataFrame.to_csv('dataFrame2.csv', index=True, encoding='utf-8-sig')
print('================={}===================='.format('csv파일로 저장'))


#선택해보기
print('================={}===================='.format('데이터 선택해보기'))
    #선택할 때 이중배열을 꼭 잊지말도록 합시다
    #원칙상 1개의 컬럼을 선택할 때 단일 배열을 쓰나, 복수 이상이라면 이중 배열을 사용합니다
    #그런데 이중배열은 그 어떤 개수의 자료에도 모두 적용되니 무조건 이중배열 사용으로 통일합시다

    #아래의 예시는 컬럼에 해당하는 특정 값을 불러오는 것입니다.
sel = dataFrame[['컬럼1', ]]
print('데이터============>\n', sel)
print('타 입============>{}'.format(type(sel)))

    #아래의 예시는 행에 해당하는 특정 값을 불러오는 것입니다.
    #loc: location의 약자로 자동으로 부여된 인덱스입니다
sel = dataFrame.loc[[0, 1, ]]
print('데이터============>\n', sel)
print('타 입============>{}'.format(type(sel)))
