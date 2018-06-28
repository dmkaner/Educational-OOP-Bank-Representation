from Person import *

class Employee(Person):

    employeeAmount = 0

    def __init__(self, name, age, phone, sex, experience):
        Person.__init__(self, name, age, phone, sex)
        Employee.employeeAmount += 1
        self.experience = experience

    # Same as in the customer class, want the print method to give basic information
    def __str__(self):
        raise NotImplementedError("Should have implemented this")

    # returns the amount of money they make per year based off of experience
    def paygrade(self):
        checkuser = input("What is your username: ")
        checkpass = input("What is your password: ")
        if checkuser == self.__username and checkpass == self.__password:
            return self.name + " makes " + str(self.__paygrade) + " per year!"

        else:
            return "This username and password do not match"

    # retrieves the employee number for the employee
    def getEmployeeNumber(self):
        checkuser = input("What is your username: ")
        checkpass = input("What is your password: ")
        if checkuser == self.__username and checkpass == self.__password:
            return 'Your employee number is ' + str(self.__employeeNumber)
        else:
            return "This username and password do not match"

    # Get the amount of overall employees
    @classmethod
    def employeeCount(cls):
        return cls.employeeAmount

    # delete employee instance: want to add a way to quit and to get fired
    def __del__(self):
        Employee.employeeAmount -= 1
        del self

    # This is if the employee wants to change his password
    # Probably want to move this to the main class
    def changePassword(self):
        checkuser = input("What is your username: ")
        checkpass = input("What is your password: ")
        if checkuser == self.__username and checkpass == self.__password:
            first = input("What would you like your new password to be? ")
            second = input("Please enter new password again: ")

            if first == second:
                self.__password = first
                print("Password changed!")
            else:
                print('Your passwords did not match!')
        else:
            return "This username and password do not match"

    # provides admin access to customer support so they may login to help customers
    def accessCustomerSupport(self):
        return 'Admin access login: ROOT | Web address: www.example.com'

    # this method is to access the private var paygrade, only can be used by managers
    def setPaygrade(self, manager, paymentIncrease):
        raise NotImplementedError("Should have implemented this")

    # this method will let an employee delete a customer if the employee is a manager
    def delCustomerAccount(self, customer):
        raise NotImplementedError("Should have implemented this")

    # this method will allow an employee see as much of the customer's info as they are allowed
    def seeCustomerDetails(self, customer):
        raise NotImplementedError("Should have implemented this")
