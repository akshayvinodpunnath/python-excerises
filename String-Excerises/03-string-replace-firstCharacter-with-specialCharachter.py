#!/usr/bin/python3
"""
    Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
"""

class String:
    def __init__(self, string, replaceChar):
        self.string = string
        self.replaceChar = replaceChar

    def replaceFirstCharacterInString(self):
        retrunString = self.string[:1]
        for i,v in enumerate(self.string):
            if i != 0:
                if v == self.string[0]:
                    retrunString += self.replaceChar
                else:
                    retrunString += v
        print(retrunString)
        return retrunString


inputString = input("Enter Input String:\n")
replaceCharacter = input("\nEnter replace character:\n")

string = String(inputString, replaceCharacter)

print("\nModified String: {}".format(string.replaceFirstCharacterInString()))

                    