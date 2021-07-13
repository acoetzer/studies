# My Python Notes
# Section 3

    # Python object and data structure basics

#__> Different Data types in Python are 
#     intergers 
#     floating points 
#     strings 
#     lists 
#     dictionairies 
#     tuples 
#     sets 
#     booleans


    # data types

#__> Integers.
ex1 = 3, 300, 200 
# integers have a type know as int(), which are whole numbers.

#__> Floating points.
ex2 = 2.3, 4.6, 100.0
# floating_points have a type known as float(), Which are numbers with a decimal point.

#__> Strings.
ex3 = "Hello World!", 'Sammy', "2000"
# strings have a type Known as str " " / ' ' / str() Which are a ordered sequence of characters.


#__> Lists.
ex4 = ["Hello World!", 10, 200.0, True]
# lists have a type == list(), [] Which is considered a data structure of a ordered sequence of objects.


# dictionaries have a type == dict {}
ex5 = {"Apples": 20.99, "key2": 2}
# dictionaries have a type == dict {} Which is also considered a data structure but of unordered key:value pairs or mappings.


#__> Tuples.
ex6 = (10, "Hello World!", 200.3)
# tuples have a type == tuple() () Which are a ordered immutable sequence of objects


#__> Sets.
ex7 = {"a", "b"}
# sets have a type == set () or .set() Which are a unordered collection of unique objects such as


#__> Booleans.
ex8 = True, False
# booleans have a type == bool True / False Which are logical values indicating True or False using the comparison 
# operators == <= >= != and logical operators such as (and) (or) (not).

# ---------------------------------
# --- basic math operators in python
# ---------------------------------

# addition which is represent by +
exam_9 = 2 + 1

# subtraction which is represented by -
exam_10 = 2 - 1

# multiplication which is represented by *
exam_11 = 2 * 1

# devision which is represented by /
exam_12 = 2 / 1

# exponents / to the power of which is represent by **
exam_13 = 2 ** 1 ("the square of")  or 2 ** 0.5 ("the square root of")

# modulo / mod which is represented by % which is the remainder after division, if return value is even then output
# will be 0, if there is a remainder for example:
exam_14 = 9 % 4
# then return == 1 remainder

# You can also do more complex math for example: 2 + 10 * 10 + 3 and this following the basic flow of
# math 2 + (10 * 10) + 3 multiplcation will be first unless stated otherwise.
exam_15 = 2 + 10 * 10 + 3
result = 105

# but what if you want to do the addition first then for example you type:
exam_16 = (2 + 10) * (10 + 3)
result = 156


# ---------------------------------
# --- variable assignments
# ---------------------------------
print("---START OF VARIABLES---\n")
# To create a variable in python all you need to do is type a name and assign the "=" sign to it and give it a value
# in the form of any data type. 
# 
# You can never start a variable with a number, nor use any other symbols/syntax apart from underscore. 
# 
# You cannot put spaces in the name but you can use an underscore "_" to seperate names, almost like snake casing in 
# functions. 
# General rule from (PEP8) is to try to keep variable lowercase as global variables are usually with all caps.
# In python you can assign the same variable with multiple data types throughout your code and not get an error.
# see example below:

my_dogs_1 = 2
my_dogs_1 = "Sammy", "Max"
# this above is totally fine within python.

# another simple example
a = 5

# then later you can change that to:
a = 10

# you can also add variables together for example:
a + a
print(a + a)
# = 20

# you can also reassign a variable to:
a = a + a
# a = 20, result is 'a' is no longer 10 but reassigned in a way to make it equal to 20, so 'a' is now 20.

# another note is if you dont know what type a variable is, you can type type(var_name)
reason_1 = "\nFor checking what type a variable is you can type print(type(var)), for this instance variable 'a' equals"
print(f"{reason_1}", type(a))

# you can also reassign the variable "a" to a floating point number and check the type again and python will give you the correct type.
a = 30.1
reason_2 = "When reassigning the variable 'a' to a float number and you check it again"
print(f"\n{reason_2}", type(a))

# Another note is you can perform logic with variable names, as an example
my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
reason_3 = "This shows that you can use logic on variable names, you can now see what your my_taxes variable is equal to"
print(f"\n{reason_3}", my_taxes)
print("\n---END OF VARIABLES---")


