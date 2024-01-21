'''\
#### 目前本库可以实现以下功能：  
    1.获取当前时间（实现方法示例如下）  
        ```python
        from lib.easytools import Time
        a=Time()
        print(a.gettime())
        ```  
    2.给字典排序+合并两个字典
        ```python
        from lib.easytools import Dict
        a={'a':[1,2,3],'b':[1,2]}
        b={'a':[4,5],'c':[3]}
        a,b=b,a
        c=Dict()
        print(c.sortdict(c.condict(a,b)))
        ```  
        还可以使用`demo()`函数完成这个示例。
'''


from time import strftime,localtime,time
class Time:
    def gettime(self):
        return strftime('%Y-%m-%d %H:%M:%S',localtime())

class Dict:
    def sortdict(self,_dict:dict,mode='key') -> dict|ValueError:
        '''最好不要用mode=\'value\'，因为这个功能并没有测试过。'''
        if mode=='key':
            c=[]
            for i in sorted (_dict) : 
                c.append((i, _dict[i]))
            return dict(c)
        elif mode=='value':
            return dict(sorted(_dict.items(), key = lambda kv:(kv[1], kv[0])))
        else:
            raise ValueError('Mode must be "key" or "value".')
        
    def condict(self,dict1:dict,dict2:dict):
        c=dict()
        namepool=[]
        for i in dict1.keys():
            for j in dict2.keys():
                #print(i,j,namepool)
                if j==i:
                    a=dict1[i]+dict2[j]
                    c[i]=a
                    namepool.append(i)
                    #print(dict1[i]+dict2[j])
                elif j in namepool:
                    c[j]+=dict2[j]
                    c[i]=dict1[i]
                else:
                    c[i]=dict1[i]
                    c[j]=dict2[j]
        return c

def demo():
    a={'a':[1,2,3],'b':[1,2]}
    b={'a':[4,5],'c':[3]}
    a,b=b,a
    c=Dict()
    print(c.sortdict(c.condict(a,b)))

if __name__=='__main__':
    demo()