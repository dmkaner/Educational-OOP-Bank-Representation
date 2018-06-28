import random
from Employee import *
from Customer import *

class Teller(Employee):

    # can only be initialized if manager logs in
    def __init__(self, name, age, phone, sex, paygrade, position, experience, username, password, manager):
        if manager.isManager():
            Employee.__init__(self, name, age, phone, sex, experience)
            # used encapsulation here because other users should not be able to access this information
            self.__username = username
            self.__password = password
            self.__employeeNumber = 100000 + random.randint(100, 999)
            self.__paygrade = paygrade
            self.position = position
            print('Employee created')
        else:
            print('Must be a manager to hire new Teller')

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

    # this method is to access the private var paygrade, only can be used by managers
    def setPaygrade(self, manager, paymentIncrease):
        if manager.isManager:
            self.__paygrade += paymentIncrease

    # implementing notification that lets tellers know they cannot delete user accounts
    def delCustomerAccount(self, customer):
        print('Tellers do not have permission to delete user accounts')

    # shows teller all the info they are allowed to see about a customer
    def seeCustomerDetails(self, customer):
        return customer.accessCustomerInfoTeller()
