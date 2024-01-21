#packages and modules
from json import load,dump,JSONDecodeError
from pickle import load as pload,dump as pdump
from lib import *
from lib.cmd import cmd
from ttkbootstrap import Frame,Label,Text,Entry,Button,Scrollbar,Window
#from ttkbootstrap.dialogs import Messagebox
from tkinter.messagebox import askokcancel
from PIL import ImageTk,Image
from base64 import b64decode
from threading import Thread
from time import strftime,localtime
from msg_config import*
from sockthread import MyThread
from socket import timeout,error,errno
from errno import errorcode
from os import system,getcwd
#from sys import exit
'''from ctypes import windll,c_int,byref,sizeof
from win32gui import GetParent'''
line=1.0
errors=[]
isstop=False

#tools
def savedat(set=True,black=True,admin=True,*args):
    if set:
        with open('setting.json','w',encoding='UTF-8') as f:
            dump(args[0],f)

def savewin():
    a=askokcancel('退出程序','确定要退出程序吗？')
    if a:
        root.destroy()
        try:
            t.join()
        except:
            print('error.')
        exit(0)
'''def round_ui(win):
    _master = GetParent(win.winfo_id())
    Value = c_int(1)
    def dwm_set_window_attribute(type, attribute, size):
        windll.dwmapi.DwmSetWindowAttribute(_master,type,attribute,size)
    dwm_set_window_attribute(33,byref(Value),sizeof(Value))'''
def cmds(CommandString='',mode='run'):
    if mode=='run':
        cmd(CommandString,stop,show_error,data,exerror,isstop).run()
    elif mode=='help':
        cmd(CommandString,stop,show_error,data,exerror,isstop).returnhelp()
'''def notdel(object_):
    if object_.winfo_exists():
        print('对象存在')
    else:
        print('对象不存在')'''
def exerror(var=None,stops=False,string='未知错误。',title='ERROR',showdat=True):
    if var !=None:
        errors.append(str(strftime('%Y-%m-%d %H:%M:%S',localtime())+':'+repr(var)))
    if showdat:
        data(string,title=title)
    if stops:
        stop()

def stop():
    global isstop,file,t
    if isstop!=True:
        data('>>>')
        isstop=True
        e1.configure(state='normal')
        b1.configure(state='normal')
        b2.configure(state='normal')
        if t.socketStart:
            t.join()
'''def start():
    global isstop
    isstop=False
    data('已成功重启。')
    main()'''
def runcmd(string=None):
    global line
    global txt
    a=cmds(string)
    line+=1.0
    txt.see(line)
def data(info:str,num=None,title='INFO'):
    global line,txt
    data_='['+strftime('%Y-%m-%d %H:%M:%S',localtime())+'] ['+title+'] '+info
    if num != None:
        data_+=f' {num}%'
    txt.configure(state='normal')
    txt.insert('end',data_+'\n')
    txt.configure(state='disabled')
    line+=1.0
    print(data_)
def funcHelper(string=None):
    a=cmds(string,'help')
def show_error():
    with open('./log/errors.txt','w',encoding='utf-8') as f:
        cache='共有'+str(len(errors))+'个报错内容。（'+strftime('%Y-%m-%d %H:%M:%S',localtime())+'的查询结果）\n============'
        for i in errors:
            cache+=f'\n{i}'
        f.write(cache)
    a=Thread(target=system,args=(f'{getcwd()}\\log\\errors.txt',))
    a.start()
    a.join()
    
