#!/usr/bin/python3
"""
    Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
"""

#compute function returns vale of n+nn+nnn
def compute(n):
    return n + int("%s%s" % (n,n)) + int("%s%s%s" % (n,n,n))

n = int(input("Enter integer value: "))

print("Result: {}".format(compute(n)))