# -*- coding: utf-8 -*-
"""
in class work 3.21.22 helper
"""

class FunctionPracticeHelper: #returns a String, not a float
    #Create a function (in a module) that accepts a temperature in degrees Fahrenheit and returns the temperature in degrees Celsius. The function should ask for the temperature in Fahrenheit, convert the temperature value to Celsius and return it
     def fahrenheitToCelsius():
        degreesF = float(input("Please input a temperature in Fahrenheit to convert to Celsius.\n"))
        #formula: (x°F − 32) × 5/9 = 0°C
        return(str(round((degreesF - 32) * (5/9),3)))
    