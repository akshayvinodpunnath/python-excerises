#!/usr/bin/python3
"""
    Write a Python program to print the calendar of a given month and year.
"""

import calendar

month = input("Enter month in format MM(01-12): ")
year = input("Enter year in format YYYY: ")

try:
    print("\n", calendar.month(int(year), int(month)))
except:
    print("\nPlease enter year and month in requested format")