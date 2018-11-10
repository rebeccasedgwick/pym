# Use of os module in CL to list current directory's files & directories
import os


def view_dir(path='.'):
    names = os.listdir(path)
    names.sort()
    for name in names:
        print(name, end='\n')