# ---------------------------------
# --- introduction to stings
# ---------------------------------
print("---START OF INRODUCTION TO STRINGS---\n")
# strings are a sequence of ordered characters, using the syntax of either single qoutes or double. strings can also be indexed and sliced.
# string indexing starts at 0 1 2 3 ... and it can also be reversed indexed whereby the last character in the sentence starts with -1 and then -2 -3 as
# it moves towards the beginning. You index a string by placing [brackets] next to the string or variable thats assigned with a string and then 
# assinging an index to it.

# a string can also have an escape sequence for example (\n) this telling python to begin on a new line when outputting a result.
line_break = "\nThis is \na line break"
print(line_break)

# slicing can also take place with a string by using [start:stop:step]. start being the numerical index for where the slice starts for example 3,
# stop being the index you go up to but do not include, and step being how many you skip between start and stop.

exam_str_1 = "Hello"
# with double qoutation marks
exam_str_2 = 'Hello'
# with single qoutation marks
# 
# you have both options double and single qoutation marks, because if ever you need to use a single syntax
# of qoutes you can use the other for the string and python will understand what you trying to do.

exam_str_3 = "It uses both qoutation marks so that if a word like I'm is ever needed, you could use the other syntax for the string"

# string indexing for example is when you want to grab a specific index value and return it

exam_index = "abcdefg"
# a b c d e
# 0 1 2 3 4

print(exam_index[1])

# another example is
exam_indexing = "abcdefg"

result_1 = "You index the value of 2 in the string abcdefg, this returning"

print(f"\n{result_1}", exam_indexing[2])

# string slicing for example is when you want to grab a group or sub section of index's with specified parameters of a string [start:stop:step].

exam_slice_a = "abcdefg"

result_2a = "If you want to grab from a specified index to the very end you type [2 : ] this giving the result of"

print(f"\n{result_2a}", exam_slice_a[2:])

exam_slice_b = "abcdefg"

result_2b = "You can also do the opposite, if you want to go from the beginning to a specified index but not including for example [:4] gives a result as seen here"

print(f"\n{result_2b}", exam_slice_b[:4])

exam_slice = "abcdefg"

result_3 = "You sliced the string by the starting point of 1, you stopped at 6 which is g but notice it did not include g, so this returning"

print(f"\n{result_3}", exam_slice[1:6])

# string slicing with a step

exam_slice_step = "abcdefg"

result_4 = "You did exactly the same as the last example but this time you added a step of 2, this returning"

print(f"\n{result_4}", exam_slice_step[1:6:2])

# you can check the length of string by trying the following

result_5 = "this prints the length of a string '12345' and gives the result of"

print(f"\n{result_5}", len("12345"))

# you can also check the length of a string which is assigned to a vaiable as follows

exam_length = "12345"

result_6 = "this prints the length of a string inside a variable, again same as before the string is '12345' and your result is"

print(f"\n{result_6}", len(exam_length))

# quick note about reversing strings, in python you can reverse a string by using a negative step size as follows [::-1]

exam_reverse_string = "abcdefg"

result_7 = "This shows the you can reverse a string with slicing in python using negative intergers in step size in the following way [::-1]"

print(f"\n{result_7}", exam_reverse_string[::-1])
print("\n---END OF INTORDUCTION TO STRINGS---")

# ---------------------------------
# --- string properties and methods
# ---------------------------------
print("---START OF STRING PROPERTIES AND METHODS---\n")
# immutability, which means strings are not mutable, which means again that you cannot use indexing to change individual elements of a string.
# strings in python are immutable in the sense that if you have for example

name = "Sam"

# and you want to change Sam to Pam, you cannot use the following as it will result in an error, because you cannot change a specified index.
# name[0] = "P"
# however you can concantenate strings in python, so a good example is as follows.

last_letters = name[1:]
# that would == 'am'
# we then concatenate the string 'P' with the variable assigned with am.
print("\nP" + last_letters)

# what has happened here is you assigned a new variable with the name variable that has been sliced and then concatenated "P" with "am"

print("\nanother example of string concantenation is")

x = "Hello World!"

print(x + " it is beautiful outside.")

# keep in mind of concatenating different data types for example

data_type_1 = 2 + 3

info_1 = "Here you adding intergers 2 + 3 ="

print(f"\n{info_1}", data_type_1)

