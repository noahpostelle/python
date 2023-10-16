# Given list of numbers
numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

# Initialize an empty list to store valid numbers
valid_numbers = []

# Loop through the numbers and filter the valid ones
for num in numbers:
    if 0 <= num <= 100:
        valid_numbers.append(num)

# Calculate the total and average of valid numbers
total = sum(valid_numbers)
average = total / len(valid_numbers)

# Display the valid numbers, total, and average
print("Valid numbers between 0 and 100:", valid_numbers)
print("Total of valid numbers:", total)
print("Average of valid numbers:", average)
