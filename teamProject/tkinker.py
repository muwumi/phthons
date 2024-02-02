import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Tkinter 창 생성
window = tk.Tk()
window.title("데이터프레임 뷰어")

# 데이터프레임을 표시할 Treeview 위젯 생성
tree = ttk.Treeview(window)
tree["columns"] = tuple(subset_df.columns)

# 열 제목 설정
for column in subset_df.columns:
    tree.heading(column, text=column)

# Treeview에 데이터 삽입
for index, row in subset_df.iterrows():
    tree.insert("", "end", values=tuple(row))

# Treeview를 창에 적절히 배치
tree.pack(expand=True, fill="both")

# 행의 수를 보여줄 레이블 생성
label = tk.Label(window, text=str(len(subset_df)) + '개')
label.pack()

# Tkinter 이벤트 루프 실행
window.mainloop()


