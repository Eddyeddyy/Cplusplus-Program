import re
import string
from collections import Counter

# funtion displaying the menu for the program
def displayMenu():
    print("Welcome! Please select one of the following options to begin:")
    print()
    print("1. Shows a list of all items purchased and how much of each item was purchased.")
    print("2. Shows how much a specific item was purchased.")
    print("3. Displays a histogram representing all items purchased.")
    print("4. Exit the program")
    print()
    print("Please enter your selection:")

# function to iterate through file to gather all produce purchased and how many times it occurs
def allproducefrequency():
    lines = []
    newlines = []
    #opens file and adds each line to the list labled lines
    with open("InputFile.txt") as f:
        lines = f.readlines()
    # from file all entries end with \n, and this loop removes that from each entry
    for line in lines:
        newlines.append(line.strip())
    # counts each time a produce was purchased and adds it to a dictionary
    d = dict(Counter(newlines))
    #prints each produce followed by the times it was purchased
    for i in d:
        print(i, ":", d[i],)

#this function produces the histogram of produce purchased
def histogram():
    lines = []
    newlines = []
    # opens file and adds each line to the list labled lines
    with open("InputFile.txt") as f:
        lines = f.readlines()
    # from file all entries end with \n, and this loop removes that from each entry
    for line in lines:
        newlines.append(line.strip())
    # counts each time a produce was purchased and adds it to a dictionary
    d = dict(Counter(newlines))
    #this loop takes every produce and for however many times it was purchased it adds an * to the produce
    for i in d:
        print(i, end='')
        for j in range(d[i]):
            print('*', end='')
        print()

#this function searches for specific produce and displays how much it was pruchased
def frequency(v):
    count = 0
    lines = []
    newlines = []
    # opens file and adds each line to the list labled lines
    with open("InputFile.txt") as f:
        lines = f.readlines()
    # from file all entries end with \n, and this loop removes that from each entry
    for line in lines:
        newlines.append(line.strip())
    #searches the list for specific produce
    #if in list displays how much it was purchased
    if v in newlines:
        print("The number of times ", v, " was purchased is ", newlines.count(v))
    #if specific produce does not exist displays erreor message
    else:
        print("No such produce was purchased")
    return 0

