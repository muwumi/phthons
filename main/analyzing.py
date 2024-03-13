import cx_Oracle
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns


def analyze(con='', start_date_str='', end_date_str='', analy_check=''):
    analny_list = analy_check.split(',')
    print('_____________________analny_list_______________', analny_list)
    # SQL 쿼리 실행 및 결과를 DataFrame으로 변환
    qr_user = 'select * from tbl_user'
    qr_menu = 'select * from tbl_menu'
    qr_order = 'select * from tbl_ORDER'
    qr_cate = 'select * from tbl_cate'
    user_df = pd.read_sql(qr_user, con)
    menu_df = pd.read_sql(qr_menu, con).drop(columns=['MENU_PRICE', 'MENU_IMG', 'MENU_COST', 'MENU_USE'])
    order_df = pd.read_sql(qr_order, con)
    cate_df = pd.read_sql(qr_cate, con)
    # print('|||||||||||||||||||||||||||||||||||||'*10)
    # print('___________________________________________________________________')
    merged_df = pd.merge(order_df, user_df, on=['PH_NUM'], how='left')
    # print(merged_df)
    # print('___________________________________________________________________')
    merged_df = pd.merge(merged_df, menu_df, on=['CATE_ID', 'MENU_ID'], how='left')
    # print(merged_df)
    # print('___________________________________________________________________')
    merged_df = merged_df.sort_values(by=['ORDER_DATE'])
    merged_df['AGE_AT_ORDER'] = merged_df['ORDER_DATE'].dt.year - merged_df['USER_BIRTH'].dt.year
    bins = [0, 20, 30, 40, 50, float('inf')]
    labels = ['20대 이하', '20대', '30대', '40대', '50대 이상']
    merged_df['AGE_GROUP_AT_ORDER'] = pd.cut(merged_df['AGE_AT_ORDER'], bins=bins, labels=labels, right=False)
    merged_df['ORDER_DATE'] = pd.to_datetime(merged_df['ORDER_DATE'])
    # print(merged_df)

    #날짜로 필터링하기
    start_date = pd.to_datetime(start_date_str)
    end_date = pd.to_datetime(end_date_str) + pd.Timedelta(days=1)
    filtered_df = merged_df[(merged_df['ORDER_DATE'] >= start_date) & (merged_df['ORDER_DATE'] <= end_date)]
    #성별 표시하기
    filtered_df['USER_SEX'] = filtered_df['USER_SEX'].replace({0: '여자', 1: '남자'})
    #카테 이름 표시하기
    filtered_df['CATE_ID'] = filtered_df['CATE_ID'].replace({'10': '커피', '20': '논커피 라떼', '30': '스무디', '40': '티'})  
    # print(filtered_df)
