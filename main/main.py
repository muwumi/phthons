from analyzing import analyze
from save_excel import save_excel
from db_connection import db_con
import sys



def main(start_day, end_day,analy_check):
    # db에 연결하기
    db = db_con(user='lee', pwd='lee')
    con = db[0]
    # data_frame의 데이터 분석
    anal_result = analyze(con=con, start_date_str=start_day, end_date_str=end_day, analy_check=analy_check)
    result_set_list = anal_result[0]
    filtered_df = anal_result[1]

    # print(result_set_list[0])
    # print('-------------------------------------')
    # print(result_set_list[2])
    # print(result_set_list)
    for result in result_set_list:
        print('&%&%', result)
    # 엑셀로 저장
    #save_excel(anal_result, start_date=start_day, end_date=end_day)
    # db접속 차단
    con.close()
    
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>끝')
    return result_set_list, filtered_df

if __name__ == "__main__":
    start_day = sys.argv[1]  # 첫 번째 인수로 시작 날짜 받기
    end_day = sys.argv[2]    # 두 번째 인수로 끝 날짜 받기
    analy_check =sys.argv[3] 
    # analy_check = '1,0,0,1,1,0,1,1,0'
    # start_day = '2023-01-01'
    # end_day = '2023-01-31'
    main(start_day, end_day, analy_check)
