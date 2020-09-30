#!/usr/bin/python3
"""
    Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
"""

firstName = input("Enter First Name:")
lastName = input("Enter Last Name:")

fullName = firstName + ' ' + lastName

print("Full Name:", fullName)
print("Full Name in Reverse:", fullName[::-1])