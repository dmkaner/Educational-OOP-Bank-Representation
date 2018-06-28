import random
from Employee import *

class Manager(Employee):

    def __init__(self, name, age, phone, sex, experience, username, password):
        Employee.__init__(self, name, age, phone, sex, experience)
        # used encapsulation here because other users should not be able to access this information
        self.__username = username
        self.__password = password
        self.__paygrade = 40000 + (self.experience * 750)
        self.__employeeNumber = 100000 + random.randint(100, 999)

    # Same as in the customer class, want the print method to give basic information
    def __str__(self):
        try:
            checkuser = input("What is your username: ")
            checkpass = input("What is your password: ")
            if checkuser == self.__username and checkpass == self.__password:
                return '---Employee Info---' + '\n' + \
                       'Name: ' + self.name + '\n' + \
                       'Employee Number: ' + str(self.__employeeNumber) + '\n' + \
                       'Experience: ' + str(self.experience) + '\n' + \
                       'Paygrade: ' + str(self.__paygrade) + '\n' + '------------------'
            else:
                return 'The username and password did not match'
        except (TypeError, AttributeError):
            return 'The username and password did not match'


    # give promotion to other employees
    def givePromotion(self, employee, paymentIncrease):
        employee.setPaygrade(self, paymentIncrease)

    # called method to validate that a manager is making the call to increase pay
    def isManager(self):
        checkuser = input("Manager username: ")
        checkpass = input("Manager password: ")
        if checkuser == self.__username and checkpass == self.__password:
            return True
        return False

    # this method is to access the private var paygrade, only can be used by managers
    def setPaygrade(self, manager, paymentIncrease):
        print('Managers cannot set their own pay grade')

    # manager is allowed to delete a customer
    def delCustomerAccount(self, customer):
        del customer

    # employees must be hired through the manager, manager login information must be provided
    def hireEmployee(self):

        print('---Hiring Employee---')
        name = input("Employee Name: ")
        age = input("Employee Age: ")
        phone = input("Employee Phone: ")
        sex = input("Employee Sex: ")
        paygrade = input("Employee Pay Grade: ")
        position = input("Employee Position (teller): ")
        experience = input("Employee Experience: ")
        username = input("Employee Username: ")
        password = input("Employee Password: ")

        if position == 'teller':
            return Teller(name, age, phone, sex, paygrade, position, experience, username, password, self)
        else:
            return

    # shows manager all info about customer account
    def seeCustomerDetails(self, customer):
        return customer.accessCustomerInfoManager(self)
