#work alone
#Q1

lst =  ['Antheil', 'SaintSaens', 'Price', 'Easdale', 'Nielsen']
lowerlst = [ s.lower() for s in lst]
same = []
for x in lowerlst:
    if x[0] == x[-1]:
        same.append(x)

print(same)

#Q2a

def hn(inputstr):
    return any(chr.isdigit() for chr in inputstr)
def password_check(oldpwd,newpwd):
    if oldpwd == newpwd:
        return False
    elif len(newpwd)<8:
        return False
    else:
        return hn(newpwd)
print(password_check('1234567','1234567'))
print(password_check('1234567','qwerrttd'))
print(password_check('1234567','queijij2'))
print(password_check('1234567','poeewe'))

#Q2b

def wordOccurCounter(sentence, word):
    table = str.maketrans(',.','  ')
    event = sentence.translate(table).lower().split()
    return event.count(word)
print(wordOccurCounter('May the Force be with you.','may'))
print(wordOccurCounter('Practice, practice and more PRACTICE','practice'))
print(wordOccurCounter('Yesterday she said yes','yes'))

#Q3
def line():
    print(l,':')
    return''

def multline(line,numCount):
    for i in range(1,n+1):
        x = i*l
        print (x,end=' ')
    return ''

l = int(input('line:'))
n = int(input('numCount: '))

print(line(),multline(l,n))


#Q4a

def numVowels(filename):
    file = open(filename,'r')
    content = file.read()
    B = content.lower()
    A = B.count('a')
    E = B.count('e')
    I = B.count('i')
    O = B.count('o')
    U = B.count('u')
    print(A+E+I+O+U)
    return A
    file.close()

    return len(content)
numVowels('exampleSU.txt')

#Q4b


file1 = 'file1SU.txt'
file2 = 'file2SU.txt'

def merge(file1,file2):
    f1 = open(file1,'a+')
    f2 = open(file2,'r')
    f1.write('\n')
    for i in f2:
        f1.write(i)

merge(file1,file2)






