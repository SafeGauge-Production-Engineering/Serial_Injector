# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 15:59:45 2022

1. Get serial numbers in as a list (from test.csv for starters)
    1.1 Do error checking
2. Iterate through the list
3. [Make a new file and insert all info , concatenating new serial number in there] / [Edit current file]
4. Overwrite the previous file so the new one is saved there
5. Call the BT programmer to start? Rewrite the programmer?
"""

''' List requirements:
    - less than 100 items
    - file only contains serial numbers (no title)
        + check if there are non hex values
        + check if first row is the right format
    - each cell has only one serial, not all in the one
        + error check for more than 6 characters
    
'''

import os # for file reading and writing
import csv
from functions import *
#import easygui

Serial = "111111" #must be 6 hex digits

index = 0
SerialList = [0] * 100 ## change this to the number inserted

with open("AutoInjectSerials.csv", "r") as serialFile:
    reader = csv.reader(serialFile)
    for row in reader:
        for column in row:
            SerialList[index] = column
            #print(SerialList[index] + " " + str(index))
            index += 1
            
for i in SerialList:
    print(i)
    if i == 0:
        print("skip")
    else:
       write_serial_to_file(i)
    
    
