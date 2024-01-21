from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import *

class MyQWidget(QWidget):
    def __init__(self, parent=None) -> None:
        super(MyQWidget,self).__init__(parent)
        self.setGeometry(255,150,482,465)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        
    #---gtj 实现鼠标拖拽功能
    def mousePressEvent(self, event):
        self.pressX = event.x()    #记录鼠标按下的时候的坐标
        self.pressY = event.y()

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()   #获取移动后的坐标
        moveX = x-self.pressX
        moveY = y-self.pressY  #计算移动了多少
 
        positionX = self.frameGeometry().x() + moveX
        positionY = self.frameGeometry().y() + moveY    #计算移动后主窗口在桌面的位置
        self.move(positionX, positionY) 
        
class UI(object):
    def __init__(self):
        #super(UI,self).__init__(parent)
        #self.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(93, 0, 255, 255), stop:1 rgba(255, 255, 255, 255));border-radius:13px;')
        self.initUI()

    def initUI(self):
        '''vbox=QVBoxLayout()

        g1=QGridLayout()
        g2=QGridLayout()

        uw=QWidget()
        pw=QWidget()'''
        win=MyQWidget()
        win.setWindowTitle('登录FutureChat')
        radius = 15
        win.setStyleSheet(
            """
            background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(93, 0, 255, 255), stop:1 rgba(255, 255, 255, 255));
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )
        l1=QLabel(win)
        l1.setText('Sign in')
        l1.setGeometry(0,0,161,61)
        l1.setFont(QtGui.QFont('Microsoft YaHei',20))
        l1.setStyleSheet('color:white;background-color:None;')
        l2=QLabel(win)
        l2.setText('账号：')
        l2.setGeometry(0,0,81,31)
        l2.setFont(QtGui.QFont('Microsoft YaHei',18))
        l2.setStyleSheet('color:white;background-color:None;')
        c1=QComboBox(win)
        c1.setWindowIcon(QtGui.QIcon('./down.png'))
        c1.setStyleSheet('QComboBox{\n	background-color:None;\n	border-radius:10px;\n}\nQComboBox::drop-down{\n	width:30px;\n	border-top-right-radius:10px;\n	border-botton-right-radius:10px;\n}')

        '''g1.addWidget(l1,0,0,QtCore.Qt.AlignmentFlag.AlignCenter)

        uw.setLayout(g1)
        pw.setLayout(g2)

        #grid.addWidget(l1,0,0,QtCore.Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(l1)
        self.setLayout(vbox)'''
        win.show()

if __name__=='__main__':
    from sys import argv,exit
    app=QApplication(argv)
    exe=UI()
    exit(app.exec_())