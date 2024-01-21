from base64 import b64encode
def main(path):
    try:
        with open(path,'rb') as f:
            print('结果：')
            print(b64encode(f.read()))
    except:
        print('输入有误！')
if __name__=='__main__':
    while True:
        main(input('请输入文件路径：'))