#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2018/day/1
"""

# Imports
import sys
import os
import re

# Global variables
task="d-1"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    rows = [n for n in readInput().split('\n')]
    frequencies = []
    for row in rows:
        m = re.match(r'([-+])', row)
        if m:
            frequencies.append(int(float(row)))

    freq = 0
    for inc in frequencies:
        freq += inc
    print("A): " + str(freq))

def b():
    rows = [n for n in readInput().split('\n')]
    frequencies = []

    for row in rows:
        m = re.match(r'([-+])', row)
        if m:
            frequencies.append(int(float(row)))

    freq = 0
    unique_freq = set('0')
    run = 0
    while run<1:
        for inc in frequencies:
            freq += inc
            if str(freq) in unique_freq:
                print("YEAH!!")
                run = 1
                break
            else:
                unique_freq.add(str(freq))

    print("B): " + str(freq))
    sys.exit(1)

# Main body
if __name__ == '__main__':
   # a()
    b()
    sys.exit(1)
