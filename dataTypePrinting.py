# -*- coding: utf-8 -*-
"""
in class work 1.24.22
"""

class Exercise:
    # write a program that converts miles to kilometers
    miles = 5280
    kilometers = round(miles * 1.609344, 2)
    print (str(miles) + " miles is equal to " + str(kilometers) + " kilometers.\n")
    
    #write a program to calculate the average pace of a runner (miles/minute)
    miles = 26
    minutes = 190
    average = round(miles/minutes, 3)
    mph = average * 60
    print("The average pace of a runner who ran " + str(miles) + " miles in " + str(minutes) + " minutes is " + str(average) + " mi/min, or " + str(mph) + " mph.\n")
    
    #write a script that prompts 2 variables and calculates the area of a rectangle
    width = int(input("What is the width of the rectangle?\n"))
    length = int(input("What is the length of the rectangle?\n"))
    area = width * length
    print("\nThe area is " + str(area) + ".")
    
    #branching allows the program to make a decision with an if statement
    password = input("Please input the password:\n")
    if(password == "secret"):
        print("\nAccess Granted")
        print("I already know all this information, but don't tell anybody.")
    elif(password.lower() == 'secret'):
        print("\nAccess Denied")
        print("This password is case sensitive.")
    else:
        print("\nAccess Denied")
        print("You do not have access to this information.")
        
    #prompt the user for a number and print whether it is even or odd
    num = int(input("Please input a whole number.\n"))
    if(num%2 != 0):
        print("The number input in odd.")
    else:
        print("The number input is even.")    
    
    #prompt the user for 2 numbers and print which is greater
    num1 = int(input("Please input a number.\n"))
    num2 = int(input("Please input a number.\n"))
    print('\nThe first input is larger.' if num1>num2 else'The inputs are equal.' if num1==num2 else 'The second input is larger') #ternary operator (one line if statement)
    
    #prompt the user for a 2 letter languange conde and print hello world in the given language
    langCode = input("Please input one of the following language codes:\nEN, ES, DE\n")
    if(langCode == 'EN'):
        print("Hello World!")
    elif(langCode == 'ES'):
        print("Hola Mundo!")
    elif(langCode == "DE"):
        print("Hallo Welt!")
    else:
        print("Invalid Language Code")