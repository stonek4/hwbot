''' A compiler class for turning files and text into a markdown file '''
### IMPORTS ###
import os
### GLOBALS ###

### CONSTANTS ###

### FUNCTIONS ###

### CLASSES ###
class Compiler(object):
    ''' The compiler class '''

    def __init__(self, md_file):
        ''' Initialize the class by giving it a markdown file path '''
        self.md_file = open(md_file, 'w')

    def append_title(self, title, size):
        ''' Append the title text with a header of size '''
        while size > 0:
            self.md_file.write("#")
            size -= 1
        self.md_file.write(title)
        self.append_lines(2)

    def copy_file(self, file_name):
        ''' Copy all of the lines of a file into the md file '''
        with open(file_name, 'r') as afile:
            for line in afile:
                self.md_file.write(line)

    def append_text_file(self, text_file):
        ''' Append a text file '''
        self.copy_file(text_file)
        self.append_lines(2)

    def append_code_file(self, code_type, file_name):
        ''' Append a code file using the code_type '''
        self.md_file.write("```"+code_type+"\n")
        self.copy_file(file_name)
        self.md_file.write("```")
        self.append_lines(2)

    def append_math_file(self, file_name):
        ''' Append a math file '''
        pass

    def append_picture(self, picture, name):
        ''' Append a picture '''
        self.md_file.write("!["+name+"]("+picture+")")
        self.md_file.append_lines(2)

    def append_text(self, text):
        ''' Append text '''
        self.md_file.write(text)
        self.md_file.append_lines(2)

    def append_lines(self, number):
        ''' Append a number of blank lines '''
        while number > 0:
            self.md_file.write("\n")
            number -= 1

    def append_file(self, file_name):
        ''' Given a file name, attempt to append it '''
        name, exten = os.path.splitext(file_name)
        if exten == ".py":
            self.append_code_file("python", file_name)
        elif exten == ".math":
            self.append_math_file(file_name)
        elif exten == ".png":
            self.append_picture(file_name, name)
        else:
            self.append_text_file(file_name)