data_type_2 = "2" + "3"

info_2 = "Here you are adding 2 strings together '2' + '3' ="

print(f"\n{info_2}", data_type_2)

# String methods
# .upper(), .lower(), .split()
# objects in python usualy have built in methods which are essentially functions that are inside the object, represented by ".method"
# one to take note of are .upper()

method = "hello world"

result_8 = "Here you can see the words in lower caps ="

print(f"\n{result_8}", method)

# lets to add a method to the 'method'' object / variable to make it all uppercase letters.
# method.upper()

result_9 = "Here is the same object / varaible as before but now its all in uppercase letters because we used the .upper() method / function, result as seen here = "

print(f"\n{result_9}", method.upper())

result_10 = "Note that it doesnt affect the original string as seen here ="

print(f"\n{result_10}", method)

# if you want it to affect the original string, you will have to reassign it as follows upper_method = method.upper() and then print upper_method.

# Another method is .lower(), which is essentially the opposite of .upper(), it places all letters in lowercase. lets look at an example

result_11 = "Here is the same object / variable with a different method .lower() and you can see the .lower() method makes all letter in lowercase as seen here ="

print(f"\n{result_11}", method.lower())

# another method is known as .split() which essentially splits a string / object into a list based on the white spaces inbetween or on a specified character.

split_method = "This is a nice night for knitting a kite"

result_12 = "Here we will split the sentence into a list 'This is a nice night for knitting a kite' by its white space as seen here ="

print(f"\n{result_12}", split_method.split())

result_13 = "Here we will split the same object / variable on the specific letter of 'i' as seen here ="

print(f"\n{result_13}", split_method.split("i"))
print("\n---END OF STRING PROPERTIES AND METHODS---")

# ---------------------------------
# --- print formating with strings
# ---------------------------------
print("---START OF PRINT FORMATING WITH STRINGS---\n")
# Often you will want to 'inject' a variable into a string, we know that you can concatenate a string and variable. seen in the following example

my_name = "Ben"

print("\nHello " + my_name)

# this is known as string concatenation, but there is another way called string interpolation which is basically sticking a variable into a string using
# the .format() or f-string methods.

# .format() method
# "string here {} then also {}".format("Something1", Something2)
print("\nHello, my name is {}".format(my_name))

# Advantage with this is, strings can be inserted by index position, an example of this is
print("\nThe {} {} {}".format("Fox", "Brown", "Quick"))
# notice the string will be inserted by order, you can assign a key to it if you want to call specific strings first or inorder as an example
print("\nThe {q} {b} {f}".format(f="Fox", b="Brown", q="Quick"))
# as you can see, you have assigned the string to a key word and rearranged the output of the string.
# another way to do this is with indexing as an example
print("\nThe {2} {1} {0}".format("Fox", "Brown", "Quick"))
# as you see the output is in order just by using indexing.
# with all the methods shown above you are also able to repeat the string, index or key word thoughout the curly braces if you wanted to as seen below
print("\nThe {0} {0} {0}".format("Fox", "Brown", "Quick"))
# \  this repeating the same result over and over.
#  \ -- The problem here "Too many arguments for format string, its the 0 0 0, the line only indicates not the qoutation mark but the enire string"

# f-sting method which is also a newer method injects the variable directly into the string.
# (f"string here {"Something1"} and {Something2}")
print(f"\nHello, my name is {my_name}\n")

# another thing you can do with the .format or f-strings methods is float point control. this controling the length of the decimal output.

# {value:width.precisionf} {value:1.3f}

# value is your variable, index or key word
# width is the white space between the last object and the value, generally will most times be 1
# precision is the amount of decimals you want after the 1.123 as an example.
# this works for both .format methods as seen below

result = 100 / 777
print(result)
# you get 0.1287001287001287
# now lets shorten it with both methods

print(
    "\nThe result is now shortened to 3 decimals while blank {:1.3f}".format(result))
# this without the value added
print(
    "\nThe result is now shortened to 3 decimals using indexing {0:1.3f}".format(result))
# this with the index value
print("\nThe result is now shortened to 3 decimals using key words {r:1.3f}".format(
    r=result))
# this with the key word value
# lets try the f-string method

print(
    f"\nThe result is now shortened while using the f string method {result:1.3f}")
print("\n---END OF PRINT FORMATING WITH STRINGS---")

