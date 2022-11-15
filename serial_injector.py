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
# https://docs.spyder-ide.org/5/faq.html#using-packages-installer
# https://stackoverflow.com/questions/10729116/adding-a-module-specifically-pymorph-to-spyder-python-ide

# FIX THE EASYGUI_QT ERROR (NO MODULE FOUND ERROR):
    # Inside the pip list - installed
    # Cant find the imported module. Possibly:
        # wrong path?
    # Now can't find the demos folder. maybe wasn't imported correctly in the first place

import sys
import os # for file reading and writing
import csv
from serialFunctions import * #works out of the box since it's in the same directory (finding the file is easy)

from easygui import *

# importing easygui module
from easygui import *
 
# title of our window
SGtitle = "SG Serial Injector"
 
# message for our window
msg = "This is how we inject serial numbers at SG"

#egdemo()

msgbox(title=SGtitle, msg="        SG serial injector works by:\n\n 1. Selecting a CSV with the serial numbers from the batch,\n 2. Inserting the serial number one by one into the QPS_gatt_sensor.xml file,\n 3. Repeating 2. for all serial numbers from within the selected CSV batch")

index = 0
SerialList = [0] * 100 ## change this to the number inserted. Should not be hardcoded

pathOfSerialNums = fileopenbox(title=SGtitle) # set the filetype

'''Read the Serials into an array
    -  Add check for if not 6 digits, or not hex one of 0123456789ABCDEF use bitwise AND/OR whatever works
'''
with open(pathOfSerialNums, "r") as serialFile:
    reader = csv.reader(serialFile)
    for row in reader:
        for column in row:
            #checkedSerial = hex_error_check(column)
            SerialList[index] = column
            index += 1
        
''' Inject the serial numbers into the .xml file
    - tell the user which serial is being uploaded
'''
for serial in SerialList:
    print(serial)
    msgbox(title=SGtitle, msg=serial + " will be uploaded", ok_button="Program")
    if serial == 0:
        skip = True
    else:
       write_serial_to_file(serial) 
       #ccbox()

      
       
''' Next:
    - UI
        - change to Tkinter
        - show the list of serial numbers and highligh the current one
        - have the ability to move back and forth through the serial numbers and show the current selection
    - Order arduino pro micro for footpedal- jaycar
   
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
