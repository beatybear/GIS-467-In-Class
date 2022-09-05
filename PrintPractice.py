# -*- coding: utf-8 -*-
"""
GIS 467 in class exercise 1.17.22
"""

class Exercise:
    name = 'Grace'
    department = "GIS"
    classNumber = "667"
    print("Welcome to " + department + " " + classNumber + ", " + name)
    
    rise = 2
    run = 3
    slope = str(rise/run)[0:4:1]
    print("The slope is " + slope)
    
    base = 4
    height = 5
    area = str(base*height/2)
    print("The area is " + area)
