import ttkbootstrap as ttk
from pymod import*
def main(master:ttk.Window):
    initwin.clean(master)
    title=ttk.Label(master,text='Sign in',font=('Montserrat',20))
    title.place(x=350,y=100,anchor='center')
    L1=ttk.Label(master,text='昵称：',font=('Montserrat',20),style='info')
    L1.place(x=147,y=160,anchor='nw')
    E1=ttk.Entry(master,width=40,style='info')
    E1.place(x=250,y=160,anchor='nw')
    s = ttk.Style()
    s.configure('my.TButton', font=('Montserrat', 16))
    v1=ttk.IntVar(master)
    c1=ttk.Checkbutton(master,text='自动登录',variable=v1)
    def v():
        if v1.get() == 1:
            print(1)
        else:
            print(0)
    B1=ttk.Button(master,text='登录使用FutureChat',style='my.TButton')
    B1.place(x=350,y=300,anchor='center')
    c1.configure(command=v)
    c1.place(x=230,y=350,anchor='nw')
if __name__ == '__main__':
    root=ttk.Window('FutureChat')
    root.geometry('700x600+200+200')
    main(root)
    root.mainloop()