import cx_Oracle

def db_con(user='', pwd=''):
    # Oracle 연결 설정

    con = cx_Oracle.connect(user, pwd, "192.168.0.127", encoding="UTF-8")

    # SQL 쿼리 실행 및 결과를 DataFrame으로 변환
    query = "SELECT table_name FROM all_tables WHERE owner = '{}'".format(user)
    return con, query