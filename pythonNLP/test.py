from curses.ascii import isdigit
import re
filepath = 'C:/Users/DELL/Desktop/vckg_concept.txt'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        for c in line:
            if c.isdigit():
                