# ---------------------------------
# --- lists in python
# ---------------------------------
print("---START OF LISTS IN PYTHON---\n")
# lists are ordered sequences that can hold a variety of object types and are mutable, which means you can change or mutate items within the list.
# they use the square brackets [ ] and objects are seperated with a comma.
# lists can also be nested inside one another as an example [[ ]], to index a nested list you will nested_list[[  ], [  ]]

nested_list_exam = [["One", "True"], ["Two", False]]
# as an exercise lets change the string True to a boolean
nested_list_exam[0][1] = True

result_nest = "Here you can see the we change the index 0 and the index 1 of the sub nest to a boolean, the result ="

print(f"{result_nest} {nested_list_exam}")

my_list_1 = [1, 2, 3, 4]
my_list_2 = ["string", 1, 200.30, True]

# these are some examples of what lists can hold.
# lists also support indexing and slicing, list can be nested and also have a variety of useful methods that can be called off of them.

# you can also check the length of a list by using the len() function

length_list = ["string", 1, 200.34, False]

result_len = "this will print out the number of elements or objects inside a list, note its not the amount of characters but elements or objects ="

print(f"\n{result_len}", len(length_list))

# lists you can also index and slice as seen in the example below

exam_list = ["One", "Two", "Three", "Four"]

# Indexing example
print(exam_list[3])
# Slicing example
print(exam_list[1:])

# You are able to change or reassign specified indexes in a list, as an example
exam_list[3] = "4"
print(exam_list)
# exam_list = ["One", "Two", "Three", "4"]

# you can also concatenate lists together

list_1 = ["1", "2", "3"]
list_2 = ["4", "5"]
list_3 = list_1 + list_2

print(list_3)


# Lists also have methods and some examples are .append(), .remove(), .pop(), .sort(), and .reverse()
# .append() Method
method_1 = ["One", "Two", "Three"]

method_1.append("Four")

result_14 = "In this example we have 'One' 'Two' 'Three' in a list and we use the .append('Four') to add a string or object to the end of the list. result ="

print(f"\n{result_14}", method_1)

# .remove() Method
method_2 = ["One", "Two", "Three"]

method_2.remove("Three")

result_15 = "Here we removed the 'Three' from the list 'One' 'Two' 'Three', the result ="

print(f"\n{result_15}", method_2)

# .pop() Method, take note that the .pop() Method only works when assigning the index number of the item you want to remove.
method_3 = ["One", "Two", "Three"]

method_3.pop(1)

result_16 = "Here we popped off the string 'Two' from the list 'One' 'Two' 'Three' using the index number. .pop() will give an error if you enter a string, the result ="

print(f"\n{result_16}", method_3)

# another example of the .pop() Method is if you leave the () blank, it will pop the last item on a list.
# You can also save a popped item to a variable as seen in the following example

method_4 = ["One", "Two", "Three"]

popped_item = method_4.pop()

result_17 = "Here you save the popped item which was three to a new variable which ="

print(f"\n{result_17}", popped_item)

# .sort() Method

method_5 = ["b", "r", "a", "d", "j", "k"]

method_5.sort()

result_18 = "Here the list will be sorted using the .sort() method the list is unordered but the result now ="

print(f"\n{result_18}", method_5)

# .reverse Method

method_6 = [5, 4, 3, 2, 1]

method_6.reverse()

result_19 = "Here the list will be reversed, using the .reverse() Method which ="

print(f"\n{result_19}", method_6)
print("\n---END OF LISTS IN PYTHON---")

# ---------------------------------
# --- dictionairies in python
# ---------------------------------
print("---START OF DICTIONAIRIES IN PYTHON---\n")
# dictionaires use curly braces and colons { : }
# dictionairies are unordered mappings for storing objects. Not the same as list which store objects in an ordered sequence.
# dictionairies use what is known as key:value pairing or mapping
# {Key1:Value1, Key2:Value2}
# dictionairies can hold different data types including another dictionairy or list
# key:value pairing allows you to grab objects without needing to know the index value of that item.
# when do you use a dictionairy vs a list, that is when you want to call a object without knowing the index value and just use the key associated to that value for example
# to call a key you use the index [ ] brackets.
# last thing to note is that unlike lists, dictionairies cannot be sorted, or sliced and you cannot call objects based on index value.
# however dict are mutable meaning you can change the values.

