
pocket_number = int(input("Enter a pocket number (0-36): "))

if 0 <= pocket_number <= 36:
    if pocket_number == 0:
        pocket_color = "green"
    elif 1 <= pocket_number <= 10 or 19 <= pocket_number <= 28:
        pocket_color = "red" if pocket_number % 2 == 1 else "black"
    elif 11 <= pocket_number <= 18 or 29 <= pocket_number <= 36:
        pocket_color = "black" if pocket_number % 2 == 1 else "red"
    print(f"The pocket", pocket_number, "is", pocket_color)
else:
    
    print("ERROR")
