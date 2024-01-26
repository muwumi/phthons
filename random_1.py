import sys
from datetime import datetime
def selfFx(c: int):
    # 기본 사례 정의
    if c <= 0:
        return 0

    # 재귀 호출
    result = selfFx(c - 1) / 7.3

    # 조건 충족 시 결과 반환
    if result <= 10:
        return result
    else:
        return 0 

print(selfFx(10123123))

'''
def randomFunction(a: int, b: int):
    ti = str(datetime.now())
    arrRand = ti.split('.')
    ranNum = arrRand[1]
    print('ranNum=========>', ranNum)
    
    if ranNum > b:
            selfFx(ranNum)
    else :
        return ranNum
'''


 