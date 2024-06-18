# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:03:40 2022

@author: 61477
"""


# importing easygui module
from easygui import *
SGtitle = "SG Serial Injector"

def write_serial_to_file(productName, serialNo, pathOfOutputFile):
    lineUntilName = "        <value>"
    lineAfterName = "</value>\n"
    lineUntilSerial = "<service uuid=\"477b695e-fb98-4cfc-9c89-539326"
    lineAfterSerial = "\" advertise=\"true\">\n"
    
    # import serial numbers as a list
    # fopen( )
    # filePath = filePicker( )
    
    #easygui.egdemo()
    
    with open(pathOfOutputFile, "r") as file:
        contents = file.readlines()
        
    
    # contents[17] = "<service uuid=\"477b695e-fb98-4cfc-9c89-539326BEEEEF\" advertise=\"true\">\n"
    
    joinNameLine = [lineUntilName, productName, lineAfterName]
    newNameLine = ''.join(joinNameLine)
    
    joinSerialLine = [lineUntilSerial, serialNo, lineAfterSerial]
    newSerialLine = ''.join(joinSerialLine)
        
    contents[8] = newNameLine
    contents[17] = newSerialLine
    
    print(newNameLine)
    print(newSerialLine)
    
    # print(contents[17])
    # contents.insert(indexLine, value)
    
    with open(pathOfOutputFile, "w") as file:
        contents = "".join(contents)
        file.writelines(contents)
    
    # take the first serial number https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
    
    print(serialNo + " Serial written to file")
    
    
hexDigits = "0123456789ABCDEF"

def hex_error_check(serialNo):
#    print(str(len(serialNo)))
    if len(serialNo) != 6:
       error1 = " is not a 6 digit serial. Check and restart with correct serials."
       response = ccbox(title=SGtitle, msg=serialNo + error1)
       #quit()
       return 0
    
    for char in serialNo:
        if char not in hexDigits:
            error2 = " contains non-hex characters. Check and restart with correct serials."
            response = ccbox(title=SGtitle, msg=serialNo + error2) 
            #quit()
            return 0
    return serialNo

# Ideally need to have the for loop in a function that can be recalled when goBack is pressed:
    

def LoopSerials(productName, SerialList, totalCount, pathOfOutputFile):
    count = 0
    for serial in SerialList:
        if count == 0:
            prevSerialStr = "Nothing programmed yet"
            
        count += 1
        prevStr = productName + " Previous Serial: " + str(prevSerialStr) + "\n\n\n\n"
        programStr = "PROGRAMMING "+ str(count) + " OF " + str(totalCount)+ ". \n\n\n"
        #print(serial)
        
        if serial == 0:
            skip = True
        else:
            buttonChoice = indexbox(title=SGtitle, msg= prevStr + programStr + serial + " will be uploaded", choices=("Program", "Cancel", "Go Back", "Skip","Show List"))      
               
            if buttonChoice == 0: # PROGRAM pressed
                goBackTo = None
                pass # works. May not need the pass?!
                write_serial_to_file(productName, serial, pathOfOutputFile)
            elif buttonChoice == 1: # CANCEL pressed
                sys.exit()  # works
            elif buttonChoice == 2: # GO BACK pressed
                #goBack = True
                goBackTo = prevSerialStr
                return goBackTo
                test = 0   # Not sure if you can go back in a loop?! #decrement serial
            elif buttonChoice == 3: # SKIP pressed
                goBackTo = None
                continue # TEST THIS! Seems to work #increment serial
            elif buttonChoice == 4: # Quit pressed
                sys.exit()
            else:
                goBackTo = None
                print("Choice is outside all button indexes")
               
       # ccbox(title=SGtitle, msg= prevStr + progStr + serial + " will be uploaded", choices=("Program", "Cancel"))
        #print("now prev serial: " + serial)
        prevSerialStr = serial 
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    