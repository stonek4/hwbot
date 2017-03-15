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
    """ Setup the logging library """
    logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.debug("Logging Started...")

def display_options(which):
    parser = argparse.ArgumentParser()
    first_arg = ["create","edit","exit"]
    second_arg = []

    print ("Current Directory: "+os.getcwd())
    for f in os.listdir("./"):
        print (f)
    print ("")

    if (which == 1):
        second_arg += ["project"]
    if (which >= 2):
        first_arg += ["compile", "delete", "add"]
        second_arg += ["q", "file"]
        if (which >= 3):
            second_arg += ["sq"]
        if (which >= 4):
            second_arg += ["ssq"]

    parser.add_argument("command", type=str, choices=first_arg, help="the command to be run")
    parser.add_argument("c_type", nargs='?', type=str, choices=second_arg, help="the type to perform the command on")
    parser.add_argument("name", nargs='?', type=str, help="define the folder name, file number (ex: for Question 1, enter '1'), or path to file")
    while True:
        try:
            input_args = input(" ~hwbot~: ").split(" ")
            output = parser.parse_args(input_args)
            break
        except Exception as e:
            print (e)

    return output

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

def get_file(fnum):
    for dr in os.listdir("./"):
        if (os.path.isfile("./"+dr)):
            num = int(dr.split('_')[1].split('.')[0])
            if (num == fnum):
                return dr
    return None

def compile(compiler, exclude):
    file_list = []
    dir_list = []
    for dr in os.listdir():
        if (dr not in exclude):
            if (os.path.isfile("./"+dr)):
                file_list.append("./"+dr)
            else:
                dir_list.append("./"+dr)
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
    option = 1
    creator = Creator()
    command = display_options(option)
    while True:
        option = parse_input(creator, command, option)
        command = display_options(option)






if __name__ == "__main__":
    main()
