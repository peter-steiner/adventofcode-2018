#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2018/day/5
"""

# Imports
import sys
import os
import re

# Global variables
task="d-5"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def analysePolymer(polymer):
  for i in range(len(polymer)-1):
    sub = sorted([polymer[i], polymer[i+1]])
    if ''.join(sub).isalpha():
      if ord(sub[1])-ord(sub[0]) == 32:
        polymer[i] = '!'
        polymer[i+1] = '!'
        
  return polymer



def a():
    rows = [n for n in readInput().split('\n')]
    polymer = list(rows[0])
    
    while True:
      lenPol = len(polymer)
      polymer = list(''.join(analysePolymer(polymer)).replace('!', ''))
      if len(polymer) == lenPol:
        break

    modified_polymer = ''.join(analysePolymer(list(polymer)))

    print("A): ", len(list(modified_polymer)))

def b():
    rows = [n for n in readInput().split('\n')]
    originalPolymer = list(rows[0])
    
    minLengthPoly = 11546
    for ascii in range(65, 91):
      polymer = originalPolymer
      polymer = list(''.join(polymer).replace(chr(ascii), ''))
      polymer = list(''.join(polymer).replace(chr(ascii+32), ''))

      while True:
        lenPol = len(polymer)
        polymer = list(''.join(analysePolymer(polymer)).replace('!', ''))
        if len(polymer) == lenPol:
          break

      modified_polymer = ''.join(polymer)
      if len(modified_polymer) < minLengthPoly:
        minLengthPoly = len(modified_polymer)

    print("B): ", minLengthPoly)

# Main body
if __name__ == '__main__':
    a()
    b()
    sys.exit(1)
