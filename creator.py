''' A simple class for file/folder creation, deletion etc optimized for hwbot '''

### IMPORTS ###
import sys
import os
import shutil
import subprocess
### GLOBALS ###

### CONSTANTS ###

### FUNCTIONS ###

### CLASSES ###

class Creator(object):
    ''' The creator class '''

    def __init__(self):
        ''' Initialized the creator by giving it a blank hwbot project name '''
        self.project_name = None
        return

    def set_project_name(self, name):
        ''' Set the project name '''
        self.project_name = name

    def get_project_name(self):
        ''' Return the proeject name '''
        return self.project_name

    @staticmethod
    def create_folder(name):
        ''' Create a new folder called name in the current directory if one
            doesn't already exist '''
        if not os.path.exists("./"+name):
            os.makedirs("./"+name)
            os.chdir("./"+name)

    @staticmethod
    def open_folder(name):
        ''' Open a folder in the current directory called name if one exists '''
        if os.path.exists("./"+name):
            os.chdir("./"+name)
        if os.path.exists(name):
            os.chdir(name)

    @staticmethod
    def delete_folder(name):
        ''' Delete a folder called name if it exists in the current directory'''
        if os.path.exists("./"+name):
            shutil.rmtree("./"+name)

    @staticmethod
    def open_file(name):
        ''' Open a file called name in the current directory if one exists '''
        if sys.platform.startswith('darwin'):
            subprocess.call(('open', "./"+name))
        elif os.name == 'nt':
            pass
            #os.startfile("./"+name)
        elif os.name == 'posix':
            subprocess.call(('xdg-open', "./"+name))

    @staticmethod
    def create_file(name):
        ''' Create a file called name if one doesn't exist in the current
            directory '''
        if not os.path.exists("./"+name):
            open(name, 'a')

    @staticmethod
    def delete_file(name):
        ''' Delete file name if it exists in the current directory '''
        if os.path.exists("./"+name):
            os.remove("./"+name)

    @staticmethod
    def copy_file(name):
        ''' Copy a file at path name if it exists '''
        if os.path.exists(name):
            shutil.copy2(name, "./")
