import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# 주어진 데이터
data = {'Y': [25, 128, 3, 113, 7, 26, 19, 21, 42, 75, 41, 106, 30, 150, 18, 33, 127, 147, 94, 79, 114, 35, 1, 2, 40, 43, 93, 129, 104, 10, 13, 145, 100, 146, 53, 111, 130, 101, 133, 25, 128, 3, 113, 7, 26, 19, 21, 42],
        'X': [21380, 14370, 26820, 71820, 67500, 16920, 19800, 19800, 19670, 18810, 25650, 17000, 15820, 16930, 17100, 24800, 19800, 15220, 12400, 27360, 13500, 15820, 16920, 16200, 18810, 21380, 18810, 21380, 21380, 24300, 19800, 27360, 10260, 26010, 
14970, 28220, 25650, 17100, 18810, 21380, 14370, 26820, 71820, 67500, 16920, 19800, 19800, 19670]}

print(len(data['X']))
print(len(data['Y']))

# 데이터프레임 생성
df = pd.DataFrame(data)

# 독립 변수(X)에 상수항 추가
X = sm.add_constant(df['X'])

# 종속 변수(Y)
Y = df['Y']

# 선형 회귀 모델 생성
model = sm.OLS(Y, X)

# 모델 피팅
results = model.fit()

# 회귀분석 결과 출력
regResult = results.summary()
print(results.summary())
print(type(regResult))

# 데이터 산점도와 회귀선 시각화
plt.scatter(df['X'], df['Y'], label='실제 데이터')
plt.plot(df['X'], results.predict(), color='red', label='회귀선')
plt.xlabel('독립 변수 (X)')
plt.ylabel('종속 변수 (Y)')
plt.legend()
plt.show()

'''#=========================================================
import pandas as pd
import matplotlib.pyplot as plt

# 예제 데이터 생성
data = {'Title': ['Book1', 'Book2', 'Book3'],
        'PaperPrice': [20, 25, 30],
        'EbookPrice': [15, 20, 25]}

# 데이터프레임 생성
df = pd.DataFrame(data)

# e북 가격 비율 계산 및 DataFrame에 추가
df['EbookRatio'] = df['EbookPrice'] / df['PaperPrice']

# 전체 평균 계산
avg_ratio = df['EbookRatio'].mean()

# 그래프 표시
plt.scatter(df['Title'], df['EbookRatio'], color='blue', label='e북 가격 비율')
plt.axhline(y=avg_ratio, color='red', linestyle='--', label='전체 평균')

plt.xlabel('책 제목')
plt.ylabel('e북 가격의 비율(종이책 가격 대비)')
plt.title('e북 가격과 종이책 가격의 비율 분석')
plt.legend()
plt.show()
'''