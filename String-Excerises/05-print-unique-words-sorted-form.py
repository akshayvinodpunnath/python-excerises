#!/usr/bin/python3
"""
    Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
"""

class List:
    def __init__(self, string):
        self.list = string.replace(" ","").split(',')
    
    def sortedList(self):
        copiedList = self.list
        copiedList.sort()

        copiedList = list(dict.fromkeys(copiedList))

        return ", ".join(copiedList)



stringInput = input("Enter comma seperated sequence of words: \nexample: red, white, black, red, green, black\n")

string = List(stringInput)

print("Sroted unique list:\n{}".format(string.sortedList()))