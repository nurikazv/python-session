
# Session_4 learned things

# List
# Arrays
# Collection data (Data type holds multiple values with single key)
# Mutable (value can be changed) | Immutable (cannot) 

# functions for lists
# - append() - adds value to the end of the list 
# - insert([index]) - adss value too, but you can put specific index
# - remove(argument) - removes from list, takes argument
# - pop([index]) - removes too, takes index 
# - del([index]) - deletes element in the list, takes index


# ==============
# split()  - splits each element in the list
# ======

# sentence = "Collection data (Data type holds multiple values with single key)"

# lst = sentence.split()
# print(lst) ==> ['Collection', 'data', '(Data', 'type', 'holds', 'multiple', 'values', 'with', 'single', 'key)']


# sentence = "Collection:data:Data:type:holds"
# lst = sentence.split(':')
# print(lst) #==> ['Collection', 'data', 'Data', 'type', 'holds']



# List comptrhension 

# list is comptrhension is used to generate a list with for loop and if condition within single line 

# lst = [i for i in range(10) if i % 2 == 0]
# print(lst)


# -----------------------------------

# lst = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

# double indexing
# print(lst[1][2]) --> takes second list, then takes element under index 2 which is 3 

# for i in lst:
#     for j in i: 
#         print(j)


# print(lst[0][-1][2])



# -----------------------------------

# Tuple 
# List - mutable data type 

# # Tuple is exactly works like list, but is immutable 


# tpl = (1, 2, 3, 4)
# tpl2 = 1, 2, 3
# tpl3 = 1,

# print(type(tpl3))


# no such methods like append, insert, pop, remove exist for tuple data type 

# tpl = 1, 2, 2, 55, 33, 44, 3, 3, 3, 3, 3
# tpl2 = ('hello', "Hello", "Hello", "a", "b")

# # print(tpl.count(55)) counted how many 55 in the tuple
# # print(tpl.count(3)) ==> 5
# print(tpl2.count("Hello")) ==> 2



# bob = ("Bob", "Smith", "20th of December", "Male", "215-456-3334")
# real life example of tuple. We cannot remove or add

# ----------------------------
# Data type : set
# - Set is mutable, like list 
# - Holds multiple data types, like list

# - BUT, set holds only unique values !!!
# - Sets output is sorted !!!!!

# st = {1, 2,3 ,4 ,5 ,6 , "hello"}

# st2 = {1, 11, 1, 11, 3, 4,  6 , True}
# st3 = {2, 2, 12, 22, 3, 4,  6 , False}


# print(st2)
# print(st3)


# ==============================

# Dictionary

# dictionary is colleecting data type that holds key-value pairs, mutable data type.
# dictionary ={"key":"value"}  == key-value pairs
# dictionary can only hold unique keys, but values can be same 
# Dictionary doesnt support indexing



# info = {"name": "Beka", "lastname": "Sultanov", "age":"22", "city":"Philadelphia", "Age":"22"}

# info["company"] = "Starbucks"

# del info['age']
# info.pop('city')
# print(info)

# print(f"Hey, {info['name']} {info['lastname']}, I also live in {info['city']}")




# Dictionary with for loops ==================

info = {"name": "Beka", "lastname": "Sultanov", "age":"22", "city":"Philadelphia", "Age":"22"}

# for i in info:
#     print(i)  #print keys, not values

# for i in info.values():  # iterates values  info.values()
#     print(i)


# for i in info.items(): # iterates key and values, but output is list of tuple with 2 values, no keys
#     print(i) # --> ('name', 'Beka')
#                 #   ('lastname', 'Sultanov')
#                 #   ('age', '22')
#                 #   ('city', 'Philadelphia')
                #   ('Age', '22')

# items = [("name", "Beka"), ('lastname', 'Sultanov'), ('age', '22'), ('Age', '22')]


# print(info.items())


for key, value in info.items():
    print(key) ## dictionary key 
    print(value) ## dictionary value 

