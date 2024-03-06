import cx_Oracle
import pandas as pd
import matplotlib.pyplot as plt

# Oracle 연결 설정
con = cx_Oracle.connect("lee", "lee", "localhost", encoding="UTF-8")

# SQL 쿼리 실행 및 결과를 DataFrame으로 변환
query = "SELECT table_name FROM all_tables WHERE owner = 'LEE'"
df = pd.read_sql(query, con)

#________________________________조인 쿼리문__________________________________________
#1번 2번 테이블 선택
tbl1 = 'tbl_order'
tbl2 = 'tbl_user'

#선택한 테이블에 들어가서 컬럼 전부 가져오기
qr1 = "SELECT * FROM {}".format(tbl1)
df1 = pd.read_sql(qr1, con)
cols1 = df1.columns
qr2 = "SELECT * FROM {}".format(tbl2)
df2 = pd.read_sql(qr2, con)
cols2 = df2.columns

# #_______합집합 만들기_______________

# result_union1 = set(cols1) | set(cols2) | set(cols3)
# print(result_union1)

# #_______교집합 만들기_______________

# result_union2 = ((set(cols1) & set(cols2)) | (set(cols1) & set(cols3)) | (set(cols2) & set(cols3)))
# print(result_union2)

#만들어진 세트에서 tbl2.중복 컬럼 빼주기
filter_col = cols1.difference(cols2)
inter_col = cols1.intersection(cols2)

print('##################################################')    
#선택한 테이블.컬럼 세트 만들기
inner_str1 = ''
for i in range(len(filter_col)):
    add_str = "{}.{}, ".format(tbl1, filter_col[i])
    inner_str1 = inner_str1+add_str

inner_str2 = ''
for i in range(len(cols2)):
    if i+1==len(cols2):
        add_str = "{}.{}".format(tbl2, cols2[i])
    else :
        add_str = "{}.{}, ".format(tbl2, cols2[i])
    inner_str2 = inner_str2+add_str

res_str = inner_str1+inner_str2

#테이블 조인하기(핵심: 중첩되는 컬럼 여러개 모두 조인시켜주기)
join_query = 'SELECT {} FROM {} INNER JOIN {} ON 1=1'.format(res_str, tbl1, tbl2)
df = pd.read_sql(join_query, con)
print(join_query)

# tbl_order 테이블인 경우에만 날짜 범위 적용
if tbl1 == 'tbl_order' or tbl2 == 'tbl_order':# 특정 기간 선택 (예: '2024-01-01'부터 '2024-02-01'까지의 데이터)
    start_date = input('시작날짜를 입력하세요')
    end_date = input('종료날짜를 입력하세요')
    join_query = join_query + ' WHERE {}.order_date BETWEEN TO_DATE({}, \'YYYYMMDD\') AND TO_DATE({}, \'YYYYMMDD\')'.format('tbl_order', start_date, end_date)

for i in range(len(inter_col)):
    add_query = ' AND {}.{} = {}.{}'.format(tbl1, inter_col[i], tbl2, inter_col[i])
    join_query = join_query + add_query
df = pd.read_sql(join_query, con)
print(join_query)

# 특정 테이블이 'tbl_user'인 경우 나이대별로 데이터 조회
if tbl1 == 'tbl_user' or tbl2 == 'tbl_user':
    age_group = input('원하는 나이대를 선택하세요 (20대 이하, 20대, 30대, 40대, 50대 이상, 모두): ')
    
    if age_group == '20대 이하':
        join_query += ' AND EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM user_birth) + 1 < 20'
    elif age_group == '20대':
        join_query += ' AND EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM user_birth) + 1 BETWEEN 20 AND 29'
    elif age_group == '30대':
        join_query += ' AND EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM user_birth) + 1 BETWEEN 30 AND 39'
    elif age_group == '40대':
        join_query += ' AND EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM user_birth) + 1 BETWEEN 40 AND 49'
    elif age_group == '50대 이상':
        join_query += ' AND EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM user_birth) + 1 >= 50'

#조인된 테이블에서 데이터 추출하기
base_query = 'SELECT * FROM ({}) WHERE 1=1'.format(join_query)

while True:
    col_name = input('col_name 입력하시오')
    if col_name=='':
        break
    col_val = input('col_val입력하시오')
    base_query = base_query + ' AND {}={}'.format(col_name, col_val)
df = pd.read_sql(base_query, con)
print(base_query)
print(df)

#데이터 분석
select1 = 'MENU'
select2 = 'MENU_SALE_PRICE'

menu_price_df = df[['CATE_ID', 'MENU_ID', select2]]
menu_total_price = menu_price_df.groupby(['CATE_ID', 'MENU_ID']).sum().reset_index()
menu_total_price[select1] = menu_total_price['CATE_ID'].astype(str) + '-' + menu_total_price['MENU_ID'].astype(str)

print(menu_total_price)
plt.bar(menu_total_price[select1], menu_total_price[select2])
plt.xlabel(select1)
plt.ylabel(select2)
plt.title('23년도 3월 전연령 여성 커피메뉴 판매금액 합산내역')
plt.show()

#결과물 엑셀로 저장

# 연결 닫기
con.close()


