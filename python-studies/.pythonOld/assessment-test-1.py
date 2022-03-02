# Assessment Test 1

# part 1
p1 = "Part 1"
h1 = "Test your knowledge:"
print(f"{p1} \n{h1}")

# Question 1 of part 1
q1_1 = "\nQuestion 1:\nWrite a brief description of all the following Object types and Data structures we have learnt about."

a1_1 = """

- Numbers : Numbers in python are known as either int for intergers or floats for floating points. 
Intergers are whole numbers such as 1, 200, 1000, whereas floats are decimal numbers such as 1.3, 200.30 or 1000.25.

- Strings : Strings are ordered sequence characters defined by qoutation marks, single or double, that is printed out to convey or give a message to the user. 
Anything inside a string whether it be a letter or number is a character in the sense that if you put an int into a string, and python no longer sees it as a int but as a character.
Therefor if you had to try to use a operator such as +, then the string it will only be joining characters together which is known as string concantenation.
Strings are also immutable, however you are able to index and slice a string.
You are able to use methods on strings such as .upper(), .lower(), .sort() and .reverse()

- Lists : Lists are mutable, lists are a order sequence of objects or elements that can hold multiple data types. 
you can also nest a list within a list. A list sits inside square brackets and is usually assigned to a variable of some sort. 
You can change specific elements or objects within a list as well as index and slice a list. You can concantenate lists together as well as add objects or elements to a list use various methods such as .append(), 
however this will add the items to the very end of the list. You also have the .remove() and .pop() methods as well. 

- Tuples : Tuples are a immutable sequence of ordered objects and elements, this that once something is inside a tuple you cannot change it, 
tuples are the same as lists in the sense that you can index and slice objects and elements. Tuples unlike lists have a very limited amount of methods assigned to it, 2 methods known is the  .index() and .count() methods. 
They also differ from a list in the sense that a list uses square brackets [] and tuples use parenthesis ()

- Dictionairies : Dictionairies are a unordered mutable mappings that are key:value pairs, they use curly braces {} and are similair to lists with the difference that you no longer need to know the index of a specific element, 
instead you just need to know the key to get the value. Dictionairies can hold different data types just like lists, they can even have a nested dictionairy. Dictionairies can be indexed as well mutable in the sense 
that you can change specific values within the dictionairy.
why use a dictionairy over a list, and that is when you dont want to lookup the index value for a specified object instead you just use the key to get the value making it easier to work with.
some methods known with dictionairies are the .keys(), .values(), .items() methods

- Sets : Sets are a collection of unordered unique items, you cannot repeat an object or element within a set. you create a set by assigning it to a variable, sets use parenthesis but output in curly braces.
You can add to a set() by using the  .add() method
"""

print(f"{q1_1} {a1_1}")

# Part 2
p2 = "Part 2"
h2 = "Numbers:"
print(f"{p2} \n{h2}")

# Question 1 of part 2
q2_1 = "Question 1: \nWrite an equation that uses multiplication, division, an exponent, addition and subtraction that is equal to 100.25"

a2_1 = (8 / 2 * 2) ** 2 + 37 - 0.75

print(f"\n{q2_1} \n The answer is (8 / 2 * 2) ** 2 + 37 - 0.75 = {a2_1}")

# Question 2 part 2
q2_2 = "Question 2: \nAnswer these 3 questions without typing code. Then type code to check your answer. \n1. What is the value of the expression 4 * (6 + 5) \n2. What is the value of the expression 4 * 6 + 5 \n3. What is the value of the expression 4 + 6 * 5"

a2_2 = """

1. = 44
2. = 29
3. = 34
"""

code1 = 4 * (6 + 5)
code2 = 4 * 6 + 5
code3 = 4 + 6 * 5

print(f"\n{q2_2} {a2_2} \nCode Check \n1a. = {code1} \n2a. = {code2} \n3a. = {code3}")

# Question 3 of part 2
q2_3 = "Question 3: \nWhat is the type of the result of the expression 3 + 1.5 + 4?"

a2_3 = """

The type is what is know as a float, because the answer equals to 8.5, however we can use code to check if the result is correct by using the type() function
"""

code4 = 3 + 1.5 + 4

print(f"\n{q2_3} {a2_3} \nCode Check \n", type(code4))

# Question 4 of part 2
q2_4 = "Question 4: \nWhat would you use to find a number's square root, as well as its square?"

