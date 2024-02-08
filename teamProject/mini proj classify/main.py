import opt
import scroller
import crawling
import analyzing
import mailing
import file_saving

'''
모든 메서드의 결과값은 튜플로 반환 : 데이터를 복수 이상 반환하기
'''
#________________________________________웹에 접속_______________________________________
web_setting_result = opt.web_setting()
(browser, ) = web_setting_result

#__________________________________________크롤링________________________________________
    #카테고리 선택
cate_result = crawling.choose_category(browser)
(get_url_exc_page , input_category) = cate_result

    #스크롤 내리기
scroller.scroll_down_max(browser)
    #크롤링
crawl_result = crawling.crawl(browser, get_url_exc_page, input_category)
(data_result_2d , base_path , csv_file_name , data_num) = crawl_result
    #데이터를 csv 파일로 저장
csv_file_name = '{}{}개.csv'.format(input_category, data_num)
file_saving.csv_save(base_path, csv_file_name, data_result_2d)
    #데이터를 구글스프레드에 저장
(position, spreadsheet_url) = ('A1', r'https://docs.google.com/spreadsheets/d/178r_LNfWGecOdvy36ehlYTpKN_tx1wE6ecXx9VlFcF8/edit?usp=sharing')
file_saving.gspread_fx(spreadsheet_url=spreadsheet_url, position=position , data_result_2d=data_result_2d)

# #___________________________________________데이터 분석___________________________________
#     #데이터 분석하기
# analyze = analyzing.data_analyze(base_path, csv_file_name, input_category, data_num)
# (csv_data_frame , graph_list) = analyze
#     #엑셀로 저장
# exc_save = file_saving.exc_save(input_category, base_path, data_num, csv_data_frame, graph_list)
# (excel_file_name_with_graph, ) = exc_save

# #___________________________________________메일링________________________________________
# mailing.send_email(browser, base_path, excel_file_name_with_graph)

# #___________________________________________완료 메세지____________________________________
# print('프로그램 구동이 완료되었습니다.')
