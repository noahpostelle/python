print("this is a leap year program")
year = int(input("Enter a year "))
month = str(input("Enter a month "))
day = int(input("Enter a day"))
daystoskip = int(input("Enter the amount of days you want to skip"))
totalday = [31, 30, 28, 29]
daysleft = (totalday - day)
daymath = (day + daystoskip)
if (daymath % 31 == 0):
    month + 1



list_months = [ "Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
list_monthsnum = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


