#!/usr/bin/python3
"""
    Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

    Sample String : 'w3resource'
    Expected Result : 'w3ce'
    Sample String : 'w3'
    Expected Result : 'w3w3'
    Sample String : ' w'
    Expected Result : Empty String
"""

class String:

    def __init__(self, string):
        self.string = string

    def extractedString(self):
        stringLength = len(self.string)
        firstString = self.string[:2]
        lastString = self.string[stringLength-2:stringLength]
        if stringLength <= 1:
            return ''
        elif stringLength < 4:
            return firstString + firstString
        else:
            return firstString + lastString


inputString = input("Enter String:\n")

string = String(inputString)

print("Expected Result:\t", string.extractedString())



