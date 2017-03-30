from base import  *
from check_tools import *
import os

test = base()
test.func.append(check_magic_code)

dir_list = ['code']

def check_file(filename):
    test.open(filename)
    test.readfile()

for dir1 in dir_list:
    for root, dirs, files in os.walk(dir1):
        for filename in files:
            fullpath = os.path.join(root, filename)
            check_file(fullpath)