shopping_price_list = {"Apples": 2.99, "Chocolate": 6.99, "Milk": 2.85}
# here we call our dictionairy
print(shopping_price_list)
# here we called a specific key to check its value
result_20 = "Here we called the price, by searching the key named 'Apples' from our list above, result ="

print(f"\n{result_20}", shopping_price_list["Apples"])

# dictionairies are flexible in the data types they can hold, for example you can have a list within the dictionairy as well as another dictionairy, shown in the example below

multi_data_types = {"Apples": 2.99, "List": [1, 2, 3], "dict": {"inside dict": "inside value"}}

# if you want to call the list above which is nested in the dictionairy

result_21 = "Here you pulling the list value which is nested inside a dictionairy and the result ="

print(f"\n{result_21}", multi_data_types["List"])

# you can even pull a specific value from the list as shown below using the same method as in the nested list indexing example

result_22 = "Here you pulling the value from the list using the nested indexing method [ ] [ ], result ="

print(f"\n{result_22}", multi_data_types["List"][1])

# You can use methods suchs as .upper() in a dictionairy, shown in an example

uppercase = {"letters": ["a", "b", "c"]}

result_23 = "Here we call the key 'letters' and the sub object b to make it capital, using the .upper() Method, result ="

print(f"\n{result_23}", uppercase["letters"][1].upper())

# you can also add to a dictionairy, as seen below

add_to_dict = {"k1": 100, "k2": 200, "k3": 300}
add_to_dict["k4"] = 400

result_24 = "Here we added 'k4' with a value of 400 to the dictionairy"

print(f"\n{result_24}", add_to_dict)

# you can also overwrite a value in the same method
add_to_dict["k1"] = "apples"

result_25 = "Here we are overwriting the value of k1 to be apples as an example, result ="

print(f"\n{result_25}", add_to_dict)

# few methods of dictionairies are .keys(), .values(), .items()

dict_methods = {".keys()": 1, ".values()": 2, ".items()": 3}

result_26 = "Here we call the all the keys in a dictionairy, using the .key() method, result ="

print(f"\n{result_26}", dict_methods.keys())

result_27 = "Here we call all the values in a dictionairy, using the .values() Method, result ="

print(f"\n{result_27}", dict_methods.values())

result_28 = "Here we call all the items in a dictionairy, using the .items() Method, take note that with this method you will see brackets around the dictionairy items which are also known as tuples"

print(f"\n{result_28}", dict_methods.items())
# quick note on the .items() is that  it will bring back the list in a for
# a tuples, which you will later learn about tuple unpacking.
print("\n---END OF DICTIONAIRIES IN PYTHON---")

# ---------------------------------
# --- tuples in python
# ---------------------------------
print("---START OF TUPLES IN PYTHON---\n")
# tuples use () parenthesis
# Tuples are very similair to lists, however instead of [] brackets, tuples use () parenthesis.
# tuples are also immutable, meaning that once something is inside a tuple it cannot be reassigned.
# you can also mix different data types within a tuple.

tup = (1, 2, 3)

result_29 = "This checks the type, result ="

# check the type of variable
print(f"{result_29}", type(tup))

result_30 = "This checks the length of a tuple, the same as a list, result ="
# check the length of a tuple like a list
print(f"\n{result_30}", len(tup))

result_31 = "Here you can index a tuple as well, result ="
# you can call a specific index of a tuple as well, note -1 negative indexes work as well.
print(f"\n{result_31}", tup[0])

result_32 = "You can also slice a tuple as shown here, result ="
# you can slice a tuple as well
print(f"\n{result_32}", tup[0:])

result_33 = "You can reverse a tuple as well, result ="
# reversing a tuple with negative slicing
print(f"\n{result_33}", tup[::-1])

# there are also 2 basic methods for tuples, that is the .index(), .count() Method

tuple_method = ("Apples", "Apples", 300.92, False)

result_34 = "Here we have a method for tuple, the .count() Method which will show how many of a certain object is repeated in the tuple, result ="
# .count() Method, shows how many of an item or object is repeated within the tuple.
print(f"\n{result_34}", tuple_method.count("Apples"))

