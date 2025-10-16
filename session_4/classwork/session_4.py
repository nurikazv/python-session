# for i in range(1, 11):
#     if i == 5: 
#         break # it is a loop keyword that stops the loop (it will end on 4)
# else: 
#     print("Hey, loop is finished")
#   #this block will always get executed when the loop fully finished 


# counter = 0 
# while counter != 10:
#     counter += 1 

#     if counter == 5: 
#         break 
#     print(counter)
# else: 
#     print("Hey, loop is done")


# # lets wirte a programm that stops when it see input character


# word = "this block always gets executed when the loop fully finishes"

# character = input("Enter ur character: ")

# for char in word: 
#     if character == char: 
#         break 
#     else:
#         print(char, end='\n') #end='\n' with that output is po vertikali
# print()






# sep --> separator 

# print("Hello", "World", , sep="") ==> HelloWorld
# print("Hello", "World", , sep="-") ==> Hello-World





# continue -------------

for i in range(1, 11):
    if i % 2 == 0:
        print(i)
    else:
        continue  
        print(i)  ## gets ignored

        # break - stops the loop
        # continue - skips the iterator


for i in range(1, 6):
    if i == 3:  
        continue
    print(i)
    # output ==> 1
    #            2
    #            4
    #            5


numbers = [4, -2, 7, -5, 3]

for n in numbers:
    if n < 0:
        continue
    print(n)



# ----------- pass 



for i 