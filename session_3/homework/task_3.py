# Input:
# Enter a word: CODE

# Output:
# C
# CO
# COD
# CODE

word = input("Enter your word: ")
pyramid = ""

for char in word:
    pyramid += char   
    print(pyramid)