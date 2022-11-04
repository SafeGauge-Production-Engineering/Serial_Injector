# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 15:59:45 2022

1. Get serial numbers in as a list (from test.csv for starters)
    1.1 Do error checking
2. Iterate through the list
3. [Make a new file and insert all info , concatenating new serial number in there] / [Edit current file]
4. Overwrite the previous file so the new one is saved there
5. Call the BT programmer to start? Rewrite the programmer?
6. Redo the BT programmer to accept python calls
"""

''' List Requirements:
    - less than 100 serial numbers
    - file only contains serial numbers (no title)
        + check if there are non hex values
        + check if first row is the right format
    - each cell has only one serial, not all in the one
        + error check for more than 6 characters
    
'''

import sys
import os # for file reading and writing
import csv
from serialFunctions import *
from easygui import *  #https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages

# https://docs.spyder-ide.org/5/faq.html#using-packages-installer
# https://stackoverflow.com/questions/10729116/adding-a-module-specifically-pymorph-to-spyder-python-ide

easygui.egdemo()

index = 0
SerialList = [0] * 100 ## change this to the number inserted

with open("AutoInjectSerials.csv", "r") as serialFile:
    reader = csv.reader(serialFile)
    for row in reader:
        for column in row:
            SerialList[index] = column
            index += 1
            
for serial in SerialList:
    print(serial)
    if serial == 0:
        skip = True
    else:
       write_serial_to_file(serial)
       

''' Next:
    - add key press to go to next serial
    - show which serial is being flashed
'''
    
    
