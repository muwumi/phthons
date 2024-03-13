from analyzing import analyze
from save_excel import save_excel
from db_connection import db_con

#db에 연결하기
db = db_con(user='lee', pwd='lee')
con = db[0]
'''#연결된 db를 통해 data_frame 생성
df = write_query(db)
start_date = df[3]
end_date = df[4]'''
#data_frame의 데이터 분석
'''anal1_result = anal1(df, con)'''
start_day = '2023-01-01'
end_day = '2024-01-31'
analy_check='1,0,1,0,1,0,1,0,1'
anal_result = analyze(con=con, start_date_str=start_day, end_date_str=end_day, analy_check=analy_check)
# #엑셀로 저장
save_excel(anal_result, start_date=start_day, end_date=end_day)
#db접속 차단
con.close()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>끝')
