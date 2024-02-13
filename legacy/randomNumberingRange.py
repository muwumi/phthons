import sys
from datetime import datetime

def downFx(ranNum, a, b) :
    result = ranNum/13
    if a<= result <= b:
        return str(result).split('.')[0]
    else :
        return downFx(result, a, b)

def upFx(ranNum, a, b) : 
    result = ranNum * 1.5
    if result >= a:
        return str(result).split('.')[0]
    elif result < a:
        return upFx(result, a, b)

def randomFunction(a: int, b: int):
    ti = str(datetime.now())
    arrRand = ti.split('.')
    ranNum = int(arrRand[1])
    
    
    if ranNum > b:
        return downFx(ranNum, a, b)
    elif (a < ranNum < b) :
        return ranNum
    elif ranNum < a:
        return upFx(ranNum, a, b)

print('범위 설정에 들어갑니다.')
print('=========시작값을 설정해주세요=========')
start = int(input())
print('=========끝값을 설정해주세요=========')
end = int(input())

test = randomFunction(start, end)

print('test===>', test)