import gspread

# json 파일이 위치한 경로를 값으로 줘야 합니다.
json_file_path = r"D:\LSH\workspace\phthons\cred.json"
gc = gspread.service_account(json_file_path)
spreadsheet_url = "https://docs.google.com/spreadsheets/d/178r_LNfWGecOdvy36ehlYTpKN_tx1wE6ecXx9VlFcF8/edit?usp=sharing"
doc = gc.open_by_url(spreadsheet_url)

worksheet = doc.worksheet("시트1")
worksheet.update('a1','자동화 끝!')