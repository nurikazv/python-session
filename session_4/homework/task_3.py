# Task 3: Find the Longest Word in a List
# Ask the user to enter a list of words. Find and print the longest word from the list.

# Example:
# Enter words: Python Java JavaScript C  
# Longest word: JavaScript  

words = input("Enter words: ").split()  

longest_word = max(words, key=len)

print(longest_word,": is longest word")