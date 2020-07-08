import tkinter as tk
from tkinter import ttk
import sql
def goto_adminui(aname):
    admin_window = tk.Tk()
    admin_window.title('期刊管理软件（第十二组） 当前登录：'+aname)
    ww=1350
    wh=700
    wxp=int(abs(admin_window.winfo_screenwidth()-ww)/2)
    wyp=int(abs(admin_window.winfo_screenheight()-wh)/2)
    admin_window.geometry('{}x{}+{}+{}'.format(ww,wh,wxp,wyp))
    admin_window.minsize(ww,wh)
    admin_window.maxsize(ww,wh)
    admin_window.iconbitmap('12.ico')
    cb_var = tk.StringVar()

    frame_operation = tk.LabelFrame(admin_window, text='操作界面', height=700,borderwidth=10)

    tk.Label(frame_operation, text='   '+aname+',欢迎使用期刊管理系统（管理员）！请在左边栏选择你要进行的操作。',
             bg='white', font=('等线', 14), width=70, height=1).pack()

    def create_frame_operation():
        for widget in frame_operation.winfo_children():
            widget.destroy()
        # inquiry periodical info
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
            tk.Label(frame_search, text='请输入期刊完整或部分名称:',font=('等线', 14)).pack(side='left')
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
        # inquiry periodical borrowed info
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
                        tree.insert('', 'end', values=results[_])
            def searchun():
                if not entrytextuname.get():
                    tk.messagebox.showerror(title='信息', message='工号不能为空！')
                    return
                results = sql.Sqloperation().inquiry_ubinfo(entrytextuname.get())
                if not results.__len__():
                    tk.messagebox.showerror(title='信息', message='该用户暂未借阅期刊')
                else:
                    items = tree.get_children()
                    for item in items:
                        tree.delete(item)
                    for _ in range(results.__len__()):
                        tree.insert('', 'end', values=results[_])
            # sub frame1
            frame21 = tk.Frame(frame_operation)
            frame21.pack()
            tk.Label(frame21, text='要查询的期刊名：',font=('等线', 16)).pack(side='left')
            entrytext = tk.Entry(frame21, width=25, font=('等线', 14))
            entrytext.pack(side='left')
            tk.Button(frame21, text='检索',font=('等线', 14),command=searchpn).pack(side='left')
            # sub frame2
            frame22 = tk.Frame(frame_operation)
            tk.Label(frame22, text='要查询的工号：',font=('等线', 16)).pack(side='left')
            entrytextuname = tk.Entry(frame22, width=25, font=('等线', 14))
            entrytextuname.pack(side='left')
            tk.Button(frame22, text='检索',font=('等线', 14),command=searchun).pack(side='left')
            frame22.pack()
            # 列表窗口
            tree = ttk.Treeview(frame_operation, show="headings", columns=(
                "bid","uid", "uname", "pname", "year", "roll", "stage", "bdate", "rdate","buser"), selectmode=tk.BROWSE)
            # 设置表格文字居中
            tree.column("bid", anchor="center", width=50)
            tree.column("uid", anchor="center", width=100)
            tree.column("uname", anchor="center", width=100)
            tree.column("pname", anchor="center", width=150)
            tree.column("year", anchor="center", width=50)
            tree.column("roll", anchor="center", width=50)
            tree.column("stage", anchor="center", width=50)
            tree.column("bdate", anchor="center", width=70)
            tree.column("rdate", anchor="center", width=70)
            tree.column("buser", anchor="center", width=70)
            # 设置表格头部标题
            tree.heading("bid", text="序号")
            tree.heading("uid", text="工号")
            tree.heading("uname", text="用户名")
            tree.heading("pname", text="期刊名称")
            tree.heading("year", text="年")
            tree.heading("roll", text="卷")
            tree.heading("stage", text="期")
            tree.heading("bdate", text="借阅日期")
            tree.heading("rdate", text="归还日期")
            tree.heading("buser", text="预定用户")
            tree.pack(expand=True, fill=tk.BOTH)
        # borrow managment
        if cb_var.get() == '3':
            def create_frame3sub_operation():
                for widget in frame32.winfo_children():
                    widget.destroy()
                if var3.get() == '1':
                    # lent
                    def searchrp():
                        resultsr = sql.Sqloperation().inquiry_register(entrytext.get())
                        resultsb = sql.Sqloperation().inquiry_pbinfo(entrytext.get())
                        discardrecord=[]
                        if not resultsr.__len__():
                            tk.messagebox.showerror(title='信息', message='未查找到相关期刊')
                            return
                        if resultsb.__len__():
                            "there is record in borrow table"
                            for r in range(resultsr.__len__()):
                                for b in range(resultsb.__len__()):
                                    if resultsr[r][1]==resultsb[b][3] and resultsr[r][2]==resultsb[b][4] and resultsr[r][3]==resultsb[b][5] and resultsr[r][4]==resultsb[b][6] and not resultsb[b][8]:
                                        discardrecord.append(r)
                                    """ if not resultsb[b][8]:
                                        "not returned"
                                        discardrecord.append(r) """
                        items = tree.get_children()
                        for item in items:
                            tree.delete(item)
                        for _ in range(resultsr.__len__()):
                            if not discardrecord.count(_):
                                tree.insert('', 'end', values=resultsr[_])
                    def lentrp():
                        itemexist=False
                        for item in tree.selection():
                            itemexist=True
                            item_text = tree.item(item,"values")
                        if not itemexist:
                            tk.messagebox.showerror(title='信息', message='借出失败，请先用鼠标选中一本期刊')
                            return
                        pname=item_text[1]
                        pyear=int(item_text[2])
                        pvolume=int(item_text[3])
                        pissue=int(item_text[4])
                        if not entrytextuname.get():
                            tk.messagebox.showerror(title='信息', message='借出失败，请输入借出工号名')
                            return
                        elif not sql.Sqloperation().checkidformat(entrytextuname.get()):
                            tk.messagebox.showerror(title='信息', message='工号格式（1字母+8数字）不正确，请重试')
                            return
                        # if the booking id match
                        resultsb = sql.Sqloperation().inquiry_pbinfo(entrytext.get())
                        matchedrecord=[None]*10
                        for b in range(resultsb.__len__()):
                            if pname==resultsb[b][3] and pyear==resultsb[b][4] and pvolume==resultsb[b][5] and pissue==resultsb[b][6]:
                                matchedrecord=resultsb[b]
                        if matchedrecord[9] and matchedrecord[9]!=entrytextuname.get():
                            tk.messagebox.showerror(title='信息', message='借出失败，该期刊已被其他用户预定')
                            return
                        if sql.Sqloperation().lend(entrytextuname.get(),pname,pyear,pvolume,pissue):
                            tk.messagebox.showinfo(title='信息', message='借出成功')
                        else:
                            tk.messagebox.showerror(title='信息', message='借出失败，请重试')
                    frame_search = tk.Frame(frame32)
                    frame_search.pack()
                    tk.Label(frame_search, text='请输入期刊完整或部分名称:',font=('等线', 14)).pack(side='left')
                    entrytext = tk.Entry(frame_search, width=25, font=('等线', 14))
                    entrytext.pack(side='left')
                    
                    tk.Button(frame_search, text='检索',font=('等线', 14),command=searchrp).pack(side='left')
                    tree = ttk.Treeview(frame32, show="headings", columns=(
                        "id","name",  "year", "roll", "stage"), selectmode=tk.BROWSE)
                    # 设置表格文字居中
                    tree.column("id", anchor="center", width=100)
                    tree.column("name", anchor="center", width=150)
                    tree.column("year", anchor="center", width=50)
                    tree.column("roll", anchor="center", width=50)
                    tree.column("stage", anchor="center", width=50)
                    # 设置表格头部标题
                    tree.heading("name", text="期刊名称")
                    tree.heading("id", text="期刊ID")
                    tree.heading("year", text="年")
                    tree.heading("roll", text="卷")
                    tree.heading("stage", text="期")
                    tree.pack(expand=True, fill=tk.BOTH)
                    frame_lent = tk.Frame(frame32)
                    frame_lent.pack(side='bottom')
                    tk.Label(frame_lent, text='请输入借阅工号:',font=('等线', 14)).pack(side='left')
                    entrytextuname = tk.Entry(frame_lent, width=25, font=('等线', 14))
                    entrytextuname.pack(side='left')
                    tk.Button(frame_lent, text='借出期刊',font=('等线', 14),command=lentrp).pack(side='left')
                else:
                    #return
                    def searchbp():
                        results = sql.Sqloperation().inquiry_pbinfo(entrytext.get())
                        if not results.__len__():
                            tk.messagebox.showerror(title='信息', message='未查找到已被借阅的相关期刊')
                        else:
                            items = tree.get_children()
                            for item in items:
                                tree.delete(item)
                            for _ in range(results.__len__()):
                                if not results[_][8]:
                                    tree.insert('', 'end', values=results[_])
                    def returnbp():
                        itemexist=False
                        for item in tree.selection():
                            itemexist=True
                            item_text = tree.item(item,"values")
                        if not itemexist:
                            tk.messagebox.showerror(title='信息', message='归还失败，请先用鼠标选中一条记录')
                            return
                        pname=item_text[3]
                        pyear=item_text[4]
                        pvolume=item_text[5]
                        pissue=item_text[6]
                        if sql.Sqloperation().returnp(pname,pyear,pvolume,pissue):
                            tk.messagebox.showinfo(title='信息', message='归还成功')
                        else:
                            tk.messagebox.showerror(title='信息', message='归还失败，请重试')
                    frame_search = tk.Frame(frame32)
                    frame_search.pack()
                    tk.Label(frame_search, text='请输入已被借阅期刊完整或部分名称:',font=('等线', 14)).pack(side='left')
                    entrytext = tk.Entry(frame_search, width=25, font=('等线', 14))
                    entrytext.pack(side='left')
                    tk.Button(frame_search, text='检索',font=('等线', 14),command=searchbp).pack(side='left')
                    tree = ttk.Treeview(frame32, show="headings", columns=(
                        "bid","uid", "uname", "pname", "year", "roll", "stage", "bdate", "rdate","buser"), selectmode=tk.BROWSE)
                    # 设置表格文字居中
                    tree.column("bid", anchor="center", width=50)
                    tree.column("uid", anchor="center", width=100)
                    tree.column("uname", anchor="center", width=100)
                    tree.column("pname", anchor="center", width=150)
                    tree.column("year", anchor="center", width=50)
                    tree.column("roll", anchor="center", width=50)
                    tree.column("stage", anchor="center", width=50)
                    tree.column("bdate", anchor="center", width=70)
                    tree.column("rdate", anchor="center", width=70)
                    tree.column("buser", anchor="center", width=70)
                    # 设置表格头部标题
                    tree.heading("bid", text="序号")
                    tree.heading("uid", text="工号")
                    tree.heading("uname", text="用户名")
                    tree.heading("pname", text="期刊名称")
                    tree.heading("year", text="年")
                    tree.heading("roll", text="卷")
                    tree.heading("stage", text="期")
                    tree.heading("bdate", text="借阅日期")
                    tree.heading("rdate", text="归还日期")
                    tree.heading("buser", text="预定用户")
                    tree.pack(expand=True, fill=tk.BOTH)
                    tk.Button(frame32, text='归还期刊',font=('等线', 14),command=returnbp).pack(side='bottom')
            frame31 = tk.Frame(frame_operation)
            frame31.pack()
            frame32 = tk.Frame(frame_operation)
            frame32.pack()
            var3=tk.StringVar()
            tk.Radiobutton(frame31, text='期刊借阅管理', variable=var3,
                   value='1', font=('等线', 16), command=create_frame3sub_operation).pack(side='left')
            tk.Radiobutton(frame31, text='期刊归还管理', variable=var3,
                   value='2', font=('等线', 16), command=create_frame3sub_operation).pack(side='left')
        # add catalog
        if cb_var.get() == '4':
            def catalogc():
                pname=entrytext1.get()
                pcn=entrytext2.get()
                pisn=entrytext3.get()
                pmail=entrytext4.get()
                pper=entrytext5.get()
                ploc=entrytext6.get()
                ppress=entrytext7.get()
                if sql.Sqloperation().checkinputcatalog(pcn,pisn,pmail,pper):
                    tk.messagebox.showerror(title='信息', message=sql.Sqloperation().checkinputcatalog(pcn,pisn,pmail,pper))
                    return
                if pname and pcn and pisn and pmail and pper and ploc and ppress:
                    comfirmc = tk.messagebox.askyesno('确认',message=r"""期刊名称:{}
CN刊号:{}
ISSN:{}
邮发代码:{}
出版周期:{}
出版地:{}
主办单位:{}
信息是否无误？
                    """.format(pname,pcn,pisn,pmail,pper,ploc,ppress))
                    if comfirmc:
                        if sql.Sqloperation().addcatalog(pname,pcn,pisn,pmail,pper,ploc,ppress):
                            tk.messagebox.showinfo(title='信息', message='目录登记成功')
                        else:
                            tk.messagebox.showerror(title='信息', message='目录登记失败，请重试')
                    else:return
                else:
                    tk.messagebox.showerror(title='信息', message='不允许留空！')
            tk.Label(frame_operation, text='期刊名称:',font=('等线', 14)).grid(row=1, column=1,padx=10,pady=10)
            entrytext1 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext1.grid(row=1, column=2)
            tk.Label(frame_operation, text='CN刊号:',font=('等线', 14)).grid(row=2, column=1,padx=10,pady=10)
            entrytext2 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext2.grid(row=2, column=2)
            tk.Label(frame_operation, text='ISSN:',font=('等线', 14)).grid(row=3, column=1,padx=10,pady=10)
            entrytext3 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext3.grid(row=3, column=2)
            tk.Label(frame_operation, text='邮发代码:',font=('等线', 14)).grid(row=4, column=1,padx=10,pady=10)
            entrytext4 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext4.grid(row=4, column=2)
            tk.Label(frame_operation, text='出版周期:',font=('等线', 14)).grid(row=5, column=1,padx=10,pady=10)
            entrytext5 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext5.grid(row=5, column=2)
            tk.Label(frame_operation, text='出版地:',font=('等线', 14)).grid(row=6, column=1,padx=10,pady=10)
            entrytext6 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext6.grid(row=6, column=2)
            tk.Label(frame_operation, text='主办单位:',font=('等线', 14)).grid(row=7, column=1,padx=10,pady=10)
            entrytext7 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext7.grid(row=7, column=2)
            tk.Button(frame_operation, text='登记期刊目录',font=('等线', 14),command=catalogc).grid(row=8, column=2,pady=10)
        #register
        if cb_var.get() == '5':
            def cregister():
                pname=entrytext1.get()
                pyear=entrytext2.get()
                pvolume=entrytext3.get()
                pissue=entrytext4.get()
                if sql.Sqloperation().checkinputregister(pyear):
                    tk.messagebox.showerror(title='信息', message=sql.Sqloperation().checkinputregister(pyear))
                    return
                if pname and pyear and pvolume and pissue:
                    try:
                        pyearn=int(pyear)
                    except:
                        tk.messagebox.showerror(title='信息', message='“年”的格式不符合要求')
                        return
                    try:
                        pvolumen=int(pvolume)
                    except:
                        tk.messagebox.showerror(title='信息', message='“卷”的格式不符合要求')
                        return
                    try:
                        pissuen=int(pissue)
                    except:
                        tk.messagebox.showerror(title='信息', message='“期”的格式不符合要求')
                        return
                    comfirmc = tk.messagebox.askyesno('确认',message=r"""期刊名称:{}
年:{}
卷:{}
期:{}
信息是否无误？
                    """.format(pname,pyear,pvolume,pissue))
                    if comfirmc:
                        if sql.Sqloperation().register(pname,pyear,pvolume,pissue):
                            tk.messagebox.showinfo(title='信息', message='期刊注册成功')
                        else:
                            tk.messagebox.showerror(title='信息', message='期刊注册失败，请重试')
                    else:return
                else:
                    tk.messagebox.showerror(title='信息', message='不允许留空！')
            tk.Label(frame_operation, text='期刊名称:',font=('等线', 14)).grid(row=1, column=1,padx=10,pady=10)
            entrytext1 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext1.grid(row=1, column=2)
            tk.Label(frame_operation, text='期刊年份:',font=('等线', 14)).grid(row=2, column=1,padx=10,pady=10)
            entrytext2 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext2.grid(row=2, column=2)
            tk.Label(frame_operation, text='期刊卷号:',font=('等线', 14)).grid(row=3, column=1,padx=10,pady=10)
            entrytext3 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext3.grid(row=3, column=2)
            tk.Label(frame_operation, text='期刊期号:',font=('等线', 14)).grid(row=4, column=1,padx=10,pady=10)
            entrytext4 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext4.grid(row=4, column=2)
            tk.Button(frame_operation, text='期刊入库',font=('等线', 14),command=cregister).grid(row=5, column=2,pady=10)
        # add content
        if cb_var.get() == '6':
            def contentc():
                pname=entrytext1.get()
                pyear=entrytext2.get()
                pvolume=entrytext3.get()
                pissue=entrytext4.get()
                ptitle=entrytext5.get()
                pauther=entrytext6.get()
                ppage=entrytext8.get()
                if pname and pyear and pvolume and pissue and ptitle and pauther and entrytext7.get() and ppage:
                    if sql.Sqloperation().checkinputcontent(pyear,ppage):
                        tk.messagebox.showerror(title='信息', message=sql.Sqloperation().checkinputcontent(pyear,ppage))
                        return
                    if entrytext7.get().count(';')>entrytext7.get().count('；'):
                        opkws=entrytext7.get().split(";")
                    else:
                        opkws=entrytext7.get().split("；")
                    npkws=[None,None,None,None,None]
                    for _ in range(len(opkws)):
                        npkws[_]=opkws[_]
                    try:
                        pyearn=int(pyear)
                    except:
                        tk.messagebox.showerror(title='信息', message='“年”的格式不符合要求')
                        return
                    try:
                        pvolumen=int(pvolume)
                    except:
                        tk.messagebox.showerror(title='信息', message='“卷”的格式不符合要求')
                        return
                    try:
                        pissuen=int(pissue)
                    except:
                        tk.messagebox.showerror(title='信息', message='“期”的格式不符合要求')
                        return
                    comfirmc = tk.messagebox.askyesno('确认',message=r"""期刊名称:{}
年:{}
卷:{}
期:{}
文章标题:{}
作者姓名:{}
所在页码:{}
关键词1:{}
关键词2:{}
关键词3:{}
关键词4:{}
关键词5:{}
信息是否无误？
                        """.format(pname,pyear,pvolume,pissue,ptitle,pauther,ppage,npkws[0],npkws[1],npkws[2],npkws[3],npkws[4]))
                    if comfirmc:
                        if sql.Sqloperation().addcontent(pname,pyear,pvolume,pissue,ptitle,pauther,ppage,npkws[0],npkws[1],npkws[2],npkws[3],npkws[4]):
                            tk.messagebox.showinfo(title='信息', message='期刊内容登记成功')
                        else:
                            tk.messagebox.showerror(title='信息', message='期刊内容登记失败，请重试')
                    else:return
                else:
                    tk.messagebox.showerror(title='信息', message='不允许留空！')
            tk.Label(frame_operation, text='期刊名称:',font=('等线', 14)).grid(row=1, column=1,padx=10,pady=10)
            entrytext1 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext1.grid(row=1, column=2)
            tk.Label(frame_operation, text='年:',font=('等线', 14)).grid(row=2, column=1,padx=10,pady=10)
            entrytext2 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext2.grid(row=2, column=2)
            tk.Label(frame_operation, text='卷:',font=('等线', 14)).grid(row=3, column=1,padx=10,pady=10)
            entrytext3 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext3.grid(row=3, column=2)
            tk.Label(frame_operation, text='期:',font=('等线', 14)).grid(row=4, column=1,padx=10,pady=10)
            entrytext4 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext4.grid(row=4, column=2)
            tk.Label(frame_operation, text='文章标题:',font=('等线', 14)).grid(row=5, column=1,padx=10,pady=10)
            entrytext5 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext5.grid(row=5, column=2)
            tk.Label(frame_operation, text='作者姓名:',font=('等线', 14)).grid(row=6, column=1,padx=10,pady=10)
            entrytext6 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext6.grid(row=6, column=2)
            tk.Label(frame_operation, text='所在页码(xx~xx)',font=('等线', 14)).grid(row=7, column=1,padx=10,pady=10)
            entrytext8 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext8.grid(row=7, column=2)
            tk.Label(frame_operation, text='关键词1-5（使用;分割）：',font=('等线', 14)).grid(row=8, column=1,padx=10,pady=10)
            entrytext7 = tk.Entry(frame_operation, width=40, font=('等线', 14))
            entrytext7.grid(row=8, column=2)
            tk.Button(frame_operation, text='登记期刊内容',font=('等线', 14),command=contentc).grid(row=9, column=2,pady=10)
        # add subscription
        if cb_var.get() == '7':
            def addsub():
                pname=entrytext1.get()
                syear=entrytext2.get()
                pmail=entrytext3.get()
                if pname and pmail and syear:
                    if sql.Sqloperation().checkinputsub(pmail,syear):
                        tk.messagebox.showerror(title='信息', message=sql.Sqloperation().checkinputsub(pmail,syear))
                        return
                    try:
                        syearn=int(syear)
                    except:
                        tk.messagebox.showerror(title='信息', message='“征订年份”的格式不符合要求')
                        return
                    comfirmc = tk.messagebox.askyesno('确认',message=r"""期刊名称:{}
邮发代码:{}
征订年份:{}
信息是否无误？
                        """.format(pname,pmail,syear))
                    if comfirmc:
                        if sql.Sqloperation().subscript(pname,pmail,syear):
                            tk.messagebox.showinfo(title='信息', message='添加征订成功')
                        else:
                            tk.messagebox.showerror(title='信息', message='添加征订失败，请重试')
                    else:return
                else:
                    tk.messagebox.showerror(title='信息', message='不允许留空！')
            def getsub():
                results=sql.Sqloperation().inquirysubscription()
                items = tree.get_children()
                for item in items:
                    tree.delete(item)
                for _ in range(results.__len__()):
                        tree.insert('', 'end', values=results[_])
            def delsubc():
                itemexist=False
                for item in tree.selection():
                    itemexist=True
                    item_text = tree.item(item,"values")
                if not itemexist:
                    tk.messagebox.showerror(title='信息', message='删除失败，请先用鼠标选中一条内容')
                    return
                pname=item_text[0]
                pmail=item_text[1]
                syear=item_text[2]
                if not tk.messagebox.askyesno('删除确认',message='确定删除选定的内容？'):return
                if sql.Sqloperation().delsub(pname,pmail,syear):
                    tk.messagebox.showinfo(title='信息', message='删除成功')
                else:
                    tk.messagebox.showerror(title='信息', message='删除失败')
            tk.Label(frame_operation, text='期刊名称:',font=('等线', 14)).grid(row=1, column=1,padx=10,pady=10)
            entrytext1 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext1.grid(row=1, column=2)
            tk.Label(frame_operation, text='邮发代号:',font=('等线', 14)).grid(row=2, column=1,padx=10,pady=10)
            entrytext3 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext3.grid(row=2, column=2)
            tk.Label(frame_operation, text='征订年份:',font=('等线', 14)).grid(row=3, column=1,padx=10,pady=10)
            entrytext2 = tk.Entry(frame_operation, width=25, font=('等线', 14))
            entrytext2.grid(row=3, column=2)
            tk.Button(frame_operation, text='添加至征订清单',font=('等线', 14),command=addsub).grid(row=4, column=2,pady=10)
            tk.Button(frame_operation, text='查看征订清单',font=('等线', 14),command=getsub).grid(row=5, column=2,pady=10)
            frame_results=tk.Frame(frame_operation)
            frame_results.grid(row=1, column=3,rowspan=5)
            tree=ttk.Treeview(frame_results,show="headings", columns=(
            "name", "mail", "syear"), selectmode=tk.BROWSE)
            # 设置表格文字居中
            tree.column("name", anchor="center", width=150)
            tree.column("mail", anchor="center", width=70)
            tree.column("syear", anchor="center", width=70)
            # 设置表格头部标题
            tree.heading("name", text="期刊名称")
            tree.heading("mail", text="邮发代码")
            tree.heading("syear", text="征订年份")
            tree.pack(expand=True, fill=tk.BOTH)
            tk.Button(frame_results, text='删除选定内容',font=('等线', 14),command=delsubc).pack(side='bottom')
        # change password
        if cb_var.get() == '8':
            def changepass():
                if not sql.Sqloperation().is_pass_match(aname,entrytext1.get()):
                    tk.messagebox.showerror('提示信息',message='原密码错误')
                    return False
                if entrytext3.get()!=entrytext2.get():
                    tk.messagebox.showerror(title='信息', message='新密码两次输入不一致，请重试')
                elif not sql.Sqloperation().checkpassformat(entrytext2.get()):
                    tk.messagebox.showerror('提示信息',message='密码格式不正确，不能为空以及包含空格')
                    return False
                else:
                    if sql.Sqloperation().update_admin_passwd(aname,entrytext2.get()):
                        tk.messagebox.showinfo('提示信息',message='修改成功')
                    else:
                        tk.messagebox.showerror('提示信息',message='修改失败')
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
        # find content
        if cb_var.get() == '9':
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
            def delcontentc():
                itemexist=False
                for item in tree.selection():
                    itemexist=True
                    item_text = tree.item(item,"values")
                if not itemexist:
                    tk.messagebox.showerror(title='信息', message='删除失败，请先用鼠标选中一条内容')
                    return
                pname=item_text[1]
                pyear=item_text[2]
                pvolume=item_text[3]
                pissue=item_text[4]
                title=item_text[5]
                author=item_text[6]
                page=item_text[7]
                if not tk.messagebox.askyesno('删除确认',message='确定删除选定的内容？'):return
                if sql.Sqloperation().delcontent(pname,pyear,pvolume,pissue,title,author,page):
                    tk.messagebox.showinfo(title='信息', message='删除成功')
                else:
                    tk.messagebox.showerror(title='信息', message='删除失败')
            frame_search1 = tk.Frame(frame_operation)
            frame_search1.pack()
            frame_search2 = tk.Frame(frame_operation)
            frame_search2.pack()
            frame_search3 = tk.Frame(frame_operation)
            frame_search3.pack()
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
            tree = ttk.Treeview(frame_operation, show="headings", columns=(
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
            tk.Button(frame_operation, text='删除选定内容',font=('等线', 14),command=delcontentc).pack(side='bottom')
    ##
    frame_option = tk.LabelFrame(admin_window, text='选择要进行的操作', height=1000,borderwidth=10)
    frame_option.grid(row=1, column=1, padx=10, pady=10, ipadx=10, ipady=10,sticky="n" + "s" + "w" + "e")
    # 分割线
    tk.Canvas(admin_window, bg='black', height=wh-50, width=1).grid(
        row=1, column=2, padx=10, pady=10, ipadx=1, ipady=10)
    frame_button = tk.Frame(admin_window)
    # 按顺序放置，不能移动下面语句的顺序
    frame_operation.grid(row=1, column=3, padx=10, pady=10, ipadx=10, ipady=10,sticky="n" + "s" + "w" + "e")
    # tk.Label(frame_option, text='选择要执行的操作：',font=('等线',16)).pack()
    tk.Radiobutton(frame_option, text='期刊信息查询', variable=cb_var,
                   value='1', font=('等线', 16), command=create_frame_operation).grid(column=1, row=1, pady=10)
    tk.Radiobutton(frame_option, text='期刊内容查询', variable=cb_var,
                   value='9', font=('等线', 16), command=create_frame_operation).grid(column=1, row=2, pady=10)
    tk.Radiobutton(frame_option, text='期刊借阅查询', variable=cb_var,
                   value='2', font=('等线', 16), command=create_frame_operation).grid(column=1, row=3, pady=10)
    tk.Radiobutton(frame_option, text='期刊借阅管理', variable=cb_var,
                   value='3', font=('等线', 16), command=create_frame_operation).grid(column=1, row=4, pady=10)
    tk.Radiobutton(frame_option, text='期刊目录登记', variable=cb_var,
                   value='4', font=('等线', 16), command=create_frame_operation).grid(column=1, row=5, pady=10)
    tk.Radiobutton(frame_option, text='期刊入库登记', variable=cb_var,
                   value='5', font=('等线', 16), command=create_frame_operation).grid(column=1, row=6, pady=10)
    tk.Radiobutton(frame_option, text='期刊内容登记', variable=cb_var,
                   value='6', font=('等线', 16), command=create_frame_operation).grid(column=1, row=7, pady=10)
    tk.Radiobutton(frame_option, text='期刊征订       ', variable=cb_var,
                   value='7', font=('等线', 16), command=create_frame_operation).grid(column=1, row=8, pady=10)
    tk.Radiobutton(frame_option, text='修改密码       ', variable=cb_var,
                   value='8', font=('等线', 16), command=create_frame_operation).grid(column=1, row=9, pady=10)
    admin_window.mainloop()
