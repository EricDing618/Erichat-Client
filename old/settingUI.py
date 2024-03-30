import ttkbootstrap as ttk
'''root=ttk.Window()
checkVar = ttk.StringVar(value="0")
check = ttk.Checkbutton(root, text="Checkbutton test", variable=checkVar,bootstyle="round-toggle")
check.grid(row=0, column=0, sticky='w', padx=2 ,pady=5)
# 定义按钮点击事件
def button_Click(event=None):
    print(checkVar.get())
 
# 创建两个按钮
b1=ttk.Button(root,text='click me', command=button_Click)
b1.grid(row=0, column=2, sticky='w', padx=2 ,pady=10)
 
# 进入消息循环
root.mainloop()'''
def main():
    pass
if __name__ == '__init__':
    root=ttk.Window()
    helplist=ttk.Frame(root,height=100,width=20)
    helplist.pack(side='left',fill='both',anchor='w',expand=True)
    b1=ttk.Button(helplist,text='a')
    b1.pack(anchor='w',fill='x')
    b2=ttk.Button(helplist,text='b')
    b2.pack(anchor='w',fill='x')
    info=ttk.Frame(root,height=100,width=80)
    info.pack(side='right',fill='both',anchor='e',expand=True)
    L1=ttk.Label(info,text='114514')
    L1.pack()
    root.mainloop()