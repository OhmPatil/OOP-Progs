class prime:
    def accept(self):
        self.lower = int(input("Enter starting number: "))
        self.upper = int(input("Enter end number: "))

    def isprime(self):
        for i in range(self.lower, self.upper + 1):
            if (i == 1):
                continue
            flag = 1
            for j in range(2, i // 2 + 1):
                if (i % j == 0):
                    flag = 0
                break
            if (flag == 1):
                print(i, end = " ")

test = prime()
test.accept()
test.isprime()