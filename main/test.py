# import matplotlib.pyplot as plt
# import numpy as np

# # 데이터 준비
# categories = ['Americano', 'Latte', 'Cappuccino']
# male_values = [30, 45, 20]
# female_values = [25, 35, 30]

# # 막대 그래프 생성
# bar_width = 0.35  # 각 막대의 너비
# index = np.arange(len(categories))  # 각 카테고리의 인덱스

# plt.bar(index, male_values, width=bar_width, label='Male', color='blue')
# plt.bar(index + bar_width, female_values, width=bar_width, label='Female', color='red')

# # 그래프에 제목과 축 레이블 추가
# plt.title('Coffee Purchase by Gender')
# plt.xlabel('Coffee Types')
# plt.ylabel('Purchase Quantity')

# # 카테고리 레이블 설정
# plt.xticks(index + bar_width / 2, categories)

# # 범례 추가
# plt.legend()

# # 그래프 보여주기
# plt.show()

from datetime import datetime


today_date = datetime.now().strftime("%Y%m%d")
print(today_date)