# -*- coding: utf-8 -*-
"""
in class work 3.14.22
"""
from random import choice

#write a script that functions like a magic 8 ball using random and the text file of responses
responses = r"C:\Users\beaty\Desktop\SP 2022\GIS 467-667\GIS 467 in class\magic8ball.txt"
with open(responses) as f: #context manager will close file outside of the code block
    answers = f.readlines() #answers = f.read()
    print(answers)
    
    question = input("What is your question? Press enter to exit.\n")
    while question:
        print(choice(answers))
        question = input("What is your question? Press enter to exit.\n")
print("Thanks for playing Magic 8 Ball!\n")

#write a script to decode morse code
morse_lookup = { 
   "A":".-",
   "B":"-...",
   "C":"-.-.",
   "D":"-..",
   "E":".",
   "F":"..-.",
   "G":"--.",
   "H":"....",
   "I":"..",
   "J":".---",
   "K":"-.-",
   "L":".-..",
   "M":"--",
   "N":"-.",
   "O":"---",
   "P":".--.",
   "Q":"--.-",
   "R":".-.",
   "S":"...",
   "T":"-",
   "U":"..-",
   "V":"...-",
   "W":".--",
   "X":"-..-",
   "Y":"-.--",
   "Z":"--.."
}

wordToConvert = input("Enter a word to convert to morse code: ")
conversion = ""
for char in wordToConvert:
    if(char.isalpha()):
        conversion += morse_lookup[char.upper()] + " "
print(conversion)
    

    