import matplotlib.pyplot as plt

# 데이터 생성 (예시 데이터)
x_values = [1, 2, 3, 4, 5]
y_values = [10, 12, 5, 8, 6]

# 꺾은 선 그래프 그리기
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b', label='Line Plot')

# 그래프 제목과 축 레이블 설정
plt.title('Line Plot Example')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# 범례 표시
plt.legend()

# 그래프 보여주기
plt.show()
