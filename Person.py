class Person:

    def __init__(self, name, age, phone, sex):
        self.name = name
        self.age = age
        self.phone = phone
        self.sex = sex

    # informs those who are not associated with the bank that they do not have access to customer support
    def accessCustomerSupport(self):
        return 'You must be a customer or an employee of the bank to receive access information to customer support'
