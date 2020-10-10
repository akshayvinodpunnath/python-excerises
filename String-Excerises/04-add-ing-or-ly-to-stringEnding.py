#!/usr/bin/python3
"""
    Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
"""


class String:
    
    def __init__(self, string):
        self.string = string

    def modifiedString(self):
        if len(self.string) < 3:
            return self.string
        elif self.string[len(self.string)-3:len(self.string)] == 'ing':
            return self.string + 'ly'
        else:
            return self.string + 'ing'


inputString = input("Enter String:\n")

string = String(inputString)

print("Converted String is : {}".format(string.modifiedString()))
