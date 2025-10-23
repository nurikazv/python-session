


# for 0, 1 in dictionaty.items():


# functions ==============

# methods - are built in functions for specific object(data type) 

# < there is a difference in term of syntax between methods and functions >

# functions - are designed to not be dependent on a speficic object (They are usually custom written)

# variable == object_name.<method>
# keys_var = dict.keys()
# lst.append()



# type() is function 
# len()
# input()
# int()
# these are functions


# we can create our own functions

# syntax: 
# def <function name>():
#     <code>


# def greet():
#     print("hey, bro")

# greet()


# parametr is input for our function
# function with parametr:
# def <function name>(parametr, parametr2, parametr3):
#     <code>

# example:
# def greet(name):  # python function figures out what kind of data type you are using. You can make it explicit as well
#     print(f"Hey {name}, how is it going?")

# name = "nurik"
# name2 = 'sean'

# greet(name)
# greet(name2)
# greet("Beka") => Hey Beka, how is it going?





# def greet(name):
#     print(f"Hey {name}, how is it going?")


# def greet2(name):
#     # print(f"Hey {name}, how is it going?")
#     return(f"Hey {name}, how is it going?")


# what does return keyword does?
# return --> returns the data type <object> back
# return - should always be used in the function instead of print, unless you need to print data in terminal

# print() -  is function that returns the data type to terminal to make it visible 
# BUT print() does not return always None  --> NoneType

# print(greet('nurik')) -> Hey nurik, how is it going?  --> this is a string

# a = greet("Esen") # print
# b = greet2("Esen") #return

# print(a)
# print(b)

# return does not print data to make it visible, you still to use print()


# input for the function called parametr
# parametr vs argument
