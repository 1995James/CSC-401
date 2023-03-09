#Q1

class Account:
    def __init__(self,fname,lname,balance):
        self.fname = fname
        self.lname = lname
        self.balance = balance
        print('Account Created')

    def deposit(self):
        amount = float(input('Enter amount to be Deposited:'))
        self.balance += amount
        print('Transaction completed successfully! Amount Deposited:',amount)

    def getFname(self,fname):
        return self.fname

    def getLname(self, lname):
        return self.lname

    def getBalance(self):
        return self.balance

    def withdraw(self):
        amount = float(input('Enter amount to be withdrawn:'))
        if self.balance>=amount:
            self.balance-=amount
            print('Transaction completed successfully! You Wihtdrew:',amount)
        else:
            print('Insufficient balance')



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
