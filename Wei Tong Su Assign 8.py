
#Q1a
def natureNumbers(n):
    def N(x):
        if x <= n:
            print(x,end= ' ')
            x += 1
            N(x)
    x = 1
    return N(x)   


#Q1b
def alt(s,t):
    n = int(len(s))
    if len(s+t) == 0:
        return ''
    elif len(s)!=len(t):
        return ''
    else:
        print(s[0]+t[0],end = '')
        alt(s[1:],t[1:])

#Q2
#(1)
def factorial(n):
    P = 1
    if n ==0:
        return 1
    else:
        for i in range(1,n+1):
            P *= i
        return P
            


#(2)
def factorialRecur(n):
    if n ==0:
        return 1
    else:
        return factorialRecur(n-1)*n


import time
def timing(func, n):
    start = time.time()
    func(n)
    end = time.time()
    print( end - start)




timing(factorial,1000)
timing(factorialRecur,1000)
