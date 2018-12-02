#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2018/day/1
"""

# Imports
import sys
import os
import re
from collections import Counter 

# Global variables
task="d-2"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def diff_letters(a,b):
    return sum ( a[i] != b[i] for i in range(len(a)) )

def filter_duplicate_letters(a,b):
    boxid = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            boxid += a[i]
    return boxid


def b():
    rows = [n for n in readInput().split('\n')]
    l = len(rows)
    index = 1
    boxid = ''
    for row in rows:
        for i in range(index, l):
            compw = rows[i]
            diff = diff_letters(row, compw)
            if diff == 1:    
                boxid = filter_duplicate_letters(row, compw)
#                print(row + " " + compw)
#                print(filter_duplicate_letters(row, compw))
        index += 1

    print("B): %s" % (boxid))
    sys.exit(1)

def a():
    rows = [n for n in readInput().split('\n')]
    checksums = []
    for row in rows:
        wc = Counter(row) 
        chs = set()
        for i in wc.values():
            if i > 1:
                chs.add(str(i))
        checksums.extend(list(chs))
 
    tmp = ''.join(checksums)
    wc = Counter(tmp)
    result = 1
    for key in wc:
        print(str(key) + " : " + str(wc[key]))
        result = result * wc[key]
 
    print("A): %d" % (result))



# Main body
if __name__ == '__main__':
    #a()
    b()
    sys.exit(1)
