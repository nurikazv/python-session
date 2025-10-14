# Input:
# Enter a word: Python
# Output:
# Reversed Word: nohtyP

word = input("Enter your word: ")

reversed_word = ""

for char in word:
    reversed_word = char + reversed_word

print(reversed_word)

