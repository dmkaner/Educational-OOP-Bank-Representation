from Person import *
from Employee import *
from Teller import *
from Manager import *
from Customer import *
from ATM import *
from Child import *
from Parent import *

def main():

    # Test Cases

    '''
    dylan = Customer("Dylan", 19, 724, "MALE", 123, 10000, 2000)
    print(dylan.accessCustomerSupport())
    print(dylan)
    money = dylan.withdrawal(123, 200)
    print(money)
    money2 = dylan.withdrawal(123, 2000)
    print(money2)
    money3 = dylan.withdrawal(123456789, 200)
    print(money3)
    dylan.deposit(5000000)
    dylan.deposit(5000000)
    print(Customer.amountOfCustomer())
    del(dylan)
    print(Customer.amountOfCustomer())
    '''

    '''
    dylan = Customer("Dylan", 19, 724, "MALE", 123, 10000, 2000)
    dylan2 = Customer("Dylan2", 19, 724, "MALE", 123, 90, 2000)
    print(dylan)
    print(dylan2)
    dylan.transferFunds(10, dylan2)
    print(dylan)
    print(dylan2)
    '''

    '''
    eric = Employee('Eric', 19, 7245491059, 'Male', 14, 'ewb5319', 'hello')
    #print(eric.paygrade())
    #print(eric.accessCustomerSupport())
    #print(eric.getEmployeeNumber())
    #eric.changePassword()
    print(eric)
    print(Employee.employeeCount())
    del(eric)
    print(Employee.employeeCount())

    eric = Employee('Eric', 19, 7245491059, 'Male', 14, 'ewb5319', 'hello')
    print(eric)
    dude = Manager('dude', 19, 12345678, 'Male', 14, 'asdf', 'asdf')
    dude.givePromotion(eric, 1500)
    print(eric)
    '''

    '''
    dude = Manager('dude', 19, 12345678, 'Male', 14, 'asdf', 'asdf')
    dylan2 = Customer("Dylan", 19, 724, "MALE", 123, 10000, 2000)
    eric = Teller('Eric', 19, 7245491059, 'Male', 14, 1234, 1234, 'ewb5319', 'hello', dude)

    print(eric)
    print(dylan2)

    print(dude.seeCustomerDetails(dylan2))
    print(eric.seeCustomerDetails(dylan2))
    '''

    '''
    dylan2 = Customer("Dylan", 19, 724, "MALE", 123, 10000, 2000)
    print(dylan2)
    ATM(dylan2)
    print(dylan2)
    '''

    '''
    eric3 = Child('Eric', 14, 724, 'Male', 1234, 1000.50, 1000.50)
    print(eric3)
    print(Customer.amountOfCustomer())
    print(Child.amountOfChildren())
    eric3.deposit(500)
    eric3.checkChecBalance()
    eric3.checkSavBalance()
    print(eric3)
    '''


    eric = Child('Eric', 14, 724, 'Male', 1, 1000, 1000)
    ATM(eric)
    dude = Manager('dude', 19, 12345678, 'Male', 14, 'asdf', 'asdf')
    print(dude.seeCustomerDetails(eric))
    print(Customer.amountOfCustomer())
    del eric
    print(Customer.amountOfCustomer())
    '''
    eric2 = Adult('Eric2', 19, 724, 'Male', 2, 1000, 1000)
    '''
    '''
    eric.checkChecBalance()
    eric2.checkChecBalance()
    eric.deposit(20)
    eric2.deposit(20)
    eric.checkChecBalance()
    eric2.checkChecBalance()

    eric2.childDeposit(20, eric)
    eric.checkChecBalance()

    eric2.withdrawal(2,20)
    eric2.checkChecBalance()
    '''
    '''
    print(Customer.amountOfCustomer())
    print(Adult.amountOfAdults())
    print(Child.amountOfChildren())
    del(eric)
    del(eric2)
    print(Customer.amountOfCustomer())
    print(Adult.amountOfAdults())
    print(Child.amountOfChildren())
    '''


if __name__ == "__main__":
    main()
