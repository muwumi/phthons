#점수 리스트 세팅
kor = {
    "a": 55 ,
    "b": 68,
    "c": 78,
    "d": 46,
    "e": 34,
    "f": 64,
    "g": 67,
    "h": 52,
    "i": 97,
    "j": 82 
}

math = {
    "a": 55 ,
    "b": 68,
    "c": 78,
    "d": 46,
    "e": 91,
    "f": 44,
    "g": 67,
    "h": 72,
    "i": 97,
    "j": 82 
}

eng = {
    "a": 55 ,
    "b": 68,
    "c": 78,
    "d": 66,
    "e": 91,
    "f": 64,
    "g": 67,
    "h": 12,
    "i": 97,
    "j": 82 
}
subject = {'kor', 'math', 'eng'}

#평균 점수

i=0
totalList = {}
avgList = {}
while i <  len(list(kor.keys())) :
    inputName = list(kor.keys())[i]
    total = kor[inputName] + math[inputName] + eng[inputName]
    avg = round(total/len(subject)) 
    totalList[inputName] = total
    avgList[inputName] = avg
    i = i+1

print("최종 평균 리스트=>>>>", avgList)

''''값만을 우선 배열로 만든다'''
jList = list(avgList.values())
print("avg list : ",jList)
'''' 배열을 나열한다 '''
sortedList = sorted(jList)
''''이름을 검색하면 해당 값의 위치-10등을 반환한다'''
print("@@@@@@@콘솔 창에 원하는 사람의 이름을 입력하세요@@@@@@@")
targetName = input()
resultJumsu = avgList.get(targetName)
indexOfName = sortedList.index(resultJumsu)
rank = (len(jList)-indexOfName) 
print(str(targetName)+ "의 최종 등수 : ", str(rank)+'등', )
print("총점 : ", totalList.get(targetName))
print("평균 : ", avgList.get(targetName))


