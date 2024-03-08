import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from write_query import write_query


qdf = write_query()
# #데이터 분석
# select1 = 'MENU'
# select2 = 'MENU_SALE_PRICE'

# menu_price_df = df[['CATE_ID', 'MENU_ID', select2]]
# menu_total_price = menu_price_df.groupby(['CATE_ID', 'MENU_ID']).sum().reset_index()
# menu_total_price[select1] = menu_total_price['CATE_ID'].astype(str) + '-' + menu_total_price['MENU_ID'].astype(str)

# print(menu_total_price)
# plt.bar(menu_total_price[select1], menu_total_price[select2])
# plt.xlabel(select1)
# plt.ylabel(select2)
# plt.title('23년도 3월 전연령 여성 커피메뉴 판매금액 합산내역')
# plt.show()
plt.rcParams['font.family'] = 'MalGun Gothic'
plt.rcParams['axes.unicode_minus'] = False
select1 = 'MENU'
select2 = 'USER_SEX'
select3 = 'MENU_COUNT'

qdf['CATE_MENU_ID'] = qdf['CATE_ID'] + '-' + qdf['MENU_ID'].astype(str)

df_grouped = qdf.groupby(['CATE_MENU_ID', 'USER_SEX'], as_index=False)['MENU_COUNT'].sum()

# 메뉴를 x축으로 하고 성별에 따른 막대 그래프 그리기
plt.figure(figsize=(10, 5))
sns.barplot(x='CATE_MENU_ID', y='MENU_COUNT', hue='USER_SEX', data=df_grouped)
plt.title('성별에 따른 메뉴별 판매량')
plt.xlabel('메뉴 ID')
plt.ylabel('카운트')
plt.savefig('이미지.png')
plt.show()
