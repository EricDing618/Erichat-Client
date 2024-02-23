#导入库
#import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import chatUI,file_UI,helpUI,cmdUI,settingUI,userUI,login #自制ui库
from pymod import*#自制扩展包

#函数
def delall(self):
    for i in self.winfo_children():
        i.destroy()
def openim(path,rsize=(100,100)):
    a=Image.open(path)
    a=a.resize(rsize)
    return ImageTk.PhotoImage(a)
#import tkinter as tk
#root = tk.Tk()

#主程序
def main(root:ttk.Window):
    #创建窗口及窗口属性
    #root.config(background='blue')
    initwin.clean(root)
    root.title('EChat')
    root.geometry('700x600+200+200')
    root.resizable(False, False)
    '''b1 = ttk.Button(root, text="Button 1", bootstyle='SUCCESS')
    b1.pack(side='left', padx=5, pady=10)'''

    #欢迎语和提示
    welcome=ttk.Label(root,text='FutureChat',font=('Montserrat',20),foreground='black')
    infor=ttk.Label(root,text='仅供学习使用，请勿商用！')

    #图标
    chat_ico=openim('./image/chat.png',(50,50))
    help_ico=openim('./image/help.png',(50,50))
    setting_ico=openim('./image/setting.png',(50,50))
    file_ico=openim('./image/file.png',(50,50))
    report_ico=openim('./image/cmd.png',(50,50))
    user_ico=openim('./image/user.png',(50,50))

    #按钮
    help = ttk.Button(root,text='帮助', bootstyle=('info', 'outline'),image=help_ico,compound='top',command=helpUI.main)
    #chat.pack(side='left', padx=5, pady=10,fill='both',expand=True,anchor='nw')
    chat = ttk.Button(root,text='聊天', bootstyle=('info', 'outline'),image=chat_ico,compound='top',command=chatUI.main)
    setting = ttk.Button(root,text='设置', bootstyle=('info', 'outline'),image=setting_ico,compound='top',command=settingUI.main)
    files = ttk.Button(root,text='文件', bootstyle=('info', 'outline'),image=file_ico,compound='top',command=file_UI.main)
    report = ttk.Button(root,text='命令', bootstyle=('info', 'outline'),image=report_ico,compound='top',command=cmdUI.main)
    user = ttk.Button(root,text='账户', bootstyle=('info', 'outline'),image=user_ico,compound='top',command=userUI.main)

    #布局
    welcome.place(x=350,y=100,anchor='center')
    help.place(x=240,y=160,anchor='ne')
    chat.place(x=350,y=160,anchor='n')
    setting.place(x=460,y=160)
    files.place(x=240,y=280,anchor='ne')
    report.place(x=350,y=280,anchor='n')
    user.place(x=460,y=280)
    infor.place(x=350,y=450,anchor='center')

    #主循环
    root.mainloop()

if __name__ == '__main__':
    a=ttk.Window()
    main(a)