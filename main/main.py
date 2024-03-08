from write_query import write_query
from anal1 import anal1
from save_excel import save_excel

df = write_query()
start_date = df[3]
end_date = df[4]
anal1_result = anal1(df)
save_excel(anal1_result, start_date, end_date)
