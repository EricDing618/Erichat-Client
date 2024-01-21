'''future={
    "msg":"广播。",
    "sayto":"私聊。",
    "mention":"提到群里某人。"
}'''

class cmd:
    def __init__(self,cmd:str,stop,show_error,data,exerror,isstop):
        self.comm=cmd
        self.DefaultHelpDocDict={
            "stop":"关闭服务器。",
            "save":"保存所有数据。",
            "help":"打开帮助文档。",
            "ui":"打开功能界面。",
            "say":"对话。"
        }
        self.stop=stop
        self.show_error=show_error
        self.data=data
        self.exerror=exerror
        self.isstop=isstop
    def run(self):
        if self.inputwrong():
            pass
        else:
            self.c1=self.comm.split(' ')
            if self.c1[0]=='stop':
                self.stop()
            elif self.c1[0]=='ui':
                if self.c1[1]=='error':
                    self.show_error()
            else:
                self.data('未找到命令“#'+self.comm+'”。',title='ERROR')
    def returnhelp(self):
        global errors
        if self.inputwrong():
            pass
        elif self.comm not in self.DefaultHelpDocDict:
            self.exerror('未找到命令“#'+self.comm+'”。')
    def inputwrong(self):
        if self.isstop:
            self.data('请先关闭程序再启动服务器。')
            return True
        elif self.comm.startswith('#'):
            self.data('在控制台中不需要#号。',title='WRONG')
            return True
        else:
            return False
