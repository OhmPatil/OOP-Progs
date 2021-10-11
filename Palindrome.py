class palindrome:
    def accept(self):
        self.str = str(input("Enter a string: "))

    def reverse(self):
        self.rev_str = reversed(self.str)
        return(list(self.rev_str) == list(self.str))

    def display(self):
        if (self.reverse()):
            print("Palindrome")
        else:
            print("Not Palindrome")


test = palindrome()
test.accept()
test.reverse()
test.display()
