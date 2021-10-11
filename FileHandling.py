from pathlib import Path
directory = Path("C:/Users/ohmpa/Documents/VScode/python/Files")
file_to_open = directory/"FileHandling.txt"

myfile = open(file_to_open, "w")
myfile.write('1. Hello this is line one')
myfile.close()

myfile = open(file_to_open, 'a')
myfile.write("\n2. This is line two")
myfile.close()


def displayFileContent():
    print("\n~~~~~~~~~File Content~~~~~~~~")
    myfile = open(file_to_open, 'r')
    print(myfile.read())
    myfile.close()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


def countSentences():
    myfile = open(file_to_open, 'r')
    linecount = 0

    for i in myfile:
        if i != "\n":
            linecount += 1
    myfile.close()
    return linecount


def countWords():
    myfile = open(file_to_open, 'r')
    content = myfile.read()
    words = content.split()
    wordcount = len(words)
    myfile.close()
    return wordcount


def charCount():
    myfile = open(file_to_open, 'r')
    content = myfile.read().replace(" ", "").replace('\n', '')
    count = len(content)
    myfile.close()
    return count


def countSpaces():
    myfile = open(file_to_open, 'r')
    count = 0
    content = myfile.read().replace('\n', '')
    myfile.close()

    for i in range(0, len(content)):
        if content[i] == " ":
            count += 1
    return count


def countDigits():
    myfile = open(file_to_open, 'r')
    digicount = 0
    content = myfile.read().replace('\n', '')
    myfile.close()

    for i in content:
        if i.isdigit():
            digicount += 1
        else:
            pass

    return digicount


def countLower():
    myfile = open(file_to_open, 'r')
    lowercount = 0
    content = myfile.read().replace('\n', '')
    myfile.close()

    for i in content:
        if i.islower():
            lowercount += 1
        else:
            pass

    return lowercount


def countUpper():
    myfile = open(file_to_open, 'r')
    uppercount = 0
    content = myfile.read().replace('\n', '')
    myfile.close()

    for i in content:
        if i.isupper():
            uppercount += 1
        else:
            pass

    return uppercount


# Driver code
displayFileContent()
print("Number of sentences: ", countSentences())
print("Number of words: ", countWords())
print("Number of characters: ", charCount())
print("Number of spaces: ", countSpaces())
print("Number of digits: ", countDigits())
print("Number of lowecase letters: ", countLower())
print("Number of uppercase letters: ", countUpper())
