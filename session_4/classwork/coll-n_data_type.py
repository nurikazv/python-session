


# Collection data types

# List

# List always starts with [] square brackets 
# As a best practice, list should contain only singular data type

# a = ["beka", "teka", "pharmacy", 1, 45.3]
# print(type(a))
# print(a)


# names = ["bob", "anna", "vanessa", "beka"]
# print(names[1::2]) ==> ['anna', 'beka']
# print(names[-1]) ==> beka
# print(names[1:3])




# Mutabel and Immatubale data type =================
# Mutuation

# word = "hello"
# word[0] = 'H' ==> error, because its unmutable data type


# word = "hello"
# print(word.title()) ==> Hello 

# print(word.upper()) ==> HELLO



# names = ["bob", "anna", "vanessa", "beka"]

# # append(), insert()

# names.append("Jeka")
# names.append("Sasha")

# print(names)

# names.insert(1, "jora")
# names.insert(3, "Jeremy")

# print(names)



# task 1

# num = int(input("Num: "))
# list = []

# for i in range(1, num):
#     if i % 2 == 0: 
#         list.append(i)
# print(list)


# --------pop(), remove()

# names.pop()  --> removes from back of the if no index
# names.pop(1) --> removes second name "anna"

# print(names)

# names.remove("vanessa") --> need value, not index

# print(names)


# names = ["bob", "anna", "vanessa", "beka", "bob"]

# rem_name = input("Enter name to remove: ")
# counter = []

# for name in names: 
#     if name == rem_name :
#         counter.append(name)

# print(counter)
# print(counter)


# if counter in names: 
#     names.remove(counter)
# else:
#     pass


# print(names)
# print(counter)

# for name in names: 
#     if counter in names: 




# rem_name = input("Enter name to remove: ")
# names = ["bob", "anna", "vanessa", "beka", "bob"]

# for index in range(len(names)):
#     print(names[index])


# names = ["bob", "anna", "vanessa", "beka", "bob"]
# rem_name = input("Enter name to remove: ")

# for index in range(len(names)-1):
#     if names[index] == rem_name:
#         names.pop(index)


# print(names)



# names = ["bob", "anna", "vanessa", "beka", "bob"]
# duplicate_list = names
# # names and duplicate_list are same thing, one list 


# duplicate_list.pop()
# duplicate_list.pop()

# print(names)

# names.append("Timmy")
# print(id(duplicate_list))
# print(id(names))

# print(duplicate_list)
# print(names)




# names = ["bob", "anna", "vanessa", "beka", "bob"]
# duplicate_list = names[::]  == # copy()
# now they are 2 seperate lists





# list comprehension -------------
# # generation of the list using a single line 

# ex: input: 10 
# lst_number: [2,4,6,8,10]

# create a list 
# for loop 
#     if condition
#         append()

inp_num = int(input("input: "))
list_comprehension = [i for i in range(1, inp_num+1) if i % 2 == 0]
print(list_comprehension) # ==> [2, 4, 6, 8, 10, 12, 14]


inp_num = int(input("input: "))
kube_value = [num ** 3 for num in range(1, inp_num + 1)]
print(kube_value)