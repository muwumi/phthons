import requests

url = 'https://engineer-mole.tistory.com/68'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

resData = requests.get(url, headers=headers)

print(resData.status_code)

if resData.status_code == requests.codes.OK :
    print('정상입니다')
    pass
else :
    print('실패 권한이 없습니다')

resData.raise_for_status() #접근에 에러가 있다면 exception을 발생시키며 종료함

#효과적인 크롤링을 위해서는 정규표현식(reqular expression:re)를 사용할 줄 알아야 함