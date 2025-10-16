# Task 2: Remove Duplicates from a List
# Ask the user to enter multiple words separated by spaces. Store them in a list and remove duplicate words while maintaining the original order.

# Example:
# Enter words: apple banana apple cherry banana apple  
# Filtered List: ['apple', 'banana', 'cherry']

list = ["apple", "banana", "apple", "cherry", "banana", "apple"]

filter_list = []

for i in list:
    if i not in filter_list:  
        filter_list.append(i)
print(filter_list)