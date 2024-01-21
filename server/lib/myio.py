from io import BytesIO
from pickle import dump,load
from easytools import Dict
from pathlib import Path
from json import dumps,loads

class ChatIO:
    def __init__(self,filepath:None|str,coding='utf-8'):
        self.path=filepath
        self.type=coding
        self.iof=BytesIO()
        self.dict={str:dict}
        self.timer=[str]
        self.c=Dict()
    
    def write(self,string:str):
        '''将字符串写入BytesIO'''
        c1=self.iof.getvalue().decode(self.type)
        c2=c1.splitlines()

        if len(c1) > 1000: #保存处理非常多的数据
            for i in c2:
                title,text=i.split(':',1)
                time,name=title.split('-',1)
                self.timer.append(time)
                self.dict[time][name]=text

            self.save()

        self.iof.write(string.encode(self.type))

    def get(self):
        '''该函数只能简单地将BytesIO内部转换成的字符串分割为每一行并返回一个列表'''
        return self.iof.getvalue().decode(self.type).splitlines()
    
    def save(self):
        '''中途保存BytesIO的数据，非自动'''
        for i in self.timer:
            if Path(f'./dat/.chat/{i}.chat').is_file():
                with open(f'./dat/.chat/{i}.chat','rb+') as f:
                    a=loads(load(f))
                    dump(self.c.sortdict(self.c.condict(self.dict[i],a)) ,f)
            else:
                with open(f'./dat/.chat/{i}.chat','wb') as f:
                    dump(dumps(self.dict[i]),f)