result_34 = "Here we have the .index() Method which returns the index of the very first time the specified index is located, result ="
# .index() returns the very first specified search of an object located within the tuple
print(f"\n{result_34}", tuple_method.index(False))
print("\n---END OF TUPLES IN PYTHON---")

# ---------------------------------
# --- sets in python
# ---------------------------------
print("---START OF SETS IN PYTHON---\n")
# set()
# sets are basically unordered collections of unique elements.
# this meaning that there can only be one representative of the same object.

# lets create a set by assigning it  to a variable

myset = set()

note = "If you print 'myset' it will bring back an empty set, result ="

print(f"{note}", myset)

# lets assign myset with a object with .add()

myset.add("a")

note_2 = "Now if we call myset, you will notice the object 'a' has been added to myset"

print(f"\n{note_2}", myset)

# lets try to add another a and you will notice nothing happens, it just stays as 1 single 'a'
myset.add("a")

note_3 = "Lets try to add another 'a' to see that nothing will be added, it will continue to show you 1 single 'a', we can run the .add() method again with a different letter to see if everything is correct, proving that if the second output put a different value that it ill not display multiple unique objects, result ="

print(f"\n{note_3}", myset)

myset.add("b")

note_4 = "Note the 'b' was added, meaning the statement is true that it wont support multiple unique objects. Another note to take in is how the set stays unordered"

print(f"\n{note_4}", myset)

# another good example, to show that set take unique items

mylist = [2, 2, 2, 2, 5, 5, 5, 7, 7, 7]
myset_2 = set(mylist)

note_5 = "Here take note that a list was embedded into the set, as follows, myset = set(mylist). Also take note that it doesnt repeat object as the original mylist example, result ="

print(f"\n{note_5}", myset_2)
print("\n---END OF SETS IN PYTHON---")

# ---------------------------------
# --- booleans in python
# ---------------------------------
print("---START OF BOOLEANS IN PYTHON---\n")
# booleans also known as bool are operators that allow you to convey True and False statements.
# this is important later on as it deals with control flow and logic.
# booleans start with capital T and F
# you dont always deal directly with true or false, but you use comparison operators to determine True or False

# basic examples

bool_1 = 1 == 1

note_6 = "Here we are checking if 1 == 1 (equal to), result ="

print(f"\n{note_6} {bool_1}")

bool_2 = 1 > 3

note_7 = "Here we are checking if 1 > 3 (greater than), result ="

print(f"\n{note_7} {bool_2}")

# these are known as comparison operators, but what they return are known as booleans
# this will come in handy when working with logic in your code.
print("\n---END OF BOOLEANS IN PYTHON---")

# ---------------------------------
# --- placeholder in python
# ---------------------------------
print("---START OF PLACEHOLDER IN PYTHON---\n")
# if you dont want to assign anything to a object or variable, you can use the word or placeholder None.
# this is great if you want to run code without getting any errors telling you that you havent yet assigned the object to anything.

example = None
# you can also check this the example and it should return none

note_8 = "Here we are checking the type for example, result should equal to None, result ="

print(f"\n{note_8 }", type(example))
print("\n---END OF PLACEHOLDER IN PYTHON---")

# ---------------------------------
# --- I / O files in python
# ---------------------------------
print("---START OF I / O IN PYTHON---\n")
# quick note on I / O, meaning of this is INPUT AND OUTPUT
# the methods shown here, expand to other files types as well, such as audio, text, excel, emails, documents, a lot covered here will be relatable to those files types as well.
# keep in mind for some of those other file types you might need to install libraries.

# you can create a text file (.txt) and open it within python, now you can manually create this .txt file outside of python or you can create the file within python using the mode write.
# for now we have created a file outside of python called myfile.txt which holds 3 lines of text.

# to open this file, you can do the following

myfile = open("myfile.txt")

# now if you get the file not found error or [Errno 2], then one of 2 things have happened, and that is you either input the wrong file name or the file is not in the same directory as the
# python file directory.
# how ever if it displays no error message, then it means all is ok and you can continue to read the file.
# take note that, in Visual Studio Code, you cannot place this file within a folder or sub folder as it doesnt read it, however you can use the direct directory path to link it.

# to read the file you can type myfile.read() inside the print function

print(myfile.read())

