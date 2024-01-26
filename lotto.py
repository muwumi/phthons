#20명 중에 3명은 문화상품권, 1명은 자동차를 선물하는 시스템
import  csv, random

#20명의 지원자 명단
people = '김은영 이상헌 채화연 김태곤 알고니 제모로 크록스 가콰몰래 카타카 김물래 습근평 등소평 왕후파 후참잘 양우영 채연 박재정 윤석열 김나영 유재석'.split(' ')

#당첨자 4인
lotto4p = []
munRanNum = []
for i in range(0, 4):
    ranNum1 = random.randint(0, 19)
    lotto4p.append(people[ranNum1])
    munRanNum.append(ranNum1)
print('================당첨자=============')
print(lotto4p)

#4인 중에서 재추첨
ranNUm2 = random.randint(0, 3)
car = lotto4p[ranNUm2]
lotto4p.remove(car)
print('================자동차 당첨===============')
print(car)
print('==================문화상품권 당첨==============')
print(lotto4p)

#remove함수에서 오랫동안 헤맴........ 그냥 원래 리스트를 반환하면 됨
