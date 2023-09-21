# File: Calories Burned
# Description: Running on a particular treadmill you burn 4.2 calories per minute. Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.
# Assignment Name and Number: Calories Burned, 2
#
# Name: Noah Postelle
# GitHub: noahpostelle
#
# On my honor, Noah Postelle, this programming assignment is my own work
# and I have not provided this code to any other student.

cpm = 4.2
timedur = [10, 15, 20, 25, 30]
for time in timedur:
    burn = cpm * time
    print('After', time, "minutes, you have burned", burn, "calories.")
