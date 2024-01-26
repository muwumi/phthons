def minmax(data):
    return min(data), max(data)

(minNum, maxNum) = minmax([1, 11, 64,76, 34, 83, 26])
print('가장 작은 숫자 : {0}입니다. 그리고 가장 큰 숫자는 : {1}'.format(minNum, maxNum))

print('====='*35)
complexDataA = 2 + 3j
complexDataB = 2 + 3j
complexResult = complexDataA + complexDataB
complexResultT = complexDataA * complexDataB
print(complexResult, complexResultT)