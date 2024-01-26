import os

#파일과 폴더를 구별하는 것
path = 'C:\\Users\\user\\Desktop'
dataList = os.listdir(path)
print('='*100)
print(type(dataList))
print('='*100)
print(dataList)

os.path.isfile

fileList = []
folderList = []
for i in range(len(dataList)):
    getPath = path+'\\'+dataList[i]
    if os.path.isfile(getPath):
        print('='*60)
        print('{}은(는) 파일입니다.'.format(dataList[i]))
        fileList.append(dataList[i])
    else :
        print('='*60)
        print('{}은(는) 폴더입니다.'.format(dataList[i]))
        folderList.append(dataList[i])
print('fileList : ', fileList)
print('folderist : ', folderList)
