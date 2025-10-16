# Task 4: Find the Second Largest Number in a List (No max() or sort())
# Ask the user to enter a list of numbers. Find and print the second largest number without using max() or sort().

# Example:
# Enter numbers: 10 45 78 23 89 56  
# Second largest number: 78


list = list(map(int, input("Enter numbers: ").split()))

large_num = list[0]

for num in list:
    if num > large_num:
        large_num = num


large_num_2 = list[0]
for num in list:
    if num != large_num and num > large_num_2:
        large_num_2 = num

print(large_num_2,"is second largest number")