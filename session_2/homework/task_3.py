# Task 3: Password Validator
# Description:
#  Ask the user to input a password.
#  Check if it meets all of the following conditions:
# At least 8 characters long
# Contains the letter “@”
# Does not contain any spaces
# Print:
# "Strong password" if all conditions are met
# Otherwise, print "Weak password"
# Example:
# Input: hello@123  
# Output: Strong password

password = input("Enter your password: ")

if len(password) >= 8 and "@" in password and " " not in password:
    print("Your password is strong")
elif len(password) < 8 or "@" not in password:
    print("Your password is weak")
else:
    print("Something went wrong, try again")

    