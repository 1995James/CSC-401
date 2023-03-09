#work alone
#Q1


def improve(lst):
    lstMin = min(lst)
    lstSum = sum(lst)
    newValue = lstSum - lstMin
    
    while lstSum < 0 and newValue > 0:
        
        lst.remove(min(lst))
        print ('Transactions: ',lst,'.', 'Value: ', newValue)
        break
    else:
        print('Oops, look bad, cannot be improved')

mylist = [10,25,-60,100,-80,-40,10]
improve(mylist)
mylist = [10,25,-45,60,-50,-40,10]
improve(mylist)
mylist = [-5,-10,-20]
improve(mylist)



#Q2a


def guess():
    import random
    answer = random.randint(0,100)
    guess = 0
    while guess!=answer:
        try:
            guess = int(input('Enter your guess:'))
            if guess > answer:
                print("too high")
            elif guess < answer:
                print("too low")
            else:
                print('You got it')
        except:
            print('That was not a valid number.')
    

#Q2b

def add():
    lst = []
    while True:
        try:
            number = input('Please enter a number:')
            if number == '':
                return '{} {}' .format(('Your total is '),sum(lst))
            lst.append(eval(number))
        except:
            print('Please enter a valid number!')


