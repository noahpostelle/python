# File: Rainfallstats.py
# Description: Design a program that lets the user enter the total rainfall for each of 12 months into a list. The program should calculate and display the total rainfall for the year, the average monthly rainfall, the months with the highest and lowest amounts.
# Assignment Name and Number: Rainfall stats, 3
#
# Name: Noah Postelle
# GitHub: noahpostelle
#
# On my honor, Noah Postelle, this programming assignment is my own work
# and I have not provided this code to any other student.

monthlyrain = []

for month in range(1, 13):
    while True:
            rain = float(input(f"Enter the total rainfall for month {month}: "))
            monthlyrain.append(monthlyrain)
            break
annual_rain = sum(monthlyrain)

avgmonth = annual_rain / 12

max_rain = max(monthlyrain)
min_rain = min(monthlyrain)
month_max = monthlyrain.index(max_rain) + 1
month_min = monthlyrain.index(min_rain) + 1

print("Total annual rainfall:" , annual_rain ," inches")
print("Average monthly rainfall: ", avgmonth ," inches")
print("Month with the highest rainfall: Month ", month_max , "with" , max_rain , "inches")
print("Month with the lowest rainfall: Month ", month_min , "with" , min_rain , "inches")
