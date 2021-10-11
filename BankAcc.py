class BankAccount:
    def __init__(self):
        self.CustName = None
        self.CustId = 0

    def AcceptCustDetails(self):
        self.CustName = str(input("Enter your name: "))
        self.CustId = int(input("Enter your ID: "))

    def displayCustDetails(self):
        print("\nWelcome", self.CustName, "(ID:", self.CustId, ")")

    def displayBank(self):
        print("\n\t\tBANK OF INDIA\n")
        print("Choose your service from below options (Enter your choice) :\n1. Savings Account\n2. Fixed Deposit\n")

    def displayTransType(self):
        print("\nChoose your transaction type:\n1. Withdrawal\n2. Deposit")

    def display(self):
        print("Your balance is: ", self.accbal)


class SavingsAccount(BankAccount):
    def __init__(self):
        self.accbal = 5000

    def Withdraw(self, amount):
        if(amount > self.accbal):
            print("Amount cant exceed", self.accbal, "!")
        else:
            self.accbal -= amount
            print("Your updated balance is: ", self.accbal)

    def Deposit(self, amount):
        self.accbal += amount
        print("Your updated balance is: ", self.accbal)


class FixedDepositAccount(BankAccount):
    def __init__(self):
        self.accbal = 5000
        self.principle = 0
        self.years = 0
        self.rate = 6.7

    def FixedAccept(self):
        self.principle = int(input("Enter principle amount: "))
        self.years = int(input("Enter number of years: "))

    def AmountCal(self):
        self.accbal = self.principle*(1+self.rate/100)*self.years

    def FixedDisplay(self):
        print("The bank rate is currently ", self.rate,"%, you will receive ", self.accbal, " after ", self.years, " years")


# Simply accepting customer details and displaying stuff
customer = BankAccount()
customer.AcceptCustDetails()
customer.displayCustDetails()
customer.displayBank()


# Main driver code starts here
choice = int(input("Enter your choice: "))

if (choice == 1):
    save = SavingsAccount()
    save.display()
    save.displayTransType()
    transchoice = int(input("\nEnter choice: "))
    if (transchoice == 1):
        amt = int(input("Enter amount to be withdrawn: "))
        save.Withdraw(amt)

    elif (transchoice == 2):
        amt = int(input("Enter amount to be deposited: "))
        save.Deposit(amt)

    else:
        print("Enter valid choice !")

elif (choice == 2):
    fixed = FixedDepositAccount()
    fixed.FixedAccept()
    fixed.AmountCal()
    fixed.FixedDisplay()
else:
    print("Please anter valid choice !")
