# -*- coding: utf-8 -*-
"""
in class work 2.14.22
"""

#write a script that prints out a grocery list
groceries = ["milk", "eggs", "cheese", "pizza", "cereal", "bread"]
for item in groceries:
    print(item)
    
item = input("Please input an item to see it it is on your list.\n")
found = False
for x in range (len(groceries)):
    if(groceries[x] == item.lower()):
        found = True
if(found):
    print(f"\n{item} is on the list")
else:
    print(f"\n{item} is not on the list")

#Read the text file of state populations and print out each line
#Read the text file of state populations and print out the total, min, max, and average populations
#Prompt the user for a minimum population and print a count of the states greater than or equal to that population.
populationFile = open("C:/Users/beaty/Desktop/SP 2022/GIS 467-667/GIS 467 assignment 5/statePopulation.txt", "r")
print("The contents of the file are:\n")
total = 0
min = 999999999
max = -1
count = 0
populations = []
for line in populationFile:
    print(line)
    temp = line.split(',') #creates a list of the values in a line that are divided by a comma
    if(temp[0] != 'FIPS'):
        pop = int(temp[0])
        total += pop
        if(pop > max):
            max = pop
        elif(pop < min):
            min = pop
        populations.append(pop)
    count += 1
populationFile.close()
avg = int(total/count)
print(f"\nThe total population is {total}.")
print(f"The average population is {avg}.")
print(f"The maximum population is {max}.")
print(f"The minuimum population is {min}.")

smallPop = int(input("Please enter a minimum population query in a whole number.\n"))
sPCount = 0
for num in populations:
    if(num >= smallPop):
        sPCount += 1
print(f"There are { sPCount} populations greater than or equal to {smallPop}")

"""
how to do csv files

csv_file = r"C:/Users/beaty/Desktop/SP 2022/GIS 467-667/GIS 467 assignment 5/earthquakes.csv"
with open(csv_file, 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    header = next(csv_reader) #the first row has the column headers
    for row in csv_reader:
       print(row)
"""