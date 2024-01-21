from socket import socket,timeout,error,errno,SOCK_STREAM,AF_INET
from lib import ipFCID
from threading import Thread
from humanfriendly import parse_size as psize
from msg_config import *
from time import time

class SockObject:
    '''在使用前请输入参数（格式如下）：
    ```python
    #Something before...
    a=SockObject(
        {
            "host":host,
            "port":port,
            "setting":file,
            "black":black,
            "admin":admin,
            "errors":errors,
            "dat":data
        }
    )
    a.start()
    a.cmd()
    ```
    '''
    def __init__(self,args:dict) -> None:
        self.users:dict
        self.host=args['host']
        self.port=args['port']
        self.set=args['setting']
        self.black=args['black']
        self.admin=args['admin']
        self.err=args['errors']
        self.dat=args['dat']
        self.socketStart=True
        self.times=list()
        
        self.sockmain()

    def echo_sock(self):
        pass

    def sockmain(self):
        try:
            self.s=socket(AF_INET,SOCK_STREAM)
            self.sock.bind((self.host,self.port))
            self.sock.listen(int(self.set['max_user']))
        except:
            pass
        else:
            self.dat('已建立连接。')
            self.times.append(time())
            
    def cmd(_cmd:str):
        pass