#main functions
def ui():
    global root,e1,b1,b2,txt
    root=Window()
    root.title('FutureChat Server')
    root.resizable(0,0)
    root.protocol('WM_DELETE_WINDOW',savewin)
    '''title=Frame(root,width=400,height=100)
    title.pack(expand=True)'''
    main=Frame(root,width=400,height=300)
    main.pack(expand=True)
    cmd=Frame(root,width=400,height=100)
    cmd.pack(expand=True)
    scry=Scrollbar(main,style='primary-round')
    scrx=Scrollbar(main,orient='horizontal',style='primary-round')
    txt=Text(main,wrap='none',state='disabled',height=24,width=78,yscrollcommand=scry.set,xscrollcommand=scrx.set)
    scry.config(command=txt.yview)
    scrx.config(command=txt.xview)
    txt.grid(row=0,column=0,sticky='nwse')
    scry.grid(row=0,column=1,sticky='ns')
    scrx.grid(row=1,column=0,sticky='we')
    L1=Label(cmd,text='Command:#',style='info')
    L1.grid(row=0,column=0)
    e1=Entry(cmd,width=50,style='info')
    e1.grid(row=0,column=1)
    e1.bind('<Return>',lambda event:runcmd(e1.get()))
    b1=Button(cmd,text='run',command=lambda:runcmd(e1.get()))
    b1.configure(takefocus=False)
    b1.grid(row=0,column=2)
    b2=Button(cmd,text='doc',style='success',command=lambda:funcHelper(e1.get()))
    b2.configure(takefocus=False)
    b2.grid(row=0,column=3)
    '''L2=Label(title,text='控制台')
    L2.grid()'''
    e1.configure(state='disabled')
    b1.configure(state='disabled')
    b2.configure(state='disabled')
def main():
    global file,errors,sock,t
    data('FutureChat服务器管理系统 Version:Beta 0.1')
    data('='*(70-len('['+strftime('%Y-%m-%d %H:%M:%S',localtime())+'] [info] ')))
    data('提示：')
    data('1.严禁做违法操作，请谨防上当受骗。')
    data('2.目测本程序仅适用于Windows系统。')
    #data('3.用户名都是上次进入获取到的（第一次即显示FCID）')
    data('3.您可以使用#help命令或点击doc按钮查看帮助文档或描述。')
    data('='*(70-len('['+strftime('%Y-%m-%d %H:%M:%S',localtime())+'] [info] ')))
    data('正在启动服务器...')
    data('正在读取配置文件setting.json...')
    try:
        file=load(open('setting.json','r',encoding='UTF-8'))
        black=load(open('./dat/blacklist.json','r',encoding='UTF-8'))
        admin=load(open('./dat/admin.json','r',encoding='UTF-8'))
        root.title(file['name'])
        global host,port
        host,port=file["host"],file["port"]
        data('ip及端口为：'+str([host,port]))
        try:
            if file['icon'][0] in ['default','mode']:
                icon=ImageTk.PhotoImage(data=b64decode(base.icon()))
                root.tk.call('wm', 'iconphoto',root._w,icon)
                data('已使用默认图标。')
            elif file['icon'][0]=='base':
                root.tk.call('wm', 'iconphoto',root._w,ImageTk.PhotoImage(data=b64decode(bytes(file['icon'][1]))))
                data('已使用自定义图标。')
            elif file['icon'][0] in ['photo','image','img']:
                icon=ImageTk.PhotoImage(Image.open(str(file['icon'][1])))
                root.iconphoto(True,icon)
                data('已使用自定义图标。')
            else:
                root.tk.call('wm', 'iconphoto',root._w,ImageTk.PhotoImage(data=b64decode(base.icon())))
                data('设置图标有误，已使用默认图标。')
        except Exception as e:
            root.tk.call('wm', 'iconphoto',root._w,ImageTk.PhotoImage(data=b64decode(base.icon())))
            exerror(e,string='设置图标有误，已使用默认图标。')
        root.attributes('-alpha',float(file['opacity']))
        data('已设置透明度。')
        '''if file['ui_round']==True:
            round_ui(root)
            data('已设置窗口边角为：圆角。')'''
        txt.see('end')
        root.update()
        e1.configure(state='normal')
        b1.configure(state='normal')
        b2.configure(state='normal')
        t=MyThread(host,port,file,black,admin,exerror,data,cmds,)
        t.start()
    except (FileNotFoundError,KeyError,IndexError,TypeError,JSONDecodeError) as e:
        exerror(e,True,'配置似乎遭到损坏，服务器无法启动！')
    except error:
        a=errorcode[errno]
        exerror(a,stops=True,string=f'Socket错误：{a}')
    except timeout:
        exerror(stops=True,string='连接超时。')
    '''except OSError:
        print('error.')
        exit(0)'''
    root.mainloop()

#run
if __name__=='__main__':
    ui()
    main()