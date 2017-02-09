### IMPORTS ###
from math import *
from builtins import input
import logging
import sys
import os
import subprocess
### GLOBALS ###

### CONSTANTS ###

### FUNCTIONS ###
def setup_logging():
    """ Setup the logging library """
    logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.debug("Logging Started...")

def display_options(which):
    #TODO: Support deletes
    print ("Available Commands: ")
    if (which == 1):
        print ("1 - Create New Assignment")
        print ("2 - Open An Existing Assignment")
    if (which >= 2):
        print ("1 - Create New Question (1.)")
        print ("2 - Edit a Question")
        if (which >= 3):
            print ("3 - Create New Subquestion (a.)")
            print ("4 - Edit a Subquestion")
        if (which >= 4):
            print ("5 - Create New Sub-Subquestion (i.)")
            print ("6 - Edit a Sub-Subquestion")
        print ("7 - Create a MATH File (.math)")
        print ("8 - Create a TEXT File (.txt)")
        print ("9 - Add a Picture File (.png)")
        print ("10 - Edit a file")
        print ("11 - Compile the assignment (.md)")

    print ("0 - Exit")
    print ("")
    print ("Current Directory:",os.getcwd())
    print ("Files: ")
    for file in os.listdir("./"):
        print (file)
    print ("")
    return input("Please input a command: ")

def navigate_to(name):
    while True:
        cd = os.getcwd().split(os.sep)[-1]
        if (cd == name or cd.split('_')[0] == name):
            mx = 0
            for dr in os.listdir("./"):
                if (os.path.isdir("./"+dr)):
                    num = int(dr.split('_')[1])
                    if num > mx:
                        mx = num
            return mx + 1
        else:
            os.chdir("../")

def get_file_number():
    mx = 0
    for dr in os.listdir("./"):
        if (os.path.isfile("./"+dr)):
            num = int(dr.split('_')[1].split('.')[0])
            if num > mx:
                mx = num
    return mx + 1



### CLASSES ###
class Creator(object):
    def __init__(self):
        self.project_name = None
        return

    def set_project_name(self, name):
        self.project_name = name

    def get_project_name(self):
        return self.project_name

    def create_folder(self, name):
        if not os.path.exists("./"+name):
            os.makedirs("./"+name)
            os.chdir("./"+name)

    def open_folder(self, name):
        if os.path.exists("./"+name):
            os.chdir("./"+name)
        if os.path.exists(name):
            os.chdir(name)

    def open_file(self, name):
        if sys.platform.startswith('darwin'):
            subprocess.call(('open', "./"+name))
        elif os.name == 'nt':
            os.startfile("./"+name)
        elif os.name == 'posix':
            subprocess.call(('xdg-open', "./"+name))

    def create_file(self, name):
        if not os.path.exists("./"+name):
            open(name, 'a')



### MAIN ###
def main():
    command = 1
    creator = Creator()
    command = int(display_options(1))
    while command != 0:
        if (command == 1):
            name = input("Please enter the name of the Assignment: ")
            creator.set_project_name(name)
            creator.create_folder(name)
        if (command == 2):
            name = input("Please enter the name of the Assignment: ")
            creator.set_project_name(name)
            creator.open_folder(name)
        command = int(display_options(2))
        last_option = 2
        while command != 0:
            if (command == 1):
                name = "Q_" + str(navigate_to(creator.get_project_name()))
                creator.create_folder(name)
                command = int(display_options(3))
                last_option = 3
            if (command == 2):
                name = "Q_" + input("Please enter the question number: ")
                navigate_to(creator.get_project_name())
                creator.open_folder(name)
                command = int(display_options(3))
                last_option = 3
            if (command == 3):
                name = "SQ_" + str(navigate_to("Q"))
                creator.create_folder(name)
                command = int(display_options(4))
                last_option = 4
            if (command == 4):
                name = "SQ_" + input("Please enter the subquestion number: ")
                navigate_to("Q")
                creator.open_folder(name)
                command = int(display_options(4))
                last_option = 4
            if (command == 5):
                name = "SSQ_" + str(navigate_to("SQ"))
                creator.create_folder(name)
                command = int(display_options(4))
                last_option = 4
            if (command == 6):
                name = "SSQ_" + input("Please enter the sub-subquestion number: ")
                navigate_to("SQ")
                creator.open_folder(name)
                command = int(display_options(4))
                last_option = 4
            if (command == 7):
                name = "F_" + str(get_file_number()) + ".math"
                creator.create_file(name)
                creator.open_file(name)
                command = int(display_options(last_option))
            if (command == 8):
                name = "F_" + str(get_file_number()) + ".txt"
                creator.create_file(name)
                creator.open_file(name)
                command = int(display_options(last_option))
            if (command == 9):
                pass
            if (command == 10):
                name = input("Please enter the number of the file: ")
                creator.open_file(name)
                command = int(display_options(last_option))



if __name__ == "__main__":
    main()
