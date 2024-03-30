import random

publicDict={
    'usefulletterList':['n', 'd', 'z', 'g', 'u', 'f', 'p', 'x', 'r', 's', 't', 'b', 'y', 'q', 'o', 'v', 'k', 'j', 'w', 'h'],
    'saltletterList':['e', 'i', 'c', 'm', 'l', 'a','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    '.':['?','!','@','~','=',']'],
    ':':['#','<','>',';','[','.'],
    'number':['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
}

def to_id(ip):
    '''ip to FCID.'''
    make=[]
    for i in ip: #main
        if i in publicDict['number']:
            make.append(publicDict['usefulletterList'][int(i)*2])
        elif i == '.':
            make.append(random.choice(publicDict['.']))
        elif i == ':':
            make.append(random.choice(publicDict[':']))
    for i in range(5): #salt
        make.insert(random.randint(0,len(make)),random.choice(publicDict['saltletterList']))
    return ''.join(make)

def to_ip(FCID):
    '''FCID to ip.'''
    make=[]
    for i in FCID:
        if i in publicDict['saltletterList']:
            pass
        elif i in publicDict['usefulletterList']:
            make.append(str(publicDict['usefulletterList'].index(i)//2))
        elif i in publicDict['.']:
            make.append('.')
        elif i in publicDict[':']:
            make.append(':')
    return ''.join(make)

if __name__ == '__main__':
    print(to_id('127.0.0.1'))
    print(to_ip('cLeo~1a~Ba@60c'))