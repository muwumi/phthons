import matplotlib.pyplot as plt

# 샘플 데이터 (정렬되지 않은 상태)
x = [5, 2, 4, 1, 3]
y = [10, 5, 8, 2, 6]

# 산포도 그리기
plt.scatter(x, y, label='Unsorted Data', color='blue', marker='o')

# 그래프에 제목과 축 레이블 추가
plt.title('Scatter Plot with Unsorted Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 범례 추가
plt.legend()

# 그래프 표시
plt.show()