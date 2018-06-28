class ATM:

    def __init__(self, customer):
        self.customer = customer
        self.interface()

    def deposit(self, amount, pin):
        return self.customer.atmDeposit(amount, pin)

    def withdraw(self, amount, pin):
        return self.customer.atmWithdraw(amount, pin)

    def interface(self):
        usedOnce = False
        uInput = ''
        while(uInput!='n'):
            if usedOnce:
                uInput = input('Would you like to make another transacion, ' + self.customer.name + ' (y) (n): ')
            else:
                uInput = input('Would you like to use the ATM, ' + self.customer.name + ' (y) (n): ')
            if uInput == 'y':
                option = ''
                while(option!='deposit' and option!='withdraw'):
                    option = input('Would you like to deposit or withdraw from the ATM (deposit) (withdraw): ')
                    if option == 'deposit':
                        amount = 0
                        try:
                            amount = int(input('How much would you like to deposit?: '))
                            pin = int(input('What is your PIN?: '))
                        except:
                            print('Invalid value, goodbye.')
                            break
                        self.deposit(amount, pin)
                        usedOnce = True
                    elif option == 'withdraw':
                        amount = 0
                        try:
                            amount = int(input('How much would you like to withdraw?: '))
                            pin = int(input('What is your PIN?: '))
                        except:
                            print('Invalid value, goodbye.')
                            break
                        print('Here is your money:', self.withdraw(amount, pin))
                        usedOnce = True
                    else:
                        print('Invalid input, try again. \n')

            elif uInput == 'n':
                print('Okay, have a wonderous day.')
            else:
                print('Invalid input, try again. \n')
