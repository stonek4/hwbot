'''
HWBOT
v1.0

Organizing and creating hw has never been so easy!

Kevin Stoner
'''
### IMPORTS ###
from math import *
import os
import sys
import logging
import argparse
from md_compile import Compiler
from creator import Creator
### GLOBALS ###

### CONSTANTS ###

### FUNCTIONS ###
def setup_logging():
    ''' Setup the logging library '''
    logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.debug("Logging Started...")

def display_options(which):
    ''' Allow the user to input a new command '''
    parser = argparse.ArgumentParser()
    first_arg = ["create", "edit", "exit"]
    second_arg = []

    print "Current Directory: " + os.getcwd()
    for proj_file in os.listdir("./"):
        print proj_file
    print ""

    if which == 1:
        second_arg += ["project"]
    elif which >= 2:
        first_arg += ["compile", "delete", "add"]
        second_arg += ["q", "file"]
        if which >= 3:
            second_arg += ["sq"]
        else:
            second_arg += ["ssq"]

    parser.add_argument("command",
                        type=str,
                        choices=first_arg,
                        help="the command to be run")
    parser.add_argument("c_type",
                        nargs='?',
                        type=str,
                        choices=second_arg,
                        help="the type to perform the command on")
    parser.add_argument("name",
                        nargs='?',
                        type=str,
                        help="""define the folder name, file number
                        (ex: for Question 1, enter '1'), or path to file""")
    while True:
        try:
            input_args = input(" ~hwbot~: ").split(" ")
            output = parser.parse_args(input_args)
            break
        except Exception as e:
            print e

    return output

def navigate_to(name):
    ''' Navigate to a parent file called name '''
    while True:
        curr_dir = os.getcwd().split(os.sep)[-1]
        if curr_dir == name or curr_dir.split('_')[0] == name:
            amax = 0
            for adir in os.listdir("./"):
                if os.path.isdir("./" + adir):
                    num = int(adir.split('_')[1])
                    if num > amax:
                        amax = num
            return amax + 1
        else:
            os.chdir("../")

def get_file_number():
    ''' Get the next usable file number in a directory and return it '''
    amax = 0
    for adir in os.listdir("./"):
        if os.path.isfile("./" + adir):
            num = int(adir.split('_')[1].split('.')[0])
            if num > amax:
                amax = num
    return amax + 1

def get_file(fnum):
    ''' Get a file by number '''
    for adir in os.listdir("./"):
        if os.path.isfile("./" + adir):
            num = int(adir.split('_')[1].split('.')[0])
            if num == fnum:
                return adir
    return None

def md_compile(compiler, exclude):
    ''' Compile the assignment using the compile class '''
    file_list = []
    dir_list = []
    for adir in os.listdir():
        if adir not in exclude:
            if os.path.isfile("./" + adir):
                file_list.append("./" + adir)
            else:
                dir_list.append("./" + adir)
    print (file_list, dir_list)
    file_list.sort(key=lambda a: a.split("_")[1].split(".")[0])
    for afile in file_list:
        compiler.append_file(afile)

    dir_list.sort(key=lambda a: a.split("_")[1].split(".")[0])
    for adir in dir_list:
        os.chdir(adir)
        compiler.append_title("QUESTION " + adir.split("_")[1], 2)
        compile(compiler, exclude)
        os.chdir("../")

def parse_input(creator, command, option):
    ''' Parse the commands that were input '''
    if command.command == "create":
        if command.c_type == "project":
            creator.set_project_name(command.name)
            creator.create_folder(command.name)
            option = 2
        elif command.c_type == "q":
            name = "Q_" + str(navigate_to(creator.get_project_name()))
            creator.create_folder(name)
            option = 3
        elif command.c_type == "sq":
            name = "SQ_" + str(navigate_to("Q"))
            creator.create_folder(name)
            option = 4
        elif command.c_type == "ssq":
            name = "SSQ_" + str(navigate_to("SQ"))
            creator.create_folder(name)
            option = 4
        elif command.c_type == "file":
            name = "F_" + str(get_file_number()) + "." + command.name
            creator.create_file(name)
            creator.open_file(name)

    if command.command == "edit":
        if command.c_type == "project":
            creator.set_project_name(command.name)
            creator.open_folder(command.name)
            option = 2
        elif command.c_type == "q":
            name = "Q_" + command.name
            navigate_to(creator.get_project_name())
            creator.open_folder(name)
            option = 3
        elif command.c_type == "sq":
            name = "SQ_" + command.name
            navigate_to("Q")
            creator.open_folder(name)
            option = 4
        elif command.c_type == "ssq":
            name = "SSQ_" + command.name
            navigate_to("SQ")
            creator.open_folder(name)
            option = 4
        elif command.c_type == "file":
            name = get_file(int(command.name))
            creator.open_file(name)

    if command.command == "delete":
        if command.c_type == "q":
            name = "Q_" + command.name
            creator.delete_folder(name)
        elif command.c_type == "sq":
            name = "SQ_" + command.name
            creator.delete_folder(name)
        elif command.c_type == "ssq":
            name = "SSQ_" + command.name
            creator.delete_folder(name)
        elif command.c_type == "file":
            name = get_file(int(command.name))
            creator.delete_file(name)

    if command.command == "add":
        if command.c_type == "file":
            creator.copy_file(command.name)

    if command.command == "exit":
        sys.exit(0)

    if command.command == "compile":
        navigate_to(creator.get_project_name())
        md_file = "./" + creator.get_project_name() + ".md"
        creator.create_file(md_file)
        compiler = Compiler(md_file)
        compile(compiler, [creator.get_project_name()+".md"])

    return option



### CLASSES ###

### MAIN ###
def main():
    ''' Main '''
    option = 1
    creator = Creator()
    command = display_options(option)
    while True:
        option = parse_input(creator, command, option)
        command = display_options(option)






if __name__ == "__main__":
    main()
