import tkinter as tk
from tkinter import ttk
import sql

def goto_normalui(username,filename1):
    normal_window = tk.Tk()
    normal_window.title('期刊管理软件（第十二组） 当前登录用户：'+username)
    ww=1350
    wh=700
    wxp=int(abs(normal_window.winfo_screenwidth()-ww)/2)
    wyp=int(abs(normal_window.winfo_screenheight()-wh)/2)
    normal_window.geometry('{}x{}+{}+{}'.format(ww,wh,wxp,wyp))
    normal_window.minsize(ww,wh)
    normal_window.maxsize(ww,wh)
    normal_window.iconbitmap(filename1)
    # option code
    cb_var = tk.StringVar()
    frame_operation = tk.LabelFrame(normal_window, text='操作界面', height=700,borderwidth=10)
    tk.Label(frame_operation, text='   '+username+',欢迎使用期刊管理系统（普通用户）！请在左边栏选择你要进行的操作。',
             bg='white', font=('等线', 14), width=70, height=1).pack()
    # operation functions

    def create_frame_operation():
        for widget in frame_operation.winfo_children():
            widget.destroy()
        if cb_var.get() == '1':
            def searchC():
                results = sql.Sqloperation().inquiry_pinfo(entrytext.get())
                if not results.__len__():
                    tk.messagebox.showerror(title='信息', message='未查找到相关期刊')
                else:
                    items = tree.get_children()
                    for item in items:
                        tree.delete(item)
                    for _ in range(results.__len__()):
                        tree.insert('', 'end', values=results[_])
            frame_search = tk.Frame(frame_operation)
            frame_search.pack()
            tk.Label(frame_search, text='请输入期刊完整或部分名称:',
                     font=('等线', 14)).pack(side='left')
            entrytext = tk.Entry(frame_search, width=25, font=('等线', 14))
            entrytext.pack(side='left')
            tree = ttk.Treeview(frame_operation, show="headings", columns=(
                "name", "CN", "ISSN", "mail", "period", "location", "belong"), selectmode=tk.BROWSE)
            # 设置表格文字居中
            tree.column("name", anchor="center", width=150)
            tree.column("CN", anchor="center", width=100)
            tree.column("ISSN", anchor="center", width=70)
            tree.column("mail", anchor="center", width=70)
            tree.column("period", anchor="center", width=70)
            tree.column("location", anchor="center", width=70)
            tree.column("belong", anchor="center", width=190)
            # 设置表格头部标题
            tree.heading("name", text="期刊名称")
            tree.heading("CN", text="CN刊号")
            tree.heading("ISSN", text="ISSN")
            tree.heading("mail", text="邮发代号")
            tree.heading("period", text="出版周期")
            tree.heading("location", text="出版地")
            tree.heading("belong", text="主办单位")
            tree.pack(expand=True, fill=tk.BOTH)
            tk.Button(frame_search, text='检索',font=('等线', 14), command=searchC).pack(side='left')
        #
        if cb_var.get() == '2':
            def searchpn():
                results = sql.Sqloperation().inquiry_pbinfo(entrytext.get())
                if not results.__len__():
                    tk.messagebox.showerror(title='信息', message='未查找到已被借阅的相关期刊')
                else:
                    items = tree.get_children()
                    for item in items:
                        tree.delete(item)
                    for _ in range(results.__len__()):
                        tree.insert('', 'end', values=
                            [results[_][3],results[_][4],results[_][5],results[_][6],results[_][7],results[_][8]])
            def searchun():
                results = sql.Sqloperation().inquiry_ubinfo(username)
                if not results.__len__():
                    tk.messagebox.showerror(title='信息', message='您暂未借阅期刊')
                else:
                    items = tree.get_children()
                    for item in items:
                        tree.delete(item)
                    for _ in range(results.__len__()):
                        tree.insert('', 'end', values=results[_])
            # sub frame1
            frame21 = tk.Frame(frame_operation)
            frame21.pack()
            tk.Label(frame21, text='查询期刊被借阅情况：',font=('等线', 16)).pack(side='left')
            entrytext = tk.Entry(frame21, width=25, font=('等线', 14))
            entrytext.pack(side='left')
            tk.Button(frame21, text='检索',font=('等线', 14),command=searchpn).pack(side='left')
            # sub frame2
            frame22 = tk.Frame(frame_operation)
            tk.Label(frame22, text='查询我的借阅情况：',font=('等线', 16)).pack(side='left')
            tk.Button(frame22, text='检索',font=('等线', 14),command=searchun).pack(side='left')
            frame22.pack()
            # 列表窗口
            tree = ttk.Treeview(frame_operation, show="headings", columns=(
                "pname", "year", "roll", "stage", "bdate", "rdate"), selectmode=tk.BROWSE)
            # 设置表格文字居中
            tree.column("pname", anchor="center", width=150)
            tree.column("year", anchor="center", width=50)
            tree.column("roll", anchor="center", width=50)
            tree.column("stage", anchor="center", width=50)
            tree.column("bdate", anchor="center", width=70)
            tree.column("rdate", anchor="center", width=70)
            # 设置表格头部标题
            tree.heading("pname", text="期刊名称")
            tree.heading("year", text="年")
            tree.heading("roll", text="卷")
            tree.heading("stage", text="期")
            tree.heading("bdate", text="借阅日期")
            tree.heading("rdate", text="归还日期")
            #tree.heading("buser", text="预定用户")
            tree.pack(expand=True, fill=tk.BOTH)
        #
        if cb_var.get() == '3':
            def searchpb():
                results = sql.Sqloperation().inquiry_pbinfo(entrytext.get())
                if not results.__len__():
                    tk.messagebox.showerror(title='信息', message='未查找到已被借阅的相关期刊')
                else:
                    items = tree.get_children()
                    for item in items:
                        tree.delete(item)
                    for _ in range(results.__len__()):
                        # discard returned and booked items
                        if not results[_][9] and not results[_][8]:
                            if results[_][1] != username:
                                tree.insert('', 'end', values=
                                    [results[_][3],results[_][4],results[_][5],results[_][6],results[_][7]])
            def cbookp():
                for item in tree.selection():
                    item_text = tree.item(item,"values")
                pname=item_text[0]
                pyear=item_text[1]
                pvolume=item_text[2]
                pissue=item_text[3]
                if sql.Sqloperation().bookp(pname,username,pyear,pvolume,pissue):
                    tk.messagebox.showinfo(title='信息', message='预定成功')
                else:
                    tk.messagebox.showerror(title='信息', message='预定失败，请联系管理员')
            frame_sub = tk.Frame(frame_operation)
            frame_subs = tk.Frame(frame_sub)
            frame_sub.pack()
            frame_subs.pack()
            tk.Label(frame_subs, text='请输入已被借阅期刊完整或部分名称:',font=('等线', 14)).pack(side='left')
            entrytext = tk.Entry(frame_subs, width=25, font=('等线', 14))
            entrytext.pack(side='left')
            tk.Button(frame_subs, text='检索',font=('等线', 14),command=searchpb).pack(side='left')
            tk.Label(frame_sub, text='以下是可被预定期刊列表:',font=('等线', 14)).pack()
            # 列表窗口
            tree = ttk.Treeview(frame_operation, show="headings", columns=(
                "pname", "year", "roll", "stage", "bdate"), selectmode=tk.BROWSE)
            # 设置表格文字居中
            tree.column("pname", anchor="center", width=150)
            tree.column("year", anchor="center", width=50)
            tree.column("roll", anchor="center", width=50)
            tree.column("stage", anchor="center", width=50)
            tree.column("bdate", anchor="center", width=70)
            # 设置表格头部标题
            tree.heading("pname", text="期刊名称")
            tree.heading("year", text="年")
            tree.heading("roll", text="卷")
            tree.heading("stage", text="期")
            tree.heading("bdate", text="借阅日期")
            tree.pack(expand=True, fill=tk.BOTH)
            tk.Button(frame_operation, text='预定选定的期刊',font=('等线', 14),command=cbookp).pack(side='bottom')
        #
        if cb_var.get() == '4':
            def changepass():
                if not sql.Sqloperation().is_pass_match(username,entrytext1.get()):
                    tk.messagebox.showerror('提示信息',message='原密码错误')
                    return False
                if entrytext3.get()!=entrytext2.get():
                    tk.messagebox.showerror(title='信息', message='新密码两次输入不一致，请重试')
                    return False
                elif not sql.Sqloperation().checkpassformat(entrytext2.get()):
                    tk.messagebox.showerror('提示信息',message='密码格式不正确，不能为空以及包含空格')
                    return False
                else:
                    if sql.Sqloperation().update_user_passwd(username,entrytext2.get()):
                        tk.messagebox.showinfo('提示信息',message='修改成功')
                    else:
                        tk.messagebox.showerror('提示信息',message='修改失败')
                        return False
            tk.Label(frame_operation, text='请输入原密码:',
                     font=('等线', 14)).grid(row=1, column=1, padx=10, pady=10, ipadx=10, ipady=10)
            entrytext1 = tk.Entry(frame_operation, width=10, font=('等线', 14))
            entrytext1.grid(row=1, column=2, padx=20, pady=10, ipadx=15, ipady=1)
            tk.Label(frame_operation, text='请输入新密码:',
                     font=('等线', 14)).grid(row=2, column=1, padx=10, pady=10, ipadx=10, ipady=10)
            entrytext2 = tk.Entry(frame_operation, width=10, font=('等线', 14))
            entrytext2.grid(row=2, column=2, padx=20, pady=10, ipadx=15, ipady=1)
            tk.Label(frame_operation, text='请确认新密码:',
                     font=('等线', 14)).grid(row=3, column=1, padx=10, pady=10, ipadx=10, ipady=10)
            entrytext3 = tk.Entry(frame_operation, width=10, font=('等线', 14))
            entrytext3.grid(row=3, column=2, padx=20, pady=10, ipadx=15, ipady=1)
            tk.Button(frame_operation, text='确定修改',
                      font=('等线', 14),command=changepass).grid(row=4, column=2, padx=10, pady=10, ipadx=10, ipady=1)
        #
        if cb_var.get() == '5':
            def search_content_bykw():
                results = sql.Sqloperation().inquiry_content_by_kw(entrytext3.get())
                if not results.__len__():
                    tk.messagebox.showerror(title='信息', message='未查找到相关内容')
                else:
                    items = tree.get_children()
                    for item in items:
                        tree.delete(item)
                    for _ in range(results.__len__()):
                        tree.insert('', 'end', values=results[_])
            def search_content_byau():
                results = sql.Sqloperation().inquiry_content_by_au(entrytext1.get())
                if not results.__len__():
                    tk.messagebox.showerror(title='信息', message='未查找到相关内容')
                else:
                    items = tree.get_children()
                    for item in items:
                        tree.delete(item)
                    for _ in range(results.__len__()):
                        tree.insert('', 'end', values=results[_])
            def search_content_bytt():
                results = sql.Sqloperation().inquiry_content_by_tt(entrytext2.get())
                if not results.__len__():
                    tk.messagebox.showerror(title='信息', message='未查找到相关内容')
                else:
                    items = tree.get_children()
                    for item in items:
                        tree.delete(item)
                    for _ in range(results.__len__()):
                        tree.insert('', 'end', values=results[_])
            frame_search1 = tk.Frame(frame_operation)
            frame_search1.pack()
            frame_search2 = tk.Frame(frame_operation)
            frame_search2.pack()
            frame_search3 = tk.Frame(frame_operation)
            frame_search3.pack()
            frame_tree = tk.Frame(frame_operation)
            frame_tree.pack()
            tk.Label(frame_search1, text='请输入作者名:',font=('等线', 14)).pack(side='left')
            entrytext1 = tk.Entry(frame_search1, width=25, font=('等线', 14))
            entrytext1.pack(side='left')
            tk.Label(frame_search2, text='请输入文章标题:',font=('等线', 14)).pack(side='left')
            entrytext2 = tk.Entry(frame_search2, width=25, font=('等线', 14))
            entrytext2.pack(side='left')
            tk.Label(frame_search3, text='请输入关键词:',font=('等线', 14)).pack(side='left')
            entrytext3 = tk.Entry(frame_search3, width=25, font=('等线', 14))
            entrytext3.pack(side='left')
            tk.Button(frame_search1, text='按作者名检索',font=('等线', 14), command=search_content_byau).pack(side='left')
            tk.Button(frame_search2, text='按文章标题检索',font=('等线', 14), command=search_content_bytt).pack(side='left')
            tk.Button(frame_search3, text='按关键词检索',font=('等线', 14), command=search_content_bykw).pack(side='left')
            tree = ttk.Treeview(frame_tree,show="headings", columns=(
                "id", "pname", "year", "volume", "issue", "title", "author","pages","kw1","kw2","kw3","kw4","kw5"), selectmode=tk.BROWSE)
            # 设置表格文字居中
            tree.column("id", anchor="center", width=50)
            tree.column("pname", anchor="center", width=100)
            tree.column("year", anchor="center", width=70)
            tree.column("volume", anchor="center", width=50)
            tree.column("issue", anchor="center", width=50)
            tree.column("title", anchor="center", width=100)
            tree.column("author", anchor="center", width=100)
            tree.column("pages", anchor="center", width=70)
            tree.column("kw1", anchor="center", width=90)
            tree.column("kw2", anchor="center", width=90)
            tree.column("kw3", anchor="center", width=90)
            tree.column("kw4", anchor="center", width=90)
            tree.column("kw5", anchor="center", width=90)
            # 设置表格头部标题
            tree.heading("id", text="序号")
            tree.heading("pname", text="期刊名称")
            tree.heading("year", text="年")
            tree.heading("volume", text="卷")
            tree.heading("issue", text="期")
            tree.heading("title", text="文章标题")
            tree.heading("author", text="作者")
            tree.heading("pages", text="页码")
            tree.heading("kw1", text="关键词1")
            tree.heading("kw2", text="关键词2")
            tree.heading("kw3", text="关键词3")
            tree.heading("kw4", text="关键词4")
            tree.heading("kw5", text="关键词5")
            tree.pack(expand=True, fill=tk.BOTH)
            # scrool bar
    ##
    frame_option = tk.LabelFrame(normal_window, text='选择要进行的操作', height=1000,borderwidth=10)
    frame_option.grid(row=1, column=1, padx=10, pady=10, ipadx=10, ipady=10,sticky="n" + "s" + "w" + "e")
    # 分割线
    tk.Canvas(normal_window, bg='black', height=wh-50, width=1).grid(
        row=1, column=2, padx=10, pady=10, ipadx=1, ipady=10)
    frame_button = tk.Frame(normal_window)
    # 按顺序放置，不能移动下面语句的顺序
    frame_operation.grid(row=1, column=3, padx=10, pady=10, ipadx=10, ipady=10,sticky="n" + "s" + "w" + "e")
    tk.Radiobutton(frame_option, text='期刊信息查询', variable=cb_var,
                   value='1', font=('等线', 16), command=create_frame_operation).grid(column=1, row=1, pady=10)
    tk.Radiobutton(frame_option, text='期刊内容查询', variable=cb_var,
                   value='5', font=('等线', 16), command=create_frame_operation).grid(column=1, row=2, pady=10)
    tk.Radiobutton(frame_option, text='期刊借阅查询', variable=cb_var,
                   value='2', font=('等线', 16), command=create_frame_operation).grid(column=1, row=3, pady=10)
    tk.Radiobutton(frame_option, text='预定期刊       ', variable=cb_var,
                   value='3', font=('等线', 16), command=create_frame_operation).grid(column=1, row=4, pady=10)
    tk.Radiobutton(frame_option, text='修改密码       ', variable=cb_var,
                   value='4', font=('等线', 16), command=create_frame_operation).grid(column=1, row=5, pady=10)
    normal_window.mainloop()
