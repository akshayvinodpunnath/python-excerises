#!/usr/bin/python3
"""
    Write a Python program to accept a filename from the user and print the extension of that
    Sample filename : abc.java
    Output : java
"""

#Input File Name with extension
fileName = input("Enter File Name:")

#split fileName variable and extra element at index position 1
print("File Extension: {}".format(fileName.split('.')[1]))