# 
    #데이터 분석
    #그래프 폰트 설정
    plt.rcParams['font.family'] = 'MalGun Gothic'
    plt.rcParams['axes.unicode_minus'] = False
    result_set_list = []

        #1. 기간 내 총액 구하기
    title = '{}~{} 판매액'.format(start_date_str, end_date)
    data = filtered_df['MENU_SALE_PRICE'].sum()
    # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    # print(title)
    # print(data)
    result_set_list.append([title, data])
    
        #2. 메뉴별 총액
    if analny_list[2-2] =='1':
        title = '{}~{}메뉴별 판매액'.format(start_date_str, end_date_str)
        data = filtered_df.groupby('MENU_NAME')['MENU_SALE_PRICE'].sum().reset_index()
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(title)
        # print(data)
        result_set_list.append([title, data])
        plt.bar(data['MENU_NAME'], data['MENU_SALE_PRICE'])
        plt.xlabel('MENU_NAME')
        plt.ylabel('MENU_SALE_PRICE')
        plt.title(title)
        plt.savefig('{}.png'.format(title))
        plt.show()
            #3. 카테별 총액 비율
    if analny_list[3-2]=='1':  
        title = '{}~{}카테별 판매비율'.format(start_date_str, end_date_str)
        data = filtered_df.groupby('CATE_ID')['MENU_SALE_PRICE'].sum().reset_index()
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print(title)
        print(data)
        result_set_list.append([title, data])
        plt.pie(data['MENU_SALE_PRICE'], labels=data['CATE_ID'], autopct='%1.1f%%' )
        plt.title(title)
        plt.savefig('{}.png'.format(title))
        plt.show()
            #4. 성별 총액
    if analny_list[4-2]=='1':
        title = '{}~{} 성별 판매액'.format(start_date_str, end_date_str)          
        data = filtered_df.groupby('USER_SEX')['MENU_SALE_PRICE'].sum().reset_index()
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(title)
        # print(data)
        result_set_list.append([title, data])
        plt.bar(data['USER_SEX'], data['MENU_SALE_PRICE'])
        plt.xlabel('USER_SEX')
        plt.ylabel('MENU_SALE_PRICE')
        plt.title(title)
        plt.savefig('{}.png'.format(title))
        plt.show()
            #5. 성별&메뉴별 총액
    if analny_list[5-2] =='1':
        title = '{}~{} 성별 메뉴별 판매액'.format(start_date_str, end_date_str)          
        data = filtered_df.groupby(['USER_SEX', 'MENU_NAME'])['MENU_SALE_PRICE'].sum().reset_index()
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(title)
        # print(data)
        result_set_list.append([title, data])
        sns.barplot(x='MENU_NAME', y='MENU_SALE_PRICE', hue='USER_SEX', data=data)
        plt.xlabel('MENU_NAME')
        plt.ylabel('MENU_SALE_PRICE')
        plt.title(title)
        plt.savefig('{}.png'.format(title))
        plt.show()
            #6. 성별&카테별 총액
    if analny_list[6-2] =='1':
        title = '{}~{} 성별 카테별 판매액'.format(start_date_str, end_date_str)          
        data = filtered_df.groupby(['USER_SEX', 'CATE_ID'])['MENU_SALE_PRICE'].sum().reset_index()
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(title)
        # print(data)
        result_set_list.append([title, data])
        sns.barplot(x='CATE_ID', y='MENU_SALE_PRICE', hue='USER_SEX', data=data)
        plt.xlabel('CATE_ID')
        plt.ylabel('MENU_SALE_PRICE')
        plt.title(title)
        plt.savefig('{}.png'.format(title))
        plt.show()
            #7. 세대별 총액
    if analny_list[7-2] =='1':
        title = '{}~{} 세대별 판매액'.format(start_date_str, end_date_str)          
        data = filtered_df.groupby(['AGE_GROUP_AT_ORDER'])['MENU_SALE_PRICE'].sum().reset_index()
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(title)
        # print(data)
        result_set_list.append([title, data])
        sns.barplot(x='AGE_GROUP_AT_ORDER', y='MENU_SALE_PRICE', data=data)
        plt.xlabel('AGE_GROUP_AT_ORDER')
        plt.ylabel('MENU_SALE_PRICE')
        plt.title(title)
        plt.savefig('{}.png'.format(title))
        plt.show()    
            #8. 세대별 메뉴별 총액
    if analny_list[8-2] =='1':
        title = '{}~{} 세대별 메뉴별 판매액'.format(start_date_str, end_date_str)          
        data = filtered_df.groupby(['AGE_GROUP_AT_ORDER', 'MENU_NAME'])['MENU_SALE_PRICE'].sum().reset_index()
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(title)
        # print(data)
        result_set_list.append([title, data])
        sns.barplot(x='MENU_NAME', y='MENU_SALE_PRICE', hue='AGE_GROUP_AT_ORDER', data=data)
        plt.xlabel('MENU_NAME')
        plt.ylabel('MENU_SALE_PRICE')
        plt.title(title)
        plt.savefig('{}.png'.format(title))
        plt.show()
            #9. 세대별 카테별 총액
    if analny_list[9-2] =='1':
        title = '{}~{} 세대별 카테별 판매액'.format(start_date_str, end_date_str)          
        data = filtered_df.groupby(['AGE_GROUP_AT_ORDER', 'CATE_ID'])['MENU_SALE_PRICE'].sum().reset_index()
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(title)
        # print(data)
        result_set_list.append([title, data])
        sns.barplot(x='CATE_ID', y='MENU_SALE_PRICE', hue='AGE_GROUP_AT_ORDER', data=data)
        plt.xlabel('CATE_ID')
        plt.ylabel('MENU_SALE_PRICE')
        plt.title(title)
        plt.savefig('{}.png'.format(title))
        plt.show()
            #10. 월별분석
    if analny_list[10-2] =='1':
        title = '{}~{} 월별 카테별 판매액'.format(start_date_str, end_date_str)          
        filtered_df['MONTH'] = filtered_df['ORDER_DATE'].dt.to_period('M').dt.to_timestamp().dt.strftime('%Y-%m')
        data = filtered_df.groupby(['MONTH', 'CATE_ID'])['MENU_SALE_PRICE'].sum().reset_index()
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(title)
        # print(data)
        sns.lineplot(x='MONTH', y='MENU_SALE_PRICE', hue='CATE_ID', data=data)
        plt.xlabel('MONTH')
        plt.ylabel('MENU_SALE_PRICE')
        plt.legend()
        plt.title(title)
        plt.savefig('{}.png'.format(title))
        plt.show()
        result_set_list.append([title, data])

    
# 
    # print('_______>>>>>>>___________>>>>>>>>>>>>',len(result_set_list))
    return result_set_list, filtered_df
