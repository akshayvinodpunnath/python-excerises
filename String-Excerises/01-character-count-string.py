#!/usr/bin/python3
"""
    Write a Python program to count the number of characters (character frequency) in a string.
"""

class String:

    def __init__(self, string):
        self.string = string

    def characterCount(self):
        countDictionary = {}
        for i in self.string:
            if i in countDictionary:
                countDictionary[i] = countDictionary[i] + 1
            else:
                countDictionary[i] = 1
        return countDictionary



inputString = input("Please input string:\n")

string = String(inputString)

print("Count of Characters in string:\n", string.characterCount())