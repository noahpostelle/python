# File: DiceRoller
# Description: In a program, write a function named roll that accepts an integer argument number_ of_throws. The function should generate and return a sorted list of number_of_throws random numbers between 1 and 6. The program should prompt the user to enter a positive integer that is sent to the function, and then print the returned list.
# Assignment Name and Number: Dice Roller, 6
#
# Name: Noah Postelle
# GitHub: noahpostelle
#
# On my honor, Noah Postelle, this programming assignment is my own work
# and I have not provided this code to any other student.
import random
def roll(num_throws):
    
    throws = [random.randint(1, 6) for _ in range(num_throws)]
    throws.sort() 
    return throws
while True:
        num_throws = int(input("Enter the number of throws: "))
        if num_throws > 0:
            break

result = roll(num_throws)
print("random throws:", result)
