#Work alone
#Q1a

first = input('Your first name: ')
last = input('Your last name: ')
print('your name is '+ first+' '+ last)

#Q1b

Money = float(input('Enter your account balance:'))
rate = float(input('Enter the interest rate(e,g, 3 means 3%):'))
print(Money*rate/100 + Money)

#Q2

lst = ['yellow','pink','purple','black','white','maroon']
Color = input(" What's your favorite color:")
if Color in lst:
    print('I like that color too')
else:
    print('I see. Nice for you')

#Q3

n = int(input('Please enter vote number: '))
vote = []
for v in range(1,n+1):
    v = input("Chose your opinion 'yes' or 'no': ")
    vote.append(v)

SumY= vote.count('yes')

if SumY/n > 0.5:
    print('pass')
else:
    print('fail')


#Q4a

def NumberPresent():
    x=[1,7,11,15,19,27]
    Num = int(input('Please input number: '))
    a= bool(Num in x)
    print(a)
    return
print(NumberPresent())
    

#Q4b
lst = ['antheil','saint-Saens', 'price', 'easdale', 'nielsen']
for x in lst:
    if x[0] == x[-1]:
        print(x)
    

        

