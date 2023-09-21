
# File: factorial.py
# Description: Write a program that lets the user enter a nonnegative integer then uses a loop to calculate the factorial of that number. Display the factorial.
# Assignment Name and Number: Calculating the factorial of a number, 12
#
# Name: Noah Postelle
# GitHub: noahpostelle
#
# On my honor, Noah Postelle, this programming assignment is my own work
# and I have not provided this code to any other student.
n = int(input("Enter a nonnegative integer: "))


if n < 0:
    print("Please enter a nonnegative integer.")
else:
    
    factorial = 1

    
    for i in range(1, n + 1):
        factorial *= i
    print("The factorial of", n, "is",factorial)
