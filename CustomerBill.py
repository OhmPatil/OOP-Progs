class Customer:
    '''def __init__(self, cid, name, units):
        self.customerId = cid
        self.customerName = name
        self.units = units'''

    def bill(self):
        if self.units <= 50:
            amount = self.units * 0.5

        elif self.units <= 100:
            amount = ((self.units - 50) * 0.75) + 25

        elif self.units <= 150:
            amount = ((self.units - 100) * 1.2) + 25 + (50 * 0.75)

        elif self.units <= 250:
            amount = ((self.units - 150) * 1.5) + 25 + (50 * 0.75) + (50 * 1.2)

        elif self.units > 251:
            amount = ((self.units - 250) * 2.3) + 25 + \
                (50 * 0.75) + (50 * 1.2) + (50 * 1.5)

        finalamount = amount + (amount * 0.2)

        return finalamount

    def accept(self):
        self.customerId = int(input("Enter Customer ID: "))
        self.customerName = input("Enter name: ")
        self.units = int(input("Enter Units: "))

    def display(self):
        print("ID: ", self.customerId)
        print("Name: ", self.customerName)


cust1 = Customer()

cust1.accept()
cust1.display()
print("Your bill amounts to Rs. ", str(cust1.bill()))
