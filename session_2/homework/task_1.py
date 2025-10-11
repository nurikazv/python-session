# Task 1: Number info
# Description:
#  Ask the user to enter a number. Your program should:
# Check if the number is positive, negative, or zero
# Check if the number is even or odd
# Print both results
# Example:
# Input: -11  
# Output:
# The number is negative  
# The number is odd

num = int(input("Please your number: "))

if num > 0 and num % 2 == 0 :
    print(f"Your {num} is positive and even")
elif num > 0 and num % 2 != 0 :
    print(f"Your {num} is positive and odd")
elif num < 0 and num % 2 != 0 :
    print(f"Your {num} is negative and odd")
elif num < 0 and num % 2 == 0 :
    print(f"Your {num} is negative and even")
elif num == 0 :
    print(f"what do i do with {num}")
else:
    print("Something went wrong")

