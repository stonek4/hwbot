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

    def delete_folder(self, name):
        if os.path.exists("./"+name):
            shutil.rmtree("./"+name)

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

    def delete_file(self, name):
        if os.path.exists("./"+name):
            os.remove("./"+name)

    def copy_file(self, name):
        if os.path.exists(name):
            shutil.copy2(name, "./")
