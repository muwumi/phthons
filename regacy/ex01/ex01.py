#점수 리스트 세팅
jumsu = {
         "a": 55 ,
         "b": 68,
         "c": 78,
         "d": 46,
         "e": 91,
         "f": 64,
         "g": 67,
         "h": 52,
         "i": 97,
         "j": 82
        }
print("점수데이터",jumsu)

#점수 값 추출 후 순서대로 나열
jumsuVal = jumsu.values()
print("점수값들",jumsuVal)
print("점수값들 타입", type(jumsuVal))
jumsuValList = list(jumsuVal)
print("점수값들을 리스트로 변환",jumsuValList)
jumsuSorted = sorted(jumsuValList)
print('점수를 나열(작은순)',jumsuSorted)

#값을 통해 키를 얻어오기
def get_keys_by_value(dictionary, target_value):
    return [key for key, value in dictionary.items() if value == target_value]


#석차 나열 후 리스트에 넣어버리기
i=0
nameSortedList = []
sukcha =[]
result = {}
while i < len(jumsuSorted):
    nameI = get_keys_by_value(jumsu, jumsuSorted[i])[0]
    sukchaI = 10-i
    result[nameI] = sukchaI
    i = i+1


#결과 테스트
print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV 이름을 입력하세요")
targetName = input()
print(result.get(targetName),"등")
