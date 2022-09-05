# -*- coding: utf-8 -*-
"""
in class work 2.7.22
"""

class MoreItereation:
    prefixes = input("Please enter the prefixes as a String: ")
    suffix = input("Please enter the suffix to append: ")
    i = 0
    print("With a while loop.")
    while i < len(prefixes):
        print(prefixes[i].upper() + suffix)
        i += 1
    print("With a for loop.")
    for character in prefixes:
        print(character.upper() + suffix)
    
    print("\nPractice with tuples")
    #tuples are a type of sequence that contain elements of other types that do not have to be of the same type
    results = (('Jose', 2168), ('Sally', 1897), ('Jibin', 1809), 
           ('Mary', 1749), ('Monica', 2382), ('Sabrina', 2168), 
           ('Philip', 1350), ('Jeanna', 1668), ('Ryan', 2439))
    for person in results:
        print(f"{person[0]} completed the race with a time of {person[1]}")
        
    