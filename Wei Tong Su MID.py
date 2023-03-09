#Q1
def thirdPerson(word):
    word = input('word:')
    if word(-1)=='o':
        add('es')
    print()
    
thirdPerson('word')


#Q2

def numVowels(filename):
    file = open(filename,'r')
    content = file.read()
    linecount = len(content)
    wordcount = charcount = 0
    for line in content:
        words = line.split()
        wordcount, charcount = wordcount + len(words), charcount + len(count)
    print("File {0} has {1} lines, {2} words, {3} characters".format(file[0], linecount, wordcount, charcount)


numVowels('example.txt')


#Q3
def fib(bound):
    pre = 1
    cur = 1
    while cur <= bound:
        pre, cur = cur, pre+cur
        return cur
fib()

def fibo(i):
    
    if i == 1 or i ==2:
        return 1
    else:
        return fibo(i-1)+fibo(i-2)
#        print(fibo(n-1)+fibo(n-2),end='\t')

#Q4
def cross(n,m):
    for i in range(1,n+1):
        for k in range(1,m+1):
            if i ==(n+1)//2 or k == (m+1)//2:
                if k == (m+1)//2:
                    if i== (n+1)//2 and k ==(m+1)//2:
                        print(" + ",end = ' ')
                    else:
                        print(" | ",end =' ')
                else:
                    print (" - ",end =' ')
            else:
                print ("   ",end =' ')
        print() 
cross(5,5)
cross(5,9)
cross(6,10)