a2_4 = """

The Square Root of 49 ** 0.5 = 7

The Square of 7 or 7 ** 2 = 49
"""

code5 = 49 ** 0.5
code6 = 7 ** 2

print(f"\n{q2_4} {a2_4} \nCode Check \n49 ** 0.5 = {code5} \n7 ** 2 = {code6}")

# Part 3
p3 = "Part 3"
h3 = "Strings:"
print(f"\n{p3} \n{h3}")

# Question 1 of part 3
q3_1 = "Question 1: \nGiven the string 'hello' give an index command that returns 'e'."

a3_1 = """

You would type print('hello'[1]) and that would return the index value of 'e', we can prove this with code.
"""

print(f"\n{q3_1} {a3_1} \nCode Check")
print("hello"[1])

# Question 2 of part 3
q3_2 = "Question 2: \nReverse the string 'hello' using slicing"

a3_2 = """

To reverse the string you will us a negative interger on the step, for example print("hello"[::-1]), we can check the code to see if we are correct
"""

print(f"\n{q3_2} {a3_2} \nCode Check \n")
print("hello"[::-1])

# Question 3 of part 3
q3_3 = "Question 3: \nGiven the string 'hello', give two methods of producting the letter 'o' using indexing"

a3_3 = """

You retrieve the letter 'o' by either using a postive index number for example print("hello"[4]) or you can use a negative interger for example print("hello"[-1]), we can check the code to see if we are correct
"""

print(f"\n{q3_3} {a3_3} \nCode Check \n")
print("hello"[4], ": Positve indexing [4]")
print("hello"[-1], ": Negative indexing [-1]")

# Part 4
p4 = "Part 4"
h4 = "Lists:"
print(f"\n{p4} \n{h4}")

# Question 1 of part 4
q4_1 = "Question 1: \nBuild this list [0,0,0] two seperate ways"

a4_1 = """

Method 1 would be to concatenate two lists together for example x = [0, 0] and y = [0] z = x + y.
Method 2 would be to .append(0) to x = [0, 0]
Method 3 would be to multiply the list by 3 like so list_2 = [0] * 3
Method 4 would be to just create the list like so list_3 = [0, 0, 0]
"""
list_x = [0, 0]
list_y = [0]
list_z = list_x + list_y

list_1 = [0, 0]
list_1.append(0)

list_2 = [0] * 3

list_3 = [0, 0, 0]

print(f"\n{q4_1} {a4_1} \nCode Check \n{list_z} \n{list_1} \n{list_2} \n{list_3}")

# Question 2 of part 4
q4_2 = "Question 2: \nReassign 'hello' in this nested list to say 'goodbye' instead. list3 = [1, 2, [3, 4, 'hello']]"

a4_2 = """

This is how you will write the code to reassign the string 'hello' to 'goodbye' 
list_2 = [1, 2, [3, 4, "hello"]]
list_2[2][2] = "goodbye"
lets to do a code check to see if its correct. 
"""
list_2 = [1, 2, [3, 4, "hello"]]
list_2[2][2] = "goodbye"

print(f"\n{q4_2} {a4_2} \nCode Check \n{list_2}")

# Question 3 of part 4
q4_3 = "Question 3: \nSort the list below \nlist4 = [5, 4, 3, 2, 1]"

a4_3 = """

The way you will sort the list is to use the 1 of 2 methods first is known as .sort() and example of this would be 
list_3 = [5, 4, 3, 2, 1]
list_3.sort()
The second would be a function known as sorted(list_3) which will return the list itself
"""

list_3 = [5, 4, 3, 2, 1]
list_3.sort()

print(f"\n{q4_3} {a4_3} \nCode Check \n{list_3} \n")
print("using sorted() method :", sorted(list_3))

# Part 5
p5 = "Part 5"
h5 = "Dictionairies:"
print(f"\n{p5} \n{h5}")

# Question 1 of part 5
q5_1 = "Question 1: \nUsing keys and indexing, grab the 'hello' from the following dictionairies : \n1. d = {'simple key' : 'hello'} \n2. d = {'k1' : {'k2' : 'hello'}} \n3. d = {'k1' : [{'nest_key' : ['this is deep', ['hello']']}]} \n4. d = {'k1' : [1, 2, {'k2' : ['this is tricky', {'tough' : [1, 2, ['hello']]}]}]}"

