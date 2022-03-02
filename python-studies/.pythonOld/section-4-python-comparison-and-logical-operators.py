# My Python Notes
# Section 4

# Python Comparison Operators

print("Comparison Operators in Python")
# comparison operators in Python

# Equal To
ex1 = (3 == 4)
#        \_____> Known as (Equal to), if the values of two operands are equal, then the condition becomes
#                true.
print(f"\nex1 = {ex1}")
#           \__> This returns the boolean value of False because 3 is not equal to 4.

ex2 = "hello" == "bye"
#        \_____> Note you can also check if two strings equal to each other.
#                Capitalization matters when comparing two strings together, "Bye" == "bye" will equal
#                False.
#                Python will also consider types, so something like "2" == 2 will equal to false.
#                For floating points, as long as they equal the same value 2.0 == 2, it will be true.
print(f"ex2 = {ex2}")
#           \__> This returns the boolean value of False because the string "hello" is not equal to the
#                string "bye".
# __> The reason you use two (==) signs, is because if you use one (=) python will think you trying to assign a variable.

# Not Equal To
ex3 = (3 != 4)
#        \_____> Known as (Not Equal to), if the values of two operands are not equal, then condition
#                becomes true.
print(f"\nex3 = {ex3}")
#           \__> This returns the boolean value of True because 3 is not equal to 4.

# Greater Than
ex4 = (3 > 4)
#        \_____> Known as (Greater Than), If the value of the left operand is greater than the value of
#                the right operand, then the condition becomes true.
print(f"\nex4 = {ex4}")
#           \__> This returns the boolean value of False because 3 is not greater than  4.

# Less Than
ex5 = (3 < 4)
#        \_____> Known as (Less Than), If the value of  the left operand is less than the value of the right
#                operand, then the condition becomes true.
print(f"\nex5 = {ex5}")
#           \__> This returns the boolean value of True because 3 is less than 4.

# Greater Than or Equal To
ex6 = (3 >= 4)
#        \_____> Known as (Greater Than or Equal To), If the value of the left operand is greater than or
#                equal to the value of the right operand, then the condition becomes true.
print(f"\nex6 = {ex6}")
#           \__> This returns the boolean value of False because 3 is not greater than nor equal to 4.

# Less Than or Equal To
ex7 = (3 <= 4)
#        \_____> Known as (Less Than or Equal To), If the value of the left operand is less than or equal to
#                the value of the right operand, then the condition becomes true.
print(f"\nex7 = {ex7}")
#           \__> This returns the boolean value of True because 3 is less than but not equal to 4.


print("\nChaining Comparison Operators in Python with Logical Operators")
# chaining Comparison Operators in Python with Logical Operators
#                    \                                \____> [ and or not ]
#                     \____________________________________> [ == != > < >= <= ]

# The (and) Logical Operator - without parenthesis
# __> Imagine you wanted to check if 1 < 2 (and) then 2 < 3 at the same time you could write 1 < 2 < 3 this
#    would return the boolean value of true. If you were to change one of the comparison operators such as
#    1 < 2 > 3 it would return the value of False. Now you could use this sort of chaining together, but
#    alternatively you would use the Logical Operator the (and) key word as its much neater and cleaner.

ex8 = (1 < 2) and (2 > 3)
#              \_____> Known as the (and) Logical Operator or key word.
#                      (Both conditions need to be True) in order for the boolean to return the value True,
#                      otherwise its False.
#                      Note you can write the camparisons without the parenthesis, its up to your liking,
#                      certain libraries later on will need them to be in parenthesis, so best to get used to
#                      sticking the into parenthesis.
print(f"\nex8 = {ex8}")
#           \__> This returns the boolean value of False because both of the comparisons are not True.

# The (or) Logical Operator - without parenthesis
ex9 = (1 == 1) or (2 == 3)
#               \____> Known as the (or) Logical Operator or key word.
#                      Note only one of the conditions need to be True in order for the boolean to return
#                      True, Either left or right needs to be True. Both conditions need to be False in order
#                      for the boolean to return False.
print(f"\nex9 = {ex9}")
#           \__> This returns the boolean value of True even though one of the comparisons is False.

# The (not) Logical Operator - without parenthesis
ex10 = not (1 == 1)
#       \___________> Known as the (not) Logical Operator or key word.
#                     All (not) does is return the opposite Boolean value.
#                     Another example of this not (400 > 5000), which should be False as 400 is not greater
#                     than 5000, However because we added the not before it, it swapped the value to True.
print(f"\nex10 = {ex10}")
#           \__> This returns the Boolean value of False, even though it is True because we added the not
#                operator.
