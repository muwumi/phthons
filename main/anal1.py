import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import write_query 
from datetime import datetime

def anal1( df=()):
    qdf = df[0]
    tbl1 = df[1]
    tbl2 = df[2]
    start_date = df[3]
    end_date = df[4]

    qdf['MENU'] = qdf['CATE_ID'] + '-' + qdf['MENU_ID'].astype(str)
    
    # 현재 날짜 가져오기
    current_date = datetime.now()
    qdf['AGE'] = current_date.year - qdf['USER_BIRTH'].dt.year
    # 연령대 정의
    bins = [0, 20, 30, 40, 50, float('inf')]
    labels = ['20대 이하', '20대', '30대', '40대', '50대 이상']
    qdf['AGE_GROUP'] = pd.cut(qdf['AGE'], bins=bins, labels=labels, right=False)
    
    col_name1 = ['']
    col_name2 = ['']
    col1=''
    col2=''
    while True:
        print(['USER_SEX', 'AGE_GROUP'])
        if col1=='끝' or len(col_name1)==3:
            break
        col1 = input('col1 값을 넣어주세요').upper()
        if col1=='끝' or len(col_name1)==3:
            break
        col_name1.append(col1)
        print('____________>>>>>>>',col_name1)
    
    while True:
        print(['MENU', 'CATE_ID'])
        if col2=='끝' or len(col_name2)==3:
            break
        col2 = input('col2 값을 넣어주세요').upper()
        if col2=='끝' or len(col_name2)==3:
            break
        col_name2.append(col2)
        print('____________>>>>>>>',col_name2)
                
    #매월 초일에는 selected_col이 항상 전체 선택이 되도록
    
    plt.rcParams['font.family'] = 'MalGun Gothic'
    plt.rcParams['axes.unicode_minus'] = False
    
    result_set_list = []
    for i in range(len(col_name1)):
        for j in range(len(col_name2)):
            if col_name1[i] == '' and col_name2[j] == '':
                data = qdf['MENU_SALE_PRICE'].sum()
                title = '총 판매액'
                print(data)
                result_set_list.append([title, data])

            elif col_name1[i] == '':
                data = qdf.groupby(col_name2[j])['MENU_SALE_PRICE'].sum().reset_index()
                print(data)
                title = '{}~{} {}  MENU_SALE_PRICE'.format(start_date, end_date, col_name2[j])
                plt.bar(data[col_name2[j]], data['MENU_SALE_PRICE'])
                plt.xlabel(col_name2[j])
                plt.ylabel('MENU_SALE_PRICE')
                plt.title(title)
                plt.savefig('{}.png'.format(title))
                plt.show()
                result_set_list.append([title, data])

            elif col_name2[j] == '':
                data = qdf.groupby(col_name1[i])['MENU_SALE_PRICE'].sum().reset_index()
                print(data)
                title = '{}~{} {}  MENU_SALE_PRICE'.format(start_date, end_date, col_name1[i])
                plt.bar(data[col_name1[i]], data['MENU_SALE_PRICE'])
                plt.xlabel(col_name1[i])
                plt.ylabel('MENU_SALE_PRICE')
                plt.title(title)
                plt.savefig('{}.png'.format(title))
                plt.show()
                result_set_list.append([title, data])

            else :    
                data = qdf.groupby([col_name1[i], col_name2[j]])['MENU_SALE_PRICE'].sum().reset_index()
                print(data)
                title = '{}~{} {} {}  MENU_SALE_PRICE'.format(start_date, end_date, col_name1[i], col_name2[j])
                sns.barplot(x=col_name2[j], y='MENU_SALE_PRICE', hue=col_name1[i], data=data)
                #plt.bar(data.apply(lambda row: f"{row[col_name1[i]]} {row[col_name2[j]]}", axis=1), data['MENU_SALE_PRICE'])
                plt.xlabel(col_name2[j])
                plt.ylabel('MENU_SALE_PRICE')
                plt.title(title)
                plt.savefig('{}.png'.format(title))
                plt.show()
                result_set_list.append([title, data])
    
    return result_set_list, 
                
        

        
    '''
    x1=0(지정X),1(성별),2(세대별)
    x2=0(지정X),1(카테와메뉴별),2(카테고리별)
    f(x1, x2) = 매출(y)

    0.0 총 매출
    0.1 메뉴별 매출
    0.2 카테고리별 매출

    1.0 성별 매출
    1.1 성별&메뉴별 매출
    1.2 성별&카테고리별 매출

    2.0 세대별 매출
    2.1 세대별&메뉴별 매출
    2.2 세대별&카테고리별 매출
    '''