import tkinter as tk
import tkinter.messagebox
import pickle
from adminUI import goto_adminui
from normalUI import goto_normalui
import pymysql
import sql
login_window = tk.Tk()
login_window.title('期刊管理软件 by Grade 17 CS class2 Group 12 AHU')
window_posx=550
window_posy=150
login_window.geometry('400x600+550+150')
login_window.iconbitmap('12.ico')
#界面图片
canvas = tk.Canvas(login_window, width=400, height=300, bg='white')
image_file = tk.PhotoImage(file='ahu.gif')
image = canvas.create_image(200, 0, anchor='n', image=image_file)
canvas.pack(side='top')
tk.Label(login_window, text='期刊管理系统',font=('等线', 16)).place(x=140,y=340)
#账号信息
tk.Label(login_window, text='工    号:', font=('等线', 14)).place(x=50, y=400)
tk.Label(login_window, text='密    码:', font=('等线', 14)).place(x=50, y=450)
# 用户名
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(login_window, textvariable=var_usr_name, font=('等线', 14))
entry_usr_name.place(x=120,y=400)
# 用户密码
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(login_window, textvariable=var_usr_pwd, font=('等线', 14), show='*')
entry_usr_pwd.place(x=120,y=450)
# 定义用户登录功能
def usr_login():
	# 这两行代码就是获取用户输入的usr_name和usr_pwd
	usr_name = var_usr_name.get()
	usr_pwd = var_usr_pwd.get()
	# 如果用户名和密码与文件中的匹配成功，则会登录成功
	if sql.Sqloperation().is_user_exist(usr_name):
		if sql.Sqloperation().is_pass_match(usr_name,usr_pwd):
			tkinter.messagebox.showinfo(title='登录信息', message='登录成功')
			login_window.destroy()
			if sql.Sqloperation().is_admin(usr_name):goto_adminui(usr_name)
			else: goto_normalui(usr_name)
			# 如果用户名匹配成功，而密码输入错误，则会弹出'Error, your password is wrong, try again.'
			else:
				tkinter.messagebox.showerror(title='登录信息', message='登录失败，请检查用户名或密码')
			# 如果发现用户名不存在
			else:  
				is_sign_up = tkinter.messagebox.askyesno('提示信息',message='    该账号不存在，是否转到注册页面？')
				# 提示需不需要注册新用户
				if is_sign_up:usr_sign_up()
# 定义用户注册功能
def usr_sign_up():
	def sign_to_system():
		# 以下三行就是获取我们注册时所输入的信息
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
	    # 这里就是判断，如果两次密码输入不一致，则提示Error, Password and confirm password must be the same!
	    if np != npf:
			tkinter.messagebox.showerror('提示信息',message='两次密码不一致')
			return False
	    # 如果用户名已经在我们的数据文件中，则提示Error, The user has already signed up!
	    elif sql.Sqloperation().is_user_exist(nn):
			tkinter.messagebox.showerror('提示信息',message='账号已存在')
			return False
		elif not sql.Sqloperation().checkpassformat(np):
			tkinter.messagebox.showerror('提示信息',message='密码格式不正确，不能为空以及包含空格')
			return False
		elif not sql.Sqloperation().checkidformat(nn):
			tkinter.messagebox.showerror('提示信息',message='工号格式（1字母+8数字）不正确')
			return False
		# 最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功Welcome！,You have successfully signed up!，然后销毁窗口。
		else:
			sql.Sqloperation().adduser(nn,np)
			tkinter.messagebox.showinfo('提示信息',message='注册成功')
			# 然后销毁窗口。
			sign_up_window.destroy()
	 
	# 定义长在窗口上的窗口
	sign_up_window = tk.Toplevel(login_window)
	sign_up_window.geometry('300x200+600+350')
	sign_up_window.title('注册窗口')
	new_name = tk.StringVar()  # 将输入的注册名赋值给变量
	#new_name.set('在此处输入用户名')  # 将最初显示定为'example@python.com'
	tk.Label(sign_up_window, text='用户名: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
	entry_new_name = tk.Entry(sign_up_window, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
	entry_new_name.place(x=130, y=10)  # `entry`放置在坐标（150,10）.
	new_pwd = tk.StringVar()
	tk.Label(sign_up_window, text='设置密码: ').place(x=10, y=50)
	entry_usr_pwd = tk.Entry(sign_up_window, textvariable=new_pwd, show='*')
	entry_usr_pwd.place(x=130, y=50)
	new_pwd_confirm = tk.StringVar()
	tk.Label(sign_up_window, text='确认密码: ').place(x=10, y=90)
	entry_usr_pwd_confirm = tk.Entry(sign_up_window, textvariable=new_pwd_confirm, show='*')
	entry_usr_pwd_confirm.place(x=130, y=90)
	# 下面的 sign_to_system
	btn_comfirm_sign_up = tk.Button(sign_up_window, text='注册', command=sign_to_system)
	btn_comfirm_sign_up.place(x=180, y=120)
# 第7步，login and sign up 按钮
btn_login = tk.Button(login_window, text='登录', command=usr_login)
btn_login.place(x=150, y=500)
btn_sign_up = tk.Button(login_window, text='注册', command=usr_sign_up)
btn_sign_up.place(x=250, y=500)
# 第10步，主窗口循环显示
login_window.mainloop()
