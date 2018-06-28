from Customer import *
from Child import *
import random

# This class is so that there will be restrictions for some things that a child can not do
class Parent(Customer):

    #Count how many parent classes
    parentCount = 0

    def __init__(self, name, age, phone, sex, accountnum, savbalance, checbalance):
        Customer.__init__(self, name, age, phone, sex, accountnum, savbalance, checbalance)
        Parent.parentCount += 1
        self.__accountnum = accountnum
        self.__savbalance = savbalance
        self.__checbalance = checbalance
        self.__pin = random.randint(1000,9999)

        # print pin number on creation so user will know it. this is the only time it will be displayed
        # varaible will primarily be used by ATM class
        print(self.name + "'s Assigned Pin Number:", self.__pin)

    @classmethod
    def amountOfParents(cls):
        return cls.parentCount

    def deposit(self, amount):
        self.__checbalance += amount
        print('*****ACTION COMPLETE*****')

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

    def withdrawal(self, accountnum, amount):
        if accountnum == self.__accountnum:
            if amount <= self.__checbalance:
                self.__checbalance -= amount
                print('*****ACTION COMPLETE*****')
                return amount
            elif amount < .01:
                print(self.name, 'cannot withdrawal less than $0.01')
                return
            else:
                print(self.name, 'does not have this much money in his/her account to withdrawal, sorry.')
                return
        else:
            print('The account number: "' + str(accountnum) + '" does not exist under the name: "' + self.name + '"')
            return

    # makes a deposit into a childs account
    def childDeposit(self, amount, child):
        Child.deposit(child, amount)

    # checks the amount a child has in their savings
    def childCheckSavings(self, child):
        Child.checkSavBalance(child)

    # checks the amount a child has in their checkings
    def childCheckChec(self, child):
        Child.checkChecBalance(child)

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
            return '---Parent Account Info---' + '\n' + \
                    'Name: ' + self.name + '\n' + \
                    'Savings Account: ' + str(self.__savbalance) + '\n' + \
                    'Checking Account: ' + str(self.__checbalance) + '\n' + '------------------'
        else:
            return 'The account number: "' + str(accountnum) + '" does not exist under the name: "' + self.name + '"'

    def __del__(self):
        # this is to make sure that when I delete a child account it also decreases the customer account
        Customer.customerCount -= 1
        Parent.parentCount -= 1
        del self
