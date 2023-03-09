
#Q1a
def lookupWord(filename):
    file = open(filename,encoding = 'utf-8')
    lines = file.readlines()
    file.close()

    d = {}
    for i in lines:
        (key, value) = i.split(':::')
        d[key] = value

    while True:
        word = input('Enter a word:')
        lword = word.capitalize()
        if lword in d:
            print(d[lword])
        elif lword == '':
            break
        else:
            print('Word Not found')
#Q1b
def index(filename,words):
    file = open(filename,'r',encoding = 'utf-8')
    lines = file.readline()
    file.close()
    filename.replace("'",'').replace(',','').replace('.','').replace('!','')
    d = {}

    for k,line in enumerate(lines):
        if words in line:
            print(words,k+1)

#Q2a
def hasDuplicates(lst):
    seen = set()
    for x in lst:
        seen.add(x)
        if x in seen:
            return True        
    return False

#Q2b
def unique():
    lst = []
    while True:
        word = input('Enter your input here:')
        lst.append(word)
        same = set(lst)
        if word == '':
            same.remove('')
            return same
