def testFX(a: int, b: int, c: str):
    print(a+b)
    print('{}님의 점수는 {}점 입니다.'.format(c, (a+b)))

testFX(1, 2, '이상헌')

testFX(1, 3, 'lee')
