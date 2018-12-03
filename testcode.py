#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2018/day/1
"""

# Imports
import sys
import os
import re

def a():

    exampleString = '''
    Jessica is 15 years old, and Daniel is 27 years old.
    Edward is 97 years old, and his grandfather, Oscar, is 102. 
    '''
    ages = re.findall(r'\d{1,3}',exampleString)
    names = re.findall(r'[A-Z][a-z]*',exampleString)

    print(ages)
    print(names)

    row = '#1 @ 12,3: 4x44'
    print(row)
    m = re.findall(r'\d+', row) 

    print(m)
    
# Main body
if __name__ == '__main__':
    a()
    sys.exit(1)
