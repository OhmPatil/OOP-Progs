#Read text from one file, convert to uppercase, write in another file.

from pathlib import Path
directory = Path("C:/Users/ohmpa/Documents/VScode/python/Files")

class lowerToUpper:
    def __init__(self):
        self.upper = None

    def writeFile1(self):
        myfile1 = open(directory/"file1.txt", 'w')
        myfile1.write("lowercase to uppercase")
        myfile1.close()

    def convertContent(self):
        myfile1 = open(directory/"file1.txt", 'r')
        content = myfile1.read()
        self.upper = content.upper()
        myfile1.close()

    def writeFile2(self):
        myfile2 = open(directory/"file2.txt", 'w')
        myfile2.write(self.upper)
        myfile2.close()

    def displayFileContent(self):
        myfile1 = open(directory/"file1.txt", 'r')
        myfile2 = open(directory/"file2.txt", 'r')
        print("Content of file 1: ", myfile1.read())
        print("Content of file 2: ", myfile2.read())
        myfile1.close()
        myfile2.close()

# Driver code
test = lowerToUpper()
test.writeFile1()
test.convertContent()
test.writeFile2()
test.displayFileContent()
