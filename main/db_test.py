import cx_Oracle
import pandas as pd

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
    add_str = "{}.{},".format(tbl1, filter_col[i])
    inner_str1 = inner_str1+add_str
print('==============', inner_str1)

inner_str2 = ''
for i in range(len(cols2)):
    if i+1==len(cols2):
        add_str = "{}.{}".format(tbl2, cols2[i])
    else :
        add_str = "{}.{}, ".format(tbl2, cols2[i])
    inner_str2 = inner_str2+add_str
print('==============', inner_str2)


res_str = inner_str1+inner_str2
print(res_str)
print(type(res_str))

#테이블 조인하기(핵심: 중첩되는 컬럼 여러개 모두 조인시켜주기)
join_query = 'SELECT {} FROM {} INNER JOIN {} ON 1=1'.format(res_str, tbl1, tbl2)
for i in range(len(inter_col)):
    add_query = ' AND {}.{} = {}.{}'.format(tbl1, inter_col[i], tbl2, inter_col[i])
    join_query = join_query + add_query
df = pd.read_sql(join_query, con)
print(df)

#조인된 테이블에서 데이터 추출하기
base_query = 'select * from ({}) where 1=1'.format(join_query)
while True:
    col_name = input('col_name 입력하시오')
    if col_name=='':
        break
    col_val = input('col_val입력하시오')
    base_query = base_query + ' and {}={}'.format(col_name, col_val)
df = pd.read_sql(base_query, con)
print(df)

#데이터 분석


#결과물 엑셀로 저장

# 연결 닫기
con.close()


