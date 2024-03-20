import pandas as pd

# 딕셔너리를 사용하여 데이터프레임 생성
data =     {'cate_id':[10, 20, 30], 'cate_name':['커피', '논커피', '에이드']}

df = pd.DataFrame(data)
result = {10:'커피', 20:'논커피', 30:'에이드'}
result_dict = dict(zip(df['cate_id'], df['cate_name']))
print(result_dict)

print(df['cate_name'])