# take note that once we have read the file we cannot read it again, as for example the cursor is now at the end of the text file and you will need to reset that cursor using a method known as .seek() which we will get to shortly.
# lets discuss the output of read, in some editors you will see the out of .read as a single line string which will include escape sequences such as \n to indicatate a line break. Here is an example oh what you could see
# "Hello this is a text file\nThis is the second line\nThis is the third line"
# however in this editor it already seperarates those lines how they are written in the .txt file, just something to take note of.
# later we will also discuss how to read the .txt file with the .readlines() method in order to view the .txt file as its written, meaning with escape sequence or in lines.

# now if we want to read this file again, you will notice that nothing appears on your console or output. this is because if you imagine a cursor, this cursor has shifted to the end of the .txt file and no longer has anything to input.
# therefor we use the .seek() method  with a  value of 0 to reset this cursor back to the beginning.
# another note is you can also print the .seek() method to see the output as zero confirming it has reset.
# lets try to read this file as an example and then reset it and try again to see the output.

print(myfile.read())
# notice there is nothing in the output
# lets reset it

print(myfile.seek(0))
# now lets read it again

print(myfile.read())
# now you see the text from the .txt file again.

print(myfile.seek(0))

# you can save the contents of the file to a variable and as seen you can print the varaible multiple times without needing to reset the .read() method
content = myfile.read()

print(content)

# as mention earlier there is a way to output the text in the .txt file on seperate line using the .readlines() method as shown below

# first lets to reset it, otherwise you just get empty brackets
print(myfile.seek(0))

# now we we can print the .readlines() method
print(myfile.readlines())
# note that when doing so it will display the lines of the .txt file in a list form. hence making each line an object or element, whereby you can index off of the list or use looping

print(myfile.seek(0))

# file locations, we have seen that you can open a file when the file is in the same directory, so what happens if you want to open a file in another location on the computer.
# If you want to open a file in a another location, simply input the entire file path
# for windows it will look something like this

# myfile = open("C:\\Users\\Username\\Folder\\myfile.txt")

# take note of the double backslash \\ this is because you dont want to accentally confuse python with a escape sequence whereby a file might start with a small letter n

# for mac or linux it will look something like this

# myfile = ("/Users/YouUserName/Folder/myfile.txt")

# take note here we dont need to worry about double back slashes as we dont use a back slash \

myfile.close()
# take note of the above syntax, this is best to get used to for best practises within python when opening a file.
# if you do not close this, you cannot open this file on your computer later on, as python is still using it.

# there is another way to overcome this step using another syntax which will be shown here however before doing so you can run the .read() method again to test and make sure the file is closed and usually you will get an error stating that you trying to run a .read() method on a  closed file

# print(myfile.read())

# lets looks at the other way of typing the new syntax for opening a file

with open("myfile.txt") as x:
    contents = x.read()

print(content)

# notice the indentation after the : and what this means is that any code that is within this block of code is going to use "x" as the variable for the .txt file.

# lets to continue with taking a look at how to read and write to a files even overwrtie files
# here is a list of the various modes for the format
# mode = "r" : read only
# mode = "w" : is to write only (will overwrite files or create new)
# mode = "a" : is to append only (will add on to files)
# mode = "r+" : is reading and writing
# mode = "w+" : is writing and reading (Overwrites existing files or creates a new file!)

with open("myfile.txt", mode="r") as read:
    contents = read.read()

print(contents)

# lets create a new file using this method

with open("newfiletest.txt", mode="w") as newfile:
    newfile.write(
        "I create this file within python\nThis should be the second line in this file")
    # note we create a new .txt file using the mode "w", we also added an escape sequence so that we can have a second line and then ran the code

with open("newfiletest.txt", mode="r") as newfile:
    print(newfile.read())
    # we then rewrote the syntax to read only, so we can print the result and see if it worked

with open("newfiletest.txt", mode="a") as newfile:
    newfile.write(
        "\nthis should add a thrid line to the text file, while using the .append method")
    # we then added to the file another line using the append method and ran the code

with open("newfiletest.txt", mode="r") as newfile:
    print(newfile.read())
    # we then changed to mode to read only to see the output and read the file and see if it wrote to the file which it did

with open("newfiletest.txt", mode="r") as newfile:
    new_contents = newfile.read()

print(new_contents)
# lastly we then reassign the varaible associated with the .txt to a new variable so we can run it as we want.
print("\n---END OF I / O IN PYTHON---")
