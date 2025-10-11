# Task 5: Triangle Type Checker
# Description:
#  Ask the user for 3 side lengths and determine what type of triangle they form:
# Equilateral: all sides equal
# Isosceles: two sides equal
# Scalene: all sides different
# Not a triangle: if the sum of any two sides is not greater than the third
# Example:
# Input: 5, 5, 5  
# Output: Equilateral triangle


print("Enter 3 sides lengths for triangle")
side1 = input("First side lenght: ")
side2 = input("Secondd side lenght: ")
side3 = input("FiThird rst side lenght: ")


if side1 == side2 == side3 : 
    print("This is Equilateral triangle")
elif side1 == side2 != side3 or side1 != side2 == side3 :
    print("This is Isosceles triangle")
elif side1 != side2 != side3 : 
    print("This is Scalene triangle")
    
    
