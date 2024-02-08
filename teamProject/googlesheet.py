import gspread
from google.oauth2.service_account import Credentials

# json 파일이 위치한 경로를 값으로 줘야 합니다.
json_file_path = r"D:\LSH\workspace\phthons\cred.json"
credentials = Credentials.from_service_account_file(json_file_path, scopes=['https://www.googleapis.com/auth/spreadsheets'])

# 스프레드시트 열기
def open_spreadsheet(url):
    gc = gspread.authorize(credentials)
    spreadsheet = gc.open_by_url(url)
    return spreadsheet

# 시트 업데이트
def update_worksheet(spreadsheet, sheet_name, values, range_name='A1'):
    worksheet = spreadsheet.worksheet(sheet_name)
    
    # values를 리스트의 리스트로 변환
    values_list = [[values]]

    # update 메소드의 시그니처 변경에 따라 named arguments 사용
    worksheet.update(values=values_list, range_name=range_name)

# 새로운 스프레드시트 생성
def create_spreadsheet(title):
    gc = gspread.authorize(credentials)
    spreadsheet = gc.create(title)
    print(f"스프레드시트가 성공적으로 생성되었습니다. ID: {spreadsheet.id}")
    return spreadsheet

# 시트1 업데이트
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/178r_LNfWGecOdvy36ehlYTpKN_tx1wE6ecXx9VlFcF8/edit?usp=sharing'
spreadsheet = open_spreadsheet(spreadsheet_url)
update_worksheet(spreadsheet, "시트1", '자동화 끝!')
create_spreadsheet('새로운 시트')

