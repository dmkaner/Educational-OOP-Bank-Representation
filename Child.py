from Customer import *
import random

# This class is so that there will be restrictions for some things that a child can not do
class Child(Customer):

    #Purely to see if how many children the bank has
    childCount = 0

    def __init__(self, name, age, phone, sex, accountnum, savbalance, checbalance):
        Customer.__init__(self, name, age, phone, sex, accountnum, savbalance, checbalance)
        Child.childCount += 1
        self.__accountnum = accountnum
        self.__savbalance = savbalance
        self.__checbalance = checbalance
        #self.__pin = random.randint(1000,9999)

        # print pin number on creation so user will know it. this is the only time it will be displayed
        # varaible will primarily be used by ATM class
        #print(self.name + "'s Assigned Pin Number:", self.__pin)

    @classmethod
    def amountOfChildren(cls):
        return cls.childCount

    # make deposit + set limit for how much a child can deposit
    def deposit(self, amount):
        if amount > 500:
            print('INVALID AMOUNT: Child accounts have a deposit limit of $500.00')
        elif amount < .01:
            print('INVALID AMOUNT: Cannot deposit less than $0.01')
        else:
            self.__checbalance += amount
            print('*****ACTION COMPLETE*****')

    def withdrawal(self, accountnum, amount):
        if accountnum == self.__accountnum:
            if amount <= self.__checbalance:
                if amount <= 100:
                    self.__checbalance -= amount
                    print('*****ACTION COMPLETE*****')
                    return amount
                elif amount < .01:
                    print('INVALID AMOUNT: Cannot withdrawal less than $0.01')
                else:
                    print('INVALID AMOUNT: Child accounts have a withdrawal limit of $100.00')
            else:
                print(self.name, 'does not have this much money in his/her account to withdrawal, sorry.')
                return
        else:
            print('The account number: "' + str(accountnum) + '" does not exist under the name: "' + self.name + '"')
            return

    # method for ATM to deposit money
    def atmDeposit(self, amount, pin):
        if pin == self.__pin:
            self.deposit(amount)
        else:
            print('Transaction could not be completed, incorrect PIN')

    # method for ATM to withdraw money
    def atmWithdraw(self, amount, pin):
        if pin == self.__pin:
            return self.withdrawal(self.__accountnum, amount)
        return 'Transaction could not be completed, incorrect PIN'

    def checkSavBalance(self):
        accountnum = int(input('Enter the account number: '))
        if accountnum == self.__accountnum:
            print(self.name + ' has ' + "$" + str(self.__savbalance))
        else:
            print('The account number: "' + str(accountnum) + '" does not exist under the name: "' + self.name + '"')

    def checkChecBalance(self):
        accountnum = int(input('Enter the account number: '))
        if accountnum == self.__accountnum:
            print(self.name + ' has ' + "$" + str(self.__checbalance))
        else:
            print('The account number: "' + str(accountnum) + '" does not exist under the name: "' + self.name + '"')

    def __str__(self):
        accountnum = int(input('Enter the account number: '))
        if accountnum == self.__accountnum:
            return '---Child Account Info---' + '\n' + \
                    'Name: ' + self.name + '\n' + \
                    'Savings Account: ' + str(self.__savbalance) + '\n' + \
                    'Checking Account: ' + str(self.__checbalance) + '\n' + '------------------'
        else:
            return 'The account number: "' + str(accountnum) + '" does not exist under the name: "' + self.name + '"'

    def __del__(self):
        # this is to make sure that when I delete a child account it also decreases the customer account
        Customer.customerCount -= 1
        Child.childCount -= 1
        del self
