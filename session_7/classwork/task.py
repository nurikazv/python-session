def search(lst_num, digit=0):
    for index in range(len(lst_num)):
        if lst_num[index] == digit:
            found = index 
            return found
            break
    

        

lst = [2, 3, 7, 12, 34 , 35, 25, 10000, 102, 12]

# print(search(lst, 12))


def pyramid(word):
    for i in range(len(word) + 1):
        print(word[:i])

pyramid("Hello")


# word = input("Enter your word: ")
# pyramid = ""

# for char in word:
#     pyramid += char   
#     print(pyramid)