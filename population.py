
# File: population.py
# Description: Write a program that predicts the approximate size of a population of organisms. The application should use text boxes to allow the user to enter the starting number of organ- isms, the average daily population increase (as a percentage), and the number of days the organisms will be left to multiply.
# Assignment Name and Number: Population, 13
#
# Name: Noah Postelle
# GitHub: noahpostelle
#
# On my honor, Noah Postelle, this programming assignment is my own work
# and I have not provided this code to any other student.

def calcpop(startpop, dailyinc, dtm):
    popdata = []
    population = startpop
    for day in range(1, dtm + 1):
        popdata.append((day, population))
        population += (population * (dailyinc / 100))
    return popdata

startpop = int(input("Enter the starting number of people: "))
dailyinc = float(input("Enter the daily increase: "))
dtm = int(input("Enter the number of days: "))
popdata = calcpop(startpop, dailyinc, dtm)

for day, population in popdata:
    print(f"{day}\t{population:.5f}")
