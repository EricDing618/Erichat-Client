import time
class data:
    '''A module made by Eric.
We can use this module to show data or save data.'''
    def __init__(self,
                 time='['+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+']',
                 title='[INFO]',
                 info='Running Server...',
                 num=None,
                 line=False):
        '''If line is True,do not use function printData().'''
        self.number=num
        self.line=[]
        self.string=[time,title,info]
    def save(self,line=False,filename='LastData.txt',encoding='UTF-8',mode='a+'):
        f=open(filename,mode,encoding=encoding)
        if line==True:
            for i in self.line:
                f.write('\n'+i)
        else:
            f.write('\n'+self.string)
        f.close()
    def printData(self,line=False):
        if self.number == None:
            if line==True:
                print('\n'.join(self.line))
            else:
                print(' '.join(self.string))
        else:
            if line==True:
                print('\n'.join(self.line))
            else:
                self.string.append(str(self.number)+'%')
                print(' '.join(self.string))
    def appendline(self,
                 time='['+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+']',
                 title='[INFO]',
                 info='Running Server...',
                 num=None,
                 save=False):
        if num==None:
            self.line.append(time+' '+title+' '+' '+info)
            if save==True:
                self.save(True,mode='w')
        else:
            self.line.append(time+' '+title+' '+' '+info+' '+str(num)+'%')
            if save==True:
                self.save(True,mode='w')
    def returnData(self,line=False):
        if self.number == None:
            if line==True:
                return '\n'.join(self.line)
            else:
                return ' '.join(self.string)+'\n'
        else:
            if line==True:
                return '\n'.join(self.line)
            else:
                self.string.append(str(self.number)+'%')
                return ' '.join(self.string)+'\n'
def quickly(time_='['+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+']',
                 title='[INFO]',
                 info='Running Server...',
                 num=None,
                 line=False,
                 return_=False):
    d1=data(time=time_,title=title,info=info,num=num,line=line)
    if return_==False:
        d1.printData()
    else:
        d1.returnData()