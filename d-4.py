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
task="d-4"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data


class Guard:
    id = None
    minutes = []
    totalsleep = 0
    sleepStart = 0
    def __init__(self, id_):
        self.id = id_
        self.minutes = [0 for i in range(5959)]

    def sleep(self, start):
        self.sleepStart = start
    
    def stopSleep(self, stop): 
        self.totalsleep += stop-self.sleepStart
        for time in range(self.sleepStart, stop):
            self.minutes[time] = self.minutes[time] + 1
        self.sleepStart = 0

    def getIndex(self):
        return self.minutes.index(max(self.minutes))

    def getMaxOccurence(self):
        return max(self.minutes)
    
    def getTotalsleep(self):
        return self.totalsleep
    
    def getCalculatedHash(self):
        return self.getIndex() * int(self.id.replace('#', ''))

    def __eq__(self, other): 
        return self.id == other.id

    def __str__(self):
        return "[{0}]:|{1}| max occasions: {2}, {3}".format(self.id, self.totalsleep, max(self.minutes), self.minutes.index(max(self.minutes)))


def a():
    rows = [n for n in readInput().split('\n')]

    rows = sorted(rows)
    guards = {}
    for row in rows:
        m = re.findall(r'(\d+:\d+)', row)
        n = m[0].replace(':', '')
        timestamp = int(n)
        #print(row)
        if "Guard" in row:
            id = re.findall(r'(\#\d+)', row)[0]
            if id not in guards:
                guard = Guard(id)
                guards[id] = guard
        if "falls" in row:
            if id in guards:
                guards[id].sleep(timestamp)
        if "wakes" in row:
            if id in guards:
                guards[id].stopSleep(timestamp)

    # A)
    max_sleep = 0
    selected_guard = Guard("#0")
    for guard in guards.values():
        #print(guard)    
        if guard.getTotalsleep() > max_sleep:
            max_sleep = guard.getTotalsleep() 
            selected_guard = guard

    print("A): ", selected_guard.getCalculatedHash(), selected_guard)

    # B)
    max_occurence = 0
    selected_guard = Guard("#0")
    for guard in guards.values():
        #print(guard)    
        if guard.getMaxOccurence() > max_occurence:
            max_occurence = guard.getMaxOccurence() 
            selected_guard = guard


    print("B): ", selected_guard.getCalculatedHash(), selected_guard)

# Main body
if __name__ == '__main__':
    a()
    sys.exit(1)
