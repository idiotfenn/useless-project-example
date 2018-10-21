#!/bin/python

import random

string = input("Enter a string: ").title()
i = len(string) - 1
while i > 0:
    char = string[i-1:i]
    if random.randint(0, 1) == 1 and char.islower():
        char = char.swapcase()
    string = string[:i-1] + char + string[i:]
    i = i - 1

print(string)
