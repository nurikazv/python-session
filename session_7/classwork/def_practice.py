

# def is_even(not_sorted_list):
#     even_list = []

#     for i in not_sorted_list:
#         if i % 2 == 0:
#             even_list.append(i)

#     return even_list

# lst = [2, 3, 7, 12, 34 , 35, 25, 10000, 102]
# even = is_even(lst)

# print(even)

# * -> called pointer 



def search(lst_num, digit):
    for index in range(len(lst_num)):
        if lst_num[index] == digit:
            found = index #variable
            break
        else:
            return  'Digit does not exist'
        
    return found

lst = [2, 3, 7, 12, 34 , 35, 25, 10000, 102, 12]

print(search(lst, 2))

# print(lst.index(12))