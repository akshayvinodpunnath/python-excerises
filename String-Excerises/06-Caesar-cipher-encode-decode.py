#!/usr/bin/python3
"""
    Write a Python program to create a Caesar encryption.

    Element shifting by 3 characters
"""

class CaesarCipher:
    def __init__(self, string):
        self.string = string
        self.encoded = "".join([chr(ord(i)-3) for i in self.string])
        self.decoded = "".join([chr(ord(i)+3) for i in self.encoded])

inputString = input("Enter string to encode:\n")

string = CaesarCipher(inputString)

print("\nEncoded :{}\n".format(string.encoded))
print("Decoded :{}\n".format(string.decoded))

