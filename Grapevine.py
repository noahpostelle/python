
R = float(input("Enter the length of the row: "))
E = float(input("Enter the amount of space used by an end-post assembly: "))
S = float(input("Enter the amount of space between the vines: "))


V = (R - 2*E) / S


print(f"The number of grapevines that will fit is: {int(V)}")