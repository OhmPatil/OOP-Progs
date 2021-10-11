# Count occurrences of each word in sentence

from pathlib import Path
directory = Path("C:/Users/ohmpa/Documents/VScode/python/Files")
file_path = directory/"FileHandling3.txt"


class wordCount:

    def open_file(self):
        myfile = open(file_path, 'r')
        self.file_content = myfile.read()
        self.separated_words = self.file_content.split()
        self.unique_words = []

    def count_Display(self):
        for i in self.separated_words:
            if i not in self.unique_words:
                self.unique_words.append(i)

        for i in range(0, len(self.unique_words)):
            print(self.unique_words[i], "occurs",
                  self.separated_words.count(self.unique_words[i]), "times.")

        myfile.close()


object = wordCount()
object.open_file()
object.count_Display()
