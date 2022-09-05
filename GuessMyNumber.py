# -*- coding: utf-8 -*-
"""
in class work 1.31.22
"""
import random

class Exercise:
    random_num = random.randint(1,100) #creates a random integer between 1-100
    print ("Hint: {}".format(str(random_num))) #.format is another way to add non-strings to a print statement
    attempts = 1
    guess = int(input("Please guess a number between 1 and 100.\n"))
    while(guess != random_num):
        attempts = attempts + 1
        print("\nSorry, that is incorrect.nPlease Try Again")
        guess = int(input("Please guess a number between 1 and 100.\n"))
    print("That is the correct number.")
    print(f"It took {attempts} trys.") #f-Strings is another way to add non-strings to a print statement
    
    num = int(input("Please enter a whole number.\n"))
    even = 2
    count = 0
    theSum = 0
    while(even <= num):
        theSum += even
        count += 1
        even += 2
    avg = theSum/count
    # %s - String, %f - float, %d - decimal, %i - int
    print("Count: %i\nSum: %i\nAverage: %i\n" %(count, theSum, avg)) #% formatting is another way to add non-strings to a print statement