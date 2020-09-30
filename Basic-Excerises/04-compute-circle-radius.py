#!/usr/bin/python3
"""
    Write a Python program which accepts the radius of a circle from the user and compute the area.
"""

# Import math library for value of Pi
import math

"""
 Class Circle has attribute radius
 Method __area__ returns area of circle rounded to 3 decimal points
"""
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def __area__(self):
        return round(pow(self.radius, 2) * math.pi, 3)

#Input circle radius
radius = input("Enter Circle Radius: ")
# new object circle initialized for class Circle
circle = Circle(int(radius))

# Result area returned
print("Circle Area: ", circle.__area__())
