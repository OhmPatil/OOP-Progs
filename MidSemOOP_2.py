'''
Question 2: Write an Object Oriented program to generate passenger bus ticket by inputting information as Passenger id, passenger name, age, BusType
(AC, Standard, Regular) , distance to be covered in kms. For AC fair is 12 Rs/km. Standard 8Rs/km and Regular fair is 6Rs/km. Add passengers 
in a Bus till users choice and display the details with total amount collection for that trip in a bus.

@author : Ohm Patil
@rollno : 20124034
'''


class busTicket:
    def __init__(self):
        self.busType = 0
        self.distance = 0
        self.fare = 0

    def fareCalc(self):
        if (self.busType == 1):
            self.fare = 12 * self.distance
        elif (self.busType == 2):
            self.fare = 8 * self.distance
        elif (self.busType == 3):
            self.fare = 6 * self.distance
        else:
            print("Enter valid choice ! ")


class passenger(busTicket):
    def __init__(self):
        super().__init__()
        self.passName = None
        self.passID = 0
        self.passAge = 0

    def accept(self):
        self.passName = input("Enter passenger name: ")
        self.passAge = input("Enter passenger age: ")
        self.passID = input("Enter passenger ID: ")
        self.busType = int(input("\n1. AC\n2. Standard \n3. Regular\nEnter BUS TYPE: "))
        self.distance = int(input("Enter distance to be covered: "))

    def display(self):
        print("Name: ", self.passName)
        print("ID  : ", self.passID)
        print("Age : ", self.passAge)
        print("Bus Type: ", self.busType)
        print("Total fare: ", round(self.fare, 2))


# Driver code starts here
ctr = 0
objectList = []
objectList.append(passenger())
objectList[ctr].accept()
objectList[ctr].fareCalc()

condition = True
while condition == True:
    choice = input("Add another passenger?(y/n) : ")
    if choice == 'y':
        objectList.append(passenger())
        ctr += 1
        objectList[ctr].accept()
        objectList[ctr].fareCalc()
    else:
        for pas in objectList:
            pas.display()
            print()
        break
