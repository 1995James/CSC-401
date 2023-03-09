#Work alone
#Q1
def rockPaperScissors():
    num = int(input('How many times you want to play ? '))
    Computer = 0
    Player = 0
    for i in range(1,num+1):
        from random import randint
        t = ['Rock','Paper','Scissors']
        computer = t[randint(0,2)]
        Players = input('Rock, Paper, Scissors or stop to end game?')
        player = Players.capitalize()
        if player == 'Stop':
            print('Computer:',Computer)
            print('Player:',Player)
            break
        elif player == computer:
            print('Tie!')
        elif player == 'Rock':
            if computer == 'Paper':
                print('You lose!')
                Computer = Computer +1
            else:
                print('You win!')
                Player = Player +1
        elif player == 'Paper':
            if computer == 'Scissors':
                print('You lose!')
                Computer =Computer +1
            else:
                print('You win!')
                Player = Player +1
        elif player == 'Scissors':
            if computer == 'Rock':
                print('You lose!')
                Computer = Computer +1
            else:
                print('You win!')
                Player = Player +1
        else:
            print("That's not a valid play. Check your spelling!")
        print('Computer:',Computer)
        print('Player:',Player)
    print('Gameover')


#Q2
    
def startUp(filename):
    d = dict()
    try:
        file= open(filename,'r')
        
        for line in file:
            pin,firstname,lastname,balance= line.split(',')
            balance = float(balance)
            d[pin]=[firstname,lastname,balance]
        return d
    except:
        print('Cannot get to the file')
        return None
    

def verifyPin(dict):
    pin = input('Please enter your pin: ')
    
    if len(pin) == 4 and pin.isnumeric() and pin in dict:
        return [pin, dict[pin][0]]
    else:
        print('Incorrect Pin')
        return[None,None]

def menu(name):
    while True:
        print(name,'choose one of the following option')
        print('D: Deposit')
        print('W: Withdraw')
        print('B: Balance')
        print('Q: Quit')
        choice = input('Enter your choice: ')
        if choice in 'DdWwBbQq':
            return choice
        else:
            print("Valid choices are D, W, B, Q, try again")

def getAmount():
    while True:
        amt = input('Enter the amount: ')
        try:
            amt = float(amt)
            if amt <0:
                print("Negative amount. Please try again")
            else:
                return amt
        except:
            print("Invalid amount. Use digits only")

def deposit(pin, dict):
    amt = getAmount()
    dict[pin][2] += amt

def withdraw(pin, dict):
    amt = getAmount()
    while amt > dict[pin][2]:
        print("Insufficient funds to complete the transaction")
        amt = getAmount()

    dict[pin][2] -= amt

def balance(pin, dict):
    return dict[pin][2]

def quit(pin, dict):
    while True:
        ch = input('Do you really want to leave the transation Y/N? ')
        if ch in 'Yy':
            return [dict[pin][0],dict[pin][1]]
        elif ch in 'Nn':
            return [None,None]
        else:
            print('enter Y to quit or N otherwise')

def main():
    d = startUp('accounts.csv')
    if d == None:
        return
    pin, name = verifyPin(d)
    if pin != None and name != None:
        while True:
            print()
            choice = menu(name)
            if choice in 'Dd':
                deposit(pin, d)
            elif choice in 'Ww':
                withdraw(pin, d)
            elif choice in 'Bb':
                bal = balance(pin, d)
                print('Your current balance is ${:,.2f}'.format(bal))
            elif choice in 'Qq':
                fname, lname = quit(pin, d)
                if fname != None and lname != None:
                    print('\n{} {}, thanks for using ABC Bank'.format(fname, lname))
                    break





