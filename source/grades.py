#!/bin/python

import pickle

grades = {}
if input("Do you have an existing grade file? (Y/n)")[0].lower() == "y":
    try:
        grades = pickle.load(open(input("What is the name of the file?"), "rb"))
        print("Current grades:")
        for name in grades.keys():
            print(name + "'s grade is '" + grades[name] + "'")
    except:
        print("Try again.")

def computegrade(score):
    if score > 100 or score < 0:
        raise ValueError
    elif score >= 93: 
        return "A"
    elif score >= 85:
        return "B"
    elif score >= 74:
        return "C"
    elif score >= 63:
        return "D"
    else:
        return "F"

print("You may now input grades. Enter '!quit' to exit.")
    
while True:
    name = input("What is the student's name?")
    if name == "!quit":
        break
    else:
        try:
            grades[name] = computegrade(float(input("What is the student's grade?")))
            print(name + "'s grade is now '" + grades[name] + "'")
        except:
            print("Invalid grade.")

if input("Would you like to save the grades?")[0].lower() == "y":
    pickle.dump(grades, open(input("What would you like to save the file as?"), "wb"))
