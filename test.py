# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 10:14:14 2022

@author: 61477
"""

# Test
listed = ["a", "b", "c","d"]

ind = listed.index("c")
print(str() + " index is")

print(ind)
print(len(listed))

newList = listed[ind : len(listed) ]

print(str(newList) + " newlist")

for i in range(0,10):
   # print(i)
    if i == 6:
        goBack = 0
        backTo = i
        break # overwrites this assignment when it gets back to the top of the loop

if goBack:
    print(str(backTo) + " backTo")
    
# Ideally need to have the for loop in a function that can be recalled when goBack is pressed