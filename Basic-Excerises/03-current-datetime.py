#!/usr/bin/python3
"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""

# import datetime library
from datetime import datetime

"""
    now() function in datetime returns current timestamp.
    strftime formatting function converts value returned from now() to format - YYYY-MM-DD HH24:MI:SS
"""
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))