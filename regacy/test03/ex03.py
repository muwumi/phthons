#입력 폼 역할(반복)
print("이제 >>>'끝'<<<을 입력하기 전까지 데이터를 입력할 수 있습니다 ")

print("엔터를 쳐주세요(그만하고 싶으면 '끝'을 입력하세요)")
start = input()

k=0
dictMap = {}
while start != "끝":
    print("이름을 입력해주세요")
    name = input()
    dictSandS = {}
    print("국어 점수를 입력해주세요")
    dictSandS["kor"]=input()
    print("영어 점수를 입력해주세요")
    dictSandS["eng"]=input()
    print("수학 점수를 입력해주세요")
    dictSandS["math"]=input()
    
    #받은 데이터로 딕셔너리 만들기
    subject =  list(dictSandS.keys())
    information={"NAME" : name, "SCORE" : dictSandS}

    dictMap[(k)]=information
    print(dictMap)

    
    print("끝????")
    start = input()
    k=k+1
    

i=0
total = 0
while i<len(subject):
    resultData = (subject[i]+" = {}  ").format(dictSandS.get(subject[i]))
    print(resultData, end=" ")
    total = int( dictSandS.get(subject[i]) )  + total
    i = i+1
print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
length = len(list(dictSandS.keys())) 
avg = round( total/length )
information.get("SCORE")["total"]=total
information.get("SCORE")["avg"]=avg
print("최종결과 : ",information)
