
HOTDOGS = 10

BUNS = 8

people = int(input("Enter the number of people attending the cookout: "))

dogsperson = int(input("Enter the number of hot dogs each person will be given: "))

totaldogs = people * dogsperson

packagedogs = totaldogs // HOTDOGS

packagebuns = totaldogs // BUNS

dogsleftover = totaldogs % HOTDOGS

bunsleftover = totaldogs % BUNS

print("hot dogs required:", packagedogs)

print("buns required:", packagebuns)

print("Number of hot dogs left over:", dogsleftover)

print("Number of buns left over:", bunsleftover)
