import gspread
from oauth2client.service_account import ServiceAccountCredentials

test = ['https://www.googleapis.com/auth/drive' , 'http://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('cred.json', test)

gs = gspread.authorize(credentials)

#doc = gs.open_by_url('https://docs.google.com/spreadsheets/d/178r_LNfWGecOdvy36ehlYTpKN_tx1wE6ecXx9VlFcF8/edit#gid=0')

#val = ws.acell('B1').value
#print(val)

#val2 = ws.acell('C1').value
#print(val2)

#val = ws.row_values('1')
#print(val)

#val = ws.col_values('1')
#print(val)

#zvals = ws.range('A2:C4')
#for val in vals:
#    print(val.value)


doc = gs.create('글로벌 직업 전문학교')

ws = doc.get_worksheet(0)

for i in range(5):
    ws.append_row([i, str(i) + 'data'])

doc.share('tkdgjs9528@gmail.com', perm_type='user', role='reader')
