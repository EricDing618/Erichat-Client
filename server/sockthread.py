from socket import socket,timeout,error,errno,SOCK_STREAM,AF_INET
from lib import ipFCID
from threading import Thread
#from sys import exit
from humanfriendly import parse_size as psize
from msg_config import *
#import typing
from time import time

class MyThread(object):
    def __init__(self,host:str,port:int,set:dict,black:dict,admin:dict,errors,data,cmdapi):
        self.users:dict
        self.host=host
        self.port=port
        self.set=set
        self.black=black
        self.admin=admin
        self.err=errors
        self.dat=data
        self.cmd=cmdapi
        self.socketStart=True
        self.times=list()

    def echo_server(self,conn:socket,addr,contime):
        if (contime - self.times[-1]) >= self.set["between"]:
            id=ipFCID.to_id(':'.join(addr))
            join=False
            conn.send(str(IS_SERVER+self.set['mode']).encode())
            while True:
                content=conn.recv(psize(self.set['max_size'],True)).decode()
                if content==QUIT:
                    break
                else:
                    if not join:
                        if content.startswith(IS_CLIENT):
                            pass
                        else:
                            pass
        else:
            conn.send(str(ERROR+'连接太过频繁，请重试！').encode())
                        
    def sockmain(self):
        self.sock=socket(AF_INET,SOCK_STREAM)
        self.sock.bind((self.host,self.port))
        self.sock.listen(int(self.set['max_user']))
        self.dat('已建立连接。')
        self.times.append(time())
        try:
            while self.socketStart:
                conn,addr=self.sock.accept()
                temp=time()
                self.userthread=Thread(target=self.echo_server,args=(conn,addr,temp,))
                '''self.threads.append(self.userthread)
                self.socks.append(conn)'''
                self.userthread.start()

        except Exception as e:
            print(e.with_traceback(None))

    def start(self):
        self.t=Thread(target=self.sockmain)
        #self.t.setDaemon(True)
        self.t.start()
    def join(self):
        self.socketStart=False
        '''if self.users != []:
            for i in self.users:
                i.join()'''
        if self.usoc != []:
            for i in self.usoc:
                i.close()
        #self.t.join()
        self.sock.close()
