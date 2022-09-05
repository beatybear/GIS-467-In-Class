# -*- coding: utf-8 -*-
"""
in class work 3.21.22
"""
import FunctionPracticeModule

class FunctionPractice:
    #Write a function named get_rectangle_area that takes 2 floats as arguments for length and width and returns the area of a rectangle
    def get_rectangle_area(width, length):
        return (width * length)    

    w = float(input("Please enter the width of a rectangle.\n"))
    l = float(input("Please enter the length of a rectangle.\n"))
    print("\nThe area of the rectangle is " + str(get_rectangle_area(w, l)))
    
    #Create a function (in a module) that accepts a temperature in degrees Fahrenheit and returns the temperature in degrees Celsius. The function should ask for the temperature in Fahrenheit, convert the temperature value to Celsius and return it
    #In a second script, import the module, call the function and print the result as a user-friendly message.
    degreesC = FunctionPracticeModule.FunctionPracticeHelper.fahrenheitToCelsius()
    print("It is " + degreesC + " degrees Celsius.")
    
    input("Press enter to exit.")