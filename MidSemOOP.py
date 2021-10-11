'''
Question 1 : Write a OOP program to create a class Circle which is inherited to class Cylinder. Input appropriate data and find Area of Circle : PI * radius2
Circumference of Circle : 2 * PI * radius Volume of Cylinder : PI * radius2 * height. Define suitable methods, constructors, properties to implement the same.

@author: Ohm Patil
@rollno: 20124034
'''


class Circle:
    def __init__(self):
        self.radius = 0
        self.pi = 3.14
        self.circArea = 0
        self.circumference = 0

    def accept(self):
        self.radius = float(input("Enter radius of circle: "))
        self.calcArea(self.radius)
        self.calcCircumference(self.radius)

    def calcArea(self, radius):
        self.circArea = (self.pi * pow(radius, 2))

    def calcCircumference(self, radius):
        self.circumference = round((2 * self.pi * radius), 2)

    def display(self):
        print("Area of circle: ", self.circArea)
        print("Circumference of circle: ", self.circumference)


class Cylinder(Circle):
    def __init__(self):
        super().__init__()
        self.height = 0
        self.cylinderVol = 0

    def accept(self):
        super().accept()
        self.height = float(input("Enter height of cylinder: "))
        self.calcVolCylinder(self.radius, self.height)

    def calcVolCylinder(self, radius, height):
        self.cylinderVol = (self.pi * pow(radius, 2) * height)

    def display(self):
        super().display()
        print("Volume of cylinder: ", self.cylinderVol)


# Driver code starts here
cylinder1 = Cylinder()
cylinder1.accept()
cylinder1.display()


''' This program was not to be done by me. I did it by mistake but still submitting this as told by you. PLEASE allow my late submission.'''
