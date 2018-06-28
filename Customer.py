from Person import *
import random

class Customer(Person):

    customerCount = 0

    def __init__(self, name, age, phone, sex, accountnum, savbalance, checbalance):
        Person.__init__(self, name, age, phone, sex)
        Customer.customerCount += 1

        # using encapsulation on variables so they cannot be seen
        # unless printing the object, which requires an account number
        self.__accountnum = accountnum
        self.__savbalance = savbalance
        self.__checbalance = checbalance
        self.__pin = random.randint(1000,9999)

        # print pin number on creation so user will know it. this is the only time it will be displayed
        # varaible will primarily be used by ATM class
        print(self.name + "'s Assigned Pin Number:", self.__pin)

    # return amount of customers
    @classmethod
    def amountOfCustomer(cls):
        return cls.customerCount

    # provides user access to customer support so they may ask questions and get help
    def accessCustomerSupport(self):
        return 'Login: USER | Web address: www.example.com'

    # getter method to display account info to managers
    def accessCustomerInfoManager(self, manager):
        if manager.isManager():
            return '---Account Info---' + '\n' + \
                   'Name: ' + self.name + '\n' + \
                   'Savings Account: ' + str(self.__savbalance) + '\n' + \
                   'Checking Account: ' + str(self.__checbalance) + '\n' + '------------------'
        else:
            return 'Must be a manager to view all info'

    # getter method to display account info to tellers
    def accessCustomerInfoTeller(self):
        return '---Account Info---' + '\n' + \
                   'Name: ' + self.name + '\n' + '------------------'

    # make deposit
    def deposit(self, amount):
        self.__checbalance += amount
        print('*****ACTION COMPLETE*****')

    # make withdrawal; must provide accountnum for security purposes; will return a value so assign it to a varaible
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

    # transfer funds from one account to the account that is provided
    def transferFunds(self, amount, account):
        try:
            val = self.withdrawal(self.__accountnum, amount)
            account.deposit(val)
        except (TypeError, AttributeError):
            print('Transaction could not be completed')

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

    # this is so they dont have to use the print method every time, displays savings account only
    def checkSavBalance(self):
        accountnum = int(input('Enter the account number: '))
        if accountnum == self.__accountnum:
            print(self.name + ' has ' + "$" + str(self.__savbalance))
        else:
            print('The account number: "' + str(accountnum) + '" does not exist under the name: "' + self.name + '"')

    # method to check checking account only
    def checkChecBalance(self):
        accountnum = int(input('Enter the account number: '))
        if accountnum == self.__accountnum:
            print(self.name + ' has ' + "$" + str(self.__checbalance))
        else:
            print('The account number: "' + str(accountnum) + '" does not exist under the name: "' + self.name + '"')

    # returns account details in a nice format; must provide account number for security purposes
    def __str__(self):
        accountnum = int(input('Enter the account number: '))
        if accountnum == self.__accountnum:
            return '---Account Info---' + '\n' + \
                    'Name: ' + self.name + '\n' + \
                    'Savings Account: ' + str(self.__savbalance) + '\n' + \
                    'Checking Account: ' + str(self.__checbalance) + '\n' + '------------------'
        else:
            return 'The account number: "' + str(accountnum) + '" does not exist under the name: "' + self.name + '"'

    # delete self
    def __del__(self):
        Customer.customerCount -= 1
        del self
