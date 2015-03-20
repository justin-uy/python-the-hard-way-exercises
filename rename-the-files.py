from sys import argv
from os import listdir
import shutil
import re

script, p = argv

def add_leading_0_to_single_digit_ex_files(path):
    for filename in listdir(path):
        if re.match(r'^ex[\d{1}].py', filename):
            num = int(re.findall(r'\d+', filename)[0])
            shutil.move(filename, 'ex0%d.py' % num)

add_leading_0_to_single_digit_ex_files(p)

