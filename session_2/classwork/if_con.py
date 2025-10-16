# syntax for if condition 

# if <boolean_data_type>:
#     <code>
# elif <boolean_data_type>:
#     <code>
# else:
#     <code>
    
    
# if num1 > num2:
#     print("Num 1 is greater")
# elif <boolean_data_type>:
#     <code>
# else:
#     <code>
    
    
# task


# num1 = int(input("Enter your first number: "))
# num2 = int(input("Enter your second number: "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num1 < num2:
#     print(f"{num2} is greater than {num1}")
# elif num1 == num2:
#     print(f"{num1} and {num2} are equal")
# else:
#     print("Something went wrong :(")



# num = int(input("Enter your number: "))
# div_num = int(input("Enter your dividing number: "))

if num < 0 and num % div_num == 0 : 
    print(f"{num} is negative and it is divisible by {div_num}")
elif num < 0 and num % div_num != 0 : 
    print(f"{num} is negative and it is not divisible by {div_num}")
elif num > 0 and num % div_num == 0 : 
    print(f"{num} is positive and it is  divisible by {div_num}")
elif num > 0 and num % div_num != 0 : 
    print(f"{num} is positive and it is not divisible by {div_num}")
else: 
    print("Something went wrong :(")



# ---------------character counting 
# word = 'div_num = int(input("Enter your dividing number: "))'
# print(len(word))

word = input("Enter your word: ")

if len(word) >= 15:
    print("Sentence is too big")
else: 
    print(word)