
#Q1

n = int(input('Please enter vote number: '))
vote = []
for v in range(1,n+1):
    v = input("Chose your opinion 'yes' or 'no': ")
    vote.append(v)

SumY= vote.count('yes')

if SumY/n ==1:
    print('unanimously')
elif SumY/n > 2/3:
    print('supermajorit')
elif SumY/n > 0.5:
    print('simple majority')
else:
    print('fail')

#Q2a

mylst = [1,2,7,10,500,-5]
mymin = sorted(mylst)
print(mymin[0])

#Q2b

mylist = [1,2,-3,4,5,-1,-5]

for x in range (len(mylist)):
    if mylist[x]< 0:
        mylist[x]=mylist[x]*-1 
    else:
        mylist[x]
print (mylist)


#Q2c

def multLine(row, col):
    for x in range(1,row+1):
        print(x,end=':')
        
        for n in range(1,col + 1):
            print(n*x,end=' ')
        print()
multLine(10,10)

#Q2d

def rect(n,m):
    for i in range(0,n):
        for k in range(0,m):
            if i != 0 and i != n-1:
                if k == 0 or k == m-1:
                    print(" * ",end =' ' )
                else:
                    print ("   ",end =' ')
            else:
                print (" * ",end =' ')
        print()
rect(4,6)
rect(2,6)





