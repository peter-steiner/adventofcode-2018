#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2018/day/4
"""

# Imports
import sys
import os
import re

# Global variables
task="d-4-t"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    rows = [n for n in readInput().split('\n')]

    print("A): ")

def b():
    rows = [n for n in readInput().split('\n')]
   
    print("B): ")

# Main body
if __name__ == '__main__':
    a()
    b()
    sys.exit(1)
