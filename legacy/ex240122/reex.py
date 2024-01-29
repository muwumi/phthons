import re

#정규식은 데이터의 표현 형식을 지정하는 것
p = re.compile('^yang') #정규식에서 . => 문자 하나 : yang yaag yabg 등등이 부합
k = p.match('yangdoll')
#^ => 시작
#$ => 끝

print(type(p),'@@@@@@@@@' ,p)
print(type(k), '         $$$       ', k)
print(k.group()) #정규식에 맞는 단어를 출력
print(k.string) #정규식에서 테스트되는 기준의 단어 출력(yangdoll)
