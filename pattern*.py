
# File: pattern*.py
# Description: Write a program that uses nested loops to draw this pattern:
#                *******
 #               ******
#                *****
 #               ****
 #               ***
 #               ** 
 #               *
# Assignment Name and Number: No Name, 14
#
# Name: Noah Postelle
# GitHub: noahpostelle
#
# On my honor, Noah Postelle, this programming assignment is my own work
# and I have not provided this code to any other student.





rows = 7
for i in range(rows, 0, -1):
   
    for j in range(i):
        print("*", end="")
    print()  