a5_1 = """

The way you would index this is as follows
print(dict_1["simple key"])
print(dict_2["k1"]["k2"])
print(dict_3["k1"][0]["nest_key"][1][0])
print(dict_4["k1"][2]["k2"][1]["tough"][2][0])
"""

dict_1 = {"simple key": "hello"}
dict_2 = {"k1": {"k2": "hello"}}
dict_3 = {"k1": [{"nest_key": ["this is deep", ["hello"]]}]}
dict_4 = {
    "k1": [1, 2, {"k2": ["this is tricky", {"tough": [1, 2, ["hello"]]}]}]}

print(f"\n{q5_1} {a5_1} \nCheck Code \n")
print(dict_1["simple key"])
print(dict_2["k1"]["k2"])
print(dict_3["k1"][0]["nest_key"][1][0])
print(dict_4["k1"][2]["k2"][1]["tough"][2][0])

# Question 2 of part 5
q5_2 = "Question 2: \nCan you sort a dictionairy? Why or Why not?"

a5_2 = """

You cannot sort a dictionairy as dictionairies are unordered key mappings they are not the same as lists therefor you do not need to know the index value of an item to can call the object or element. normal dictionairies are mappings not a sequence
"""

print(f"\n{q5_2} {a5_2}")

# Part 6
p6 = "Part 6"
h6 = "Tuples:"
print(f"\n{p6} \n{h6}")

# Question 1 of part 6
q6_1 = "Question 6: \nWhat is the major difference between tuples and lists?"

a6_1 = """

The major diffference between a tuple and a list is that lists are mutable whereas tuples are not, meaning you cannot change values within a tuple once it is in a tuple
"""

print(f"\n{q6_1} {a6_1}")

# Question 2 of part 6
q6_2 = "Question 2: \nHow do you create a tuple?"

a6_2 = """

You create a tuple with parentesis ()
"""

tup = (1, "a", "b")


print(f"\n{q6_2} {a6_2} \nCode Check \n", type(tup))

# Part 7
p7 = "Part 7"
h7 = "Sets:"
print(f"\n{p7} \n{h7}")

# Question 1 of part 7
q7_1 = "Question 1: \n What is unique about a set?"

a7_1 = """

A set is unique because it holds a collection of unique object or elements that cannot be repeated.
"""

print(f"\n{q7_1} {a7_1}")

# Question 2 of part 7
q7_2 = "Question 2: \nUse a set to find the unique values of the list below \nlist_5 = [1, 2, 3, 33,4, 4, 11, 22, 3, 3, 2]"

a7_2 = """

The way you would do that is place the list within the set by assigning a new variable as an the example below
list_5 = [1, 2, 3, 33,4, 4, 11, 22, 3, 3, 2]
uniq = set(list_5)
"""

list_5 = [1, 2, 3, 33, 4, 4, 11, 22, 3, 3, 2]
uniq = set(list_5)

print(f"{q7_2} {a7_2} \nCode Check \n {uniq}")

# Part 8
p8 = "Part 8"
h8 = "Booleans:"
print(f"\n{p8} \n{h8}")

# Question 1 of part 8
q8_1 = "Question 1: \nWhat will be the resulting Boolean of the following pieces of code (answer first then check by code) \n1. 2 > 3 \n2. 3 <= 2 \n3. 3 == 2.0 \n4. 3.0 == 3 \n5. 4 ** 0.5 != 2"

a8_1 = """

1. False
2. False
3. False
4. True
5. False
"""

b1 = 2 > 3
b2 = 3 <= 2
b3 = 3 == 2.0
b4 = 3.0 == 3
b5 = 4 ** 0.5 != 2

print(f"\n{q8_1} {a8_1} \nCode Check \n1a. {b1} \n2a. {b2} \n3a. {b3} \n4a. {b4} \n5a. {b5}")

# Question 2 of part 8
q8_2 = "Question 2: \nWhat is the boolean output of the cell block below? \nl_one = [1, 2, [3, 4]] \nl_two = [1, 2, {'k1' : 4}] \n\n True or False? \nl_one[2][0] >= l_two = [2]['k1']"

a8_2 = """

Its false, because 3 is not greater than 4
"""
l_one = [1, 2, [3, 4]]
l_two = [1, 2, {'k1': 4}]

print(f"\n{q8_2} {a8_2} \nCode Check \n")
print(l_one[2][0])
print(l_two[2]["k1"])
