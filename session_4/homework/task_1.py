# Task 1: Reverse a List
# Write a program that reverses a list using a for loop.
# Example:

# Input:
# Enter numbers separated by space: 1 2 3 4 5
# Output:
# Reversed List: [5, 4, 3, 2, 1]


list = [1, 2, 4, 3, 5]

rev_list = []

for i in list:
    rev_list.insert(0, i)
print(rev_list)

    