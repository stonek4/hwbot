### IMPORTS ###
import os
### GLOBALS ###

### CONSTANTS ###

### FUNCTIONS ###

### CLASSES ###
class Compiler(object):
    def __init__(self, md_file):
        self.md_file = open(md_file, 'w')

    def append_title(self, title, size):
        while (size > 0):
            self.md_file.write("#")
            size -= 1
        self.md_file.write(title)
        self.append_lines(2)

    def copy_file(self, file_name):
        with open(file_name, 'r') as afile:
            for line in afile:
                self.md_file.write(line)

    def append_text_file(self, text_file):
        self.copy_file(text_file)
        self.append_lines(2)

    def append_code_file(self, code_type, file_name):
        self.md_file.write("```"+code_type+"\n")
        self.copy_file(file_name)
        self.md_file.write("```")
        self.append_lines(2)

    def append_math_file(self, file_name):
        pass

    def append_picture(self, picture, name):
        self.md_file.write("!["+name+"]("+picture+")")
        self.md_file.append_lines(2)

    def append_text(self, text):
        self.md_file.write(text)
        self.md_file.append_lines(2)

    def append_lines(self, number):
        while number > 0:
            self.md_file.write("\n")

    def append_file(self, file_name):
        name, exten = os.path.splitext(file_name)
        if (exten == ".py"):
            self.append_code_file("python", file_name)
        elif (exten == ".math"):
            self.append_math_file(file_name)
        elif (exten == ".png"):
            self.append_picture(file_name, name)
        else:
            self.append_text_file(file_name)
