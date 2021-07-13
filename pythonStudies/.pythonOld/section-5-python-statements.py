# My Python Notes
# Section 5

# Python Statements

from random import randint
from random import shuffle


print("if, elif and else Statements and control flow")
# if, elif and else Statements and control flow

# Control Flow
# __> What is control flow?, Control flow basically allows us to use logic to execute code when we want to. Often
#    you have larger pieces of code and you only want certain pieces of code to execute once the conditions have
#    been met. Imagine you trying to program a robot to feed your dogs, you would for example say (if) my dog is
#    hungry which is the condition, then feed the dog which is the action. Another example one could use
#    is if you wake up in the morning, you look out the window to check if its sunny, if true then go water
#    the plants, if false stay inside.

# __> In order to control this flow of logic, you use key words known as if, elif and else. Note that control
#    flow syntax makes use of colons and indentation otherwise known as (Whitespece). This Indentation system
#    is crucial to Python and what sets it apart from other programming languages.

# Syntax of an (if Statement)
# if some_condition:
# execute code
#         \____> (if) (which is a keyword) some_condition which is usually some sort of comparison operation
#                mentioned in the previous section. for example,
#                if hungry == True:
#                   execute action
#                 \__> Notice the indentation below the (if statement), this is the block of code that will be
#                      executed once the (if statements) condition has been met.
#
# elif some_other_condition:
# do something different
#         \____> If you want to check for multiple conditions before the (else statement) is executed.
#                You can add a (elif statement).
#                You can have as many of these (elif statements) as you want.

# else:
# do something other
#         \____> To build on to the (if Statement) you can add a (else statement), lets say that the condition is
#                not True, you can have another block of code execute such as the (else statement).
#                Notice that the (else statement) does not have a condition attached to it and thats because it
#                only executes if the conditions above has not been met.
#                Also Notice how the syntax line up, the if, elif and else all line up and are not indented.

# Some Examples
if True:
    print("\nIt's True!")
#         \__> Notice we are saying that if some condition is True it will print It's True, usualy you wont have a
#              boolean on its own like this as you will always be printing that string. Instead you might have a
#              comparison operation such as,
if (3 > 2):
    print("It's True!")
#         \__> Notice using the comparison operator greater than.

    # Another example is
hungry1 = True
if hungry1:
    print("Feed Me!")
#         \__> If you have to set hungry as False it will not print anything in return.

    # Lets to try and run the (else statement) with a false condition or a condition that is not met.
hungry2 = False
if hungry2:
    print("Feed Me!")
else:
    print("I am not hungry")
#         \__> Notice the (else statement) has executed, because the if condition was not met. In this case it
#              printed I am not hungry as the condition was not met.
# __> Note that hungry is being passed by itself as a boolean and you dont actually need to do something like this
#    if hungry == True:
#            because hungry by itself is already a boolean.

    # Another example
loc = "Bank"
# \____> loc is a variable and in this case means location

if loc == "Auto Shop":
    print("Cars are cool!")
elif loc == "Bank":
    print("Money is cool!")
elif loc == "Store":
    print("Welcome to the store!")
else:
    print("I do not know much")
#         \__> This entire exmaple shows how to add multiple conditions to an (if statement).
#              Note that it doesnt print all statements, if the original (if statement) is not met, it will
#              go down the list checking each one until it finds or does not find the desired condition, in that
#              case it will print the else statement.

    # Another example
name = "Sammy"

if name == "Frankie":
    print("Hello Frankie!")
elif name == "Sammy":
    print("Hello Sammy")
else:
    print("What is your name?")
#         \__> Typically with your else condition, its going to be something where none of the other
#              conditions were met, so a good thing to do here is to ask the user what their name is, as the
#              condition you are looking for has not been met so you would type something like What is your name
#              because the condition is searching for their name!


print("\nFor Loops in Python\n")
# For loops in Python

# Iteration and what it means,
# __> Many objects in Python are (iterable), meaning we can iterate over every element in the object.
#    Such as every element in a list or every character in a string. We can use (for loops) to execute
#    a block of code for every iteration meaning every character in a string or element in a list.

# __> The term iterable, means you can (iterate) over the object, which essentially means you can perform
#    an action for every thing in that object. which means the string is an iterable object and as an example,
#    you can iterate over every character in a string, whereby you can iterate through that string and then do
#    something for every character for example you might want to print every single letter in that string and the
#    block of code will loop/repeat itself for every character or letter.
#    Another example is, you can iterate over every item in a list as well as iterate over every key in a
#    dictionairy, which means both lists and dictionairies are iterable.

# __> Its a strange term to get use to, but think of it as a way of going through something.

# Syntax of a for loop (for_in)
# my_iterable = [1, 2, 3]
#         \__> This could be any name you choose. Notice that the list has 3 elements, items within it so
#              therefor this loop will repeat itself 3 times.
# (for) item_name (in) my_iterable:
#         \__> (for) which is the key word, item_name which is the temporary vairable name which will act
#              as a placeholder for the elements within that list/iterable and then another key word (in)
#              and then the pre defined variable name containing the list.
#       print(item_name)
# 1
# 2
# 3

# Some Examples
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in mylist:
    #        \__> Note that the variable name is (num), its only num because for this instance its a good
    #             representation of whats in the list, you can change the variable to whatever name you want.
    #             However the iterable mylist is pre-defined and cannot change so therefor mylist will stay mylist.
    print(num)
#        \__> Another note here is that you technically dont need to print num, you can run any block of code
#             here however it will iterate according to the amount of characters or elemnets in the iterable.
for num in mylist:
    print("\nHello")
    #        \__> Here we did the same for loop as above however changed the block of code to print "Hello" 10 times
    #             as there are 10 elements in the list, something intersting to take note of here, is you placed a
    #             (\n) escape sequence to originally seperate Hello from the numb variable of the last output,
    #             however because the code repeats itself it placed a escape sequence for every output of "Hello".

    # Another Example
    # Combing for loops with a bit of control flow
print("\nCombining for loops with control flow\n")

# to print the even number in the list. You could do the following.

for num in mylist:
    if num % 2 == 0:
        #        \__> What we have done here is added some control flow into our (for loop) by adding an if statement
        #             saying, If (num) can be divided by 2 and its outcome/remainder is == 0 then print(num)
        print(num)
#        \__> We can add even more control flow by adding an (else statement), lets take a look at the next example.

for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd Number: {num}")
#        \__> We added an else statement introducing more control flow, So for every condition met, there is a
#             condition not met, this represented by the else statement and odd numbers. Meaning when it
#             goes through its first iteration, its not going to meet the first if condition, therefor it will
#             print the else condition, once it repeats for the second iteration, it will then meet the condition
#             and print the first condition.
#             Key notes here is to note this is a good example showing how (for loops) can be combined with (if statements)
#             as well as taking note of the indentations.

    # Another Exmaple
    # Keeping a running tally with a for loop
list_sum = 0
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in mylist:
    list_sum = list_sum + num
#        \__> We are trying to get the sum for every element/number in that list. So list_sum is equal to 0 and
#             then we tell the code to add (num) to list_sum. So it will go 0 + 1 = 1, then repeat, but because we
#             assigned list_sum to a calculation, it will save the updated list_sum and then repeat itself going
#             onto 1 + 2 = 3, then 3 + 3 = 6, then 6 + 4 = 10 and so on. This is known as the sum of.
print(list_sum)
#        \__> Here we will get a single answer of 55, take note as of why, and that is because we are no longer
#             inside that block of code/loop and so the operation will happen only once and only give us the end result,
#             instead of showing us the iteration.
#             Lets take a look at when it is in the block of code.
list_sum = 0

for num in mylist:
    list_sum = list_sum + num

    print(list_sum)
#        \__> Here we placed the print() within the block of code, notice the indentation. Here it will print
#             every sum as it iterates over the elements in the list, almost like a running tally.

    # Another Example
    # for loops in a string
mystring = "Hello World!"

for letter in mystring:
    print(letter)
#        \__> Here we can see how the iteration can work through a string. Technically you dont need to assign a
#             variable with a string you could just place the string where the iteration variable would normally go, as example.

for letter in "String Here!":
    print(letter)
#        \__> Here you can see you replace the iterable variable with an actual string.

    # Another Example
    # iterating through a tuple and tuple unpacking
tup = (1, 2, 3)

for item in tup:
    print(item)
#        \__> This so far the same as lists, however lets take a look at tuple unpacking by creating a list
#             of tuples.

mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
#             \__> Here we creating some tuple pairs. In this list we have 4 items, and for every single item we
#                  have a tuple pair.
#                  This sort of data structure is extremely common in python and later on we going to see that a
#                  lot of built in python functions return tuples and  this kind of structureis used with tuple 
#                  unpacking.
#                  So lets print out the items in the list.
for item in mylist:
    print(item)
#        \__> Here we print out the tuple pairs.
# (1, 2)
# (3, 4)
# (5, 6)
# (7, 8)

    # Tuple unpacking
for (a, b) in mylist:
    #      \__> This is called tuple unpacking.
    print(a)
    print(b)
#        \__> Where you are duplicating the structure of the items in the list or tuple, in this case
#             tuples inside of the [(1, 2),(3, 4),(5, 6),(7, 8)] sequence and then unpack them, so now you have
#             access to the individual items. So if you only want to print out the the first item in those
#             tuples, you can write just print (a) as like the example below.
for (a, b) in mylist:
    print(a)
#        \__> This will only give you back the first items in the tuple pair sequence. Note you can do this
#             without the parenthesis for example a, b

my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for (a, b, c) in my_list:
    print(b)
#        \__> This will only print out the middle numbers of each item as another example of tuple unpacking.

    # Another Example
    # how to iterate through a Dictionairy

d = {"k1": 1, "k2": 2, "k3": 3}

for item in d:
    print(item)
#        \__> Note when you iterate through a dictionary, you only iterate through the keys. However if you want
#             to iterate through the items themselves you will need to call .items() off of d.
for item in d.items():
    print(item)
#        \__> Now it will print out the tuple pairs ('k1', 1), ('k2', 2), ('k3', 3), which means we can use tuple
#             unpacking by copying the data structure of a dictionairy. lets have a look at an example.
for key, value in d.items():
    print(value)
#        \__> Now it will only print out the values in the dictionairy. So by default when you iterate through a
#             dictionairy its going to return the keys, If you want to call the items as well you would call
#             .items() off of d. which you can then use tuple unpacking.
#             If you only want the values you can also fo the following.
for value in d.values():
    print(value)
#        \__> This will only print the values.
# __> keep in mind that when you iterate through a dictionairy you wont always get it back in the order
#    you put them in.


print("\nWhile loops in Python\n")
# While loops in Python

# __> While loops will continue to execute a block of code while some condition remains True.
#    returning to our example earlier, while its still raining outside, continue to clean the house, or while
#    my pool is not full, keep filling my pool with water, or while my dog is hungry, continue to feed it.

# Syntax of a (while loop)
# while some_boolean_condition:
# do something
#            \__> do something represents the block of code that will continue to execute while the condition is
#                 true.
# else:
# do something different.
#            \__> Now we can also combine a while statement with a else statement if we want. for example while
#                 some boolean condition is true, do something else meaning once that condition is no longer
#                 true, or since the beginning it was no longer true, we do something different.

# Some Examples
# Basic while loop

x = 0

while x < 5:
    print(f"The current value of x is {x}")

    x = x + 1
#            \__> Take note that we reassigned x to a calculation within the block of code, this because if not done,
#                 the while loop will continue to run causing a crash or freeze because x will stay at 0.
#                 With this, the output will go up until 4 and not print 5, why because 5 is not less than 5 as the condition
#                 states or wants, nor does the condition ask for it to be <= to 5.
#                 This condition will continue to run while the condition is met, so once x is no longer less than
#                 5 it will stop.
#                 Another way to write x = x + 1 is x += 1

y = 0

while y < 5:
    print(f"The current value of y is {y}")

    y += 1
#      \__> Take note of this, its the same thing as x = x + 1, its just a more compact way of writing it. lets
#           now attach an else statement to the while loop.

z = 0

while z < 5:
    print(f"The current value of z is {z}")

    z += 1
else:
    print("z is no longer less than 5")

# __> Quick Note

z = 50

while z < 5:
    print(f"The current value of z is {z}")

    z += 1
else:
    print("z is no longer less than 5")
#      \__> If z right off the bat, was greater than 5, it would only output the else statement, if you
#           didnt have the else statement then nothing will happen as the code wont execute.


print("\nUseful keywords for using with loops\n")
# Some useful keywords for using with loops
# break, continue and pass

# __> We can use break, continue and pass statements in our loops to add additional functionality for various cases.
#    The three statements are defined by:

# break
#      \__> Break out of the current enclosing loop.

# An example of that is

# using break with a for loop
mystring = "Sammy"

for letter in mystring:
    if letter == "a":
        break
    print(letter)
#      \__> Ouput would be
# S
#           So instead of going back to the top of the current closest loop, it breaks out of the current loop,
#           which is why you are left with only S.

    # using break with a while loop
x = 0

while x < 5:

    if x == 2:
        break
    print(x)
    x += 1
#      \__> Your ouput will be
# 0
# 1
#           what is happening here is you saying if x ever equals 2 then break out of the while loop. which is why you
#           are left with only 0 and 1

    # continue
#      \__> Goes to the top of the closest enclosing loop.

    # An example of that is

mystring = "Sammy"

for letter in mystring:
    print(letter)
#      \__> output would be
# S
# a
# m
# m
# y

    # Lets say you didnt want the letter a, you could write it as follows
for letter in mystring:
    if letter == "a":
        continue
    print(letter)
#      \__> Here continue will go back to the closest enclosing loop. Basically what it is saying, if the letter
#           is 'a' go ahead and continue/slip, going back to the top of the loop and moving on to the next character or element.
# S
# m
# m
# y

    # pass
#      \__> Does nothing at all, its a placeholder like none is for a variable

    # An example of that is

z = [1, 2, 3]

for item in z:
    # not yet decided
    #      \__> If you decide you dont know what will be in the block of code here, and you only had a comment to the
    #           indentation, you will get an error.
    #           So you can use pass as a placeholder, so that you could continue
    #           to run your script and print end of script which is after this code.
    pass
#      \__> here we add pass in the block of code, and we can now run our script without issues.
print("the pass key word helped me to print this script")


print("\nUseful Operators in Python\n")
# useful Operators in Python
# a few built in functions that are important to know.

# the range function

mylist = [1, 2, 3]
#      \__> Notice that often we were creating lists that were just a series of intergers as 1 2 3.
#           Since this is such a common task, python has a built in operator for this called range(). There is 2 ways you can
#           use it, one is you can iterate through it. An example
for num in range(10):
    #            \__> take note that range has a start, stop and optional step size almost like slicing, but not with colons just commas.
    print(num)
#      \__> What this will do is its going to generate the numbers from 0 all the way to but not including
#           10, Which is very similair to the slicing syntax (stop) we saw earlier in the course.
#           Lets say you wanted to specify a starting postion then we would say in the following example.
for num in range(3, 10):
    print(num)
#      \__> Now when you run this you will start from 3 and go up to but not including 10.
#           In addition to all this, you can also add a step size as in the following example.
for num in range(0, 10, 2):
    print(num)
#      \__> Now it will skip every 2 numbers. and if you want to include 10 in your output you will need
#           to increase the stopping number to 11.
# __> So thats how you can use the range function for iteration. You will notice that if I copy and paste this as
#    in range(0, 10, 2)
print(range(0, 10, 2))
#      \__> Your output will just be this range operator for example range(0, 10, 2) and that is because its a
#           generator and if you actually want the list of numbers you will need to cast it to a list for example list(range(0, 10, 2)) as
#           an example
print(list(range(0, 10, 2)))

# __> later in the course we will discuss generators in a lot more detail, but basically
#    a generator is a special type of fuction that will generate information instead of saving it all to memory like a variable with a list
#    attached to it.
#    This is a more efficient way of generating these numbers instead of having a giant list stored in memory.

# the enumerate function
# If you want the index value of whatever iteration you going through, you can use enumerate.
# Enumerate, to list or count off individually.

index_count = 0

for letter in "abcde":
    print("At index {} the letter is {}".format(index_count, letter))
    index_count += 1
#      \__> So when we run this we get the information that at index 0 the letter is 'a' for example

# At index 0 the letter is a
# At index 1 the letter is b
# At index 2 the letter is c
# At index 3 the letter is d
# At index 4 the letter is e

#           Now this is such a common operation that what we are going to do is use the enumerate function to
#           replicate this output, and the reason it is so common, is a lot of the times you will want to have a
#           counter like this to see how many times you have gone through the for loop, or what index position you
#           are at.
index_count = 0

word = "abcdef"
#      \__> Lets define word as "abcdef"
for letter in word:

    print(word[index_count])
#      \__> So for every letter in word we end up printing the index value location of said word and thats the same
#           as printing the letter because we place an index value next to it.
    index_count += 1
#      \__> but in order to do this we need to have some sort of running index count this for every iteration it
#           adds + 1 index therefor printing the next letter in that index count as it goes up by 1 each iteration,
#           because this opration is really common in python, you have a function called enumerate function. lets have a look
word = "abcdef"

for item in enumerate(word):
    print(item)
#      \__> Notice the output is in tuples

# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')
# (5, 'f')
#      \__> So this is basically doing that index count for us automatically in the form of tuples, and as we know
#           we have tuple unpacking from the for loop lecture. for example you could do

word = "abcdef"

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print("\n")
#      \__> You output will be
# 0
# a

# 1
# b

# 2
# c

# 3
# d

# 4
# e

# 5
# f

# __> So this is the enumarate function and it can take in any iterable object and what it does is it returns back some sort
#    of index number/counter and then the object itself or the elements at that particular iteration.

    # the zip function
# Kind of almost like the opposite of the enumerate function and what it does is it zips together 2 lists, almost like a zipper,
# it pairs the lists together.

mylist1 = [1, 2, 3]
mylist2 = ["a", "b", "c"]
mylist3 = [100, 200, 300]

print(zip(mylist1, mylist2))
# <zip object at 0x000001D9C434CFC0>
#      \__> If I just run zip, you get back something telling that you have this zip generator waiting for you at
#           this location in your memory.
#           If you itereate through it, for example
for item in zip(mylist1, mylist2):
    print(item)
#      \__> The output of the
# (1, 'a')
# (2, 'b')
# (3, 'c')
#      \__> Notice that we get back this list of tuples, and this is why i said eariler that tuple unpacking will
#           come in handy as a lot of built in functions in python return back a list of tuples, this is this one
#           such function, the zip function just like a zipper on a jacket will zip together two lists together
#           whereby they pair up.
#           You can actually do this with more than just two lists
for item in zip(mylist1, mylist2, mylist3):
    print(item)
#      \__> The output wil be
# (1, 'a', 100)
# (2, 'b', 200)
# (3, 'c', 300)

# __> A common quesiton is what happens if the lists are uneven, lets have a look

mylist4 = [1, 2, 3, 4, 5, 6]
mylist5 = ["x", "y", "z"]
mylist6 = [100, 200, 300, 400, 500, 600, 700]

for item in zip(mylist4, mylist5, mylist6):
    print(item)
#      \__> You get back the same results even though some lists are longer than others and uneven, with zip
#           it will only go as far as the list which is the shortest. So it wont give an error, it will just
#           ignore everything that is extra.
# (1, 'x', 100)
# (2, 'y', 200)
# (3, 'z', 300)

# __> You see here that we iterated through the list, however if you just want the list itself you can cast to list

print(list(zip(mylist4, mylist5, mylist6)))
# [(1, 'x', 100), (2, 'y', 200), (3, 'z', 300)]


# __> You can unpack zips using tuple unpacking as follows

for a, b, c in zip(mylist4, mylist5, mylist6):
    print(a)
    print(b)
    print(c)
    print("\n")
# 1
# x
# 100


# 2
# y
# 200


# 3
# z
# 300

    # the in operator
# __> We have already seen the in key word of the for loop but we can use it to quickly check if an object
#    is in a list or string.

print("x" in [1, 2, 3])
#      \__> This will return the value False because x is not in the list, You could for example use it in a
#           list of letters, for example
print("x" in ["x", "y", "z"])
#      \__> This will return the value True because x is in the list.

# __> So this is a nice way to quickly check if something is in a list. The in key word also works on other
#    iterable object types, so it works on strings as well.
print("a" in "a world")
#      \__> The return is True because a was found in the said string, This also works on dictionaries as well,
#           for their keys
print("mykey" in {"mykey": "apples"})
#      \__> Will return True because mykey is in mykey. So if you want to check if its in items or values, you can type
#          it like so
d = {"mykey": "apples"}

print("apples" in d.values())
#      \__> This will return True as apples is in values
print("apples" in d.items())
#      \__> this will retun False, I dont know why, maybe because it returns a list of tuples.
print("apples" in d.keys())
#      \__> Notice that for values it is True, but the rest is False.

# min max Function

mylist7 = [10, 20, 30, 40, 50, 200]
#      \__> Imagine we wanted to know what was the minimum number in this list, there is a built in fuction you could pass,
#           there is a built in min function

print(min(mylist7))
#      \__> the result was 10, but if ever you want to find the max number then follow the example

print(max(mylist7))
#      \__> This giving the result of the maximum number in the list. Keep in mind to not use min and max
#           as variable names as they are already key words built into python. its also denoted by the fact that
#           its highlighted by the syntax highlighting.

# the random library
# __> Python comes with its built in random library and there is a ton of functions included in this library.
#    This is going to be our first example of importing a library.
#    So to import functions from a library we are going to say (from library import function) and the key words here being from and import.

# shuffle Function
# __> So now we have this shuffle function and what it does is it ramdomly shuffles around any sort of list. So lets create
#    another list and lets make it in order, but first lets import the random library and shuffle function from that library.

# from random import shuffle
#      \__> notice the words (from) and (import) and what its saying is (from) that "random" library thats built into Python
#           (import) the "shuffle" function.

myshufflelist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

shuffle(myshufflelist)

print(myshufflelist)
#      \__> Now your outcome shows a shuffled list, Note the shuffle(myshufflelist) does not actually return
#           anything as its an in place function, so typing something like

random_list = shuffle(myshufflelist)
print(random_list)
#      \__> you will get back a result of None, because there is nothing there, and if you check the type of that

print(type(random_list))
#      \__> You get back the <class 'NoneType'>.

# randint Function
# __> this is a nice function for grabbing a random interger

# from random import randint
#      \__> Here we have imported randint from the random library. so randint will
#           randomly pick a number between a lower range and upper range for example randint(0, 10) 0 being the lower range
#           and 10 being the upper range.

print(randint(0, 10))
#      \__> You will be getting random output between 0 and 10, in this case at the time of writing this i got 6,
#           however because this is returning something, I can save the function within a list and call it back later,
#           for example

random = randint(0, 10)
print(random)
#      \__> Note this does not save the number, it will continue to be random, so you can do this over and over.

# User input
# __> Lets look at how to accept user input, using the input function. input("Your message here ")

print(input("What is your name? "))
#      \__> Note we use the input("") function, notice the "" inside the input function, this is the text you want to show
#           when you ask the user for input. For example,

print(input("enter a number: "))
#      \__> Now the user can see what  to input, reason why I use a number here is to show the whatever the user inputs
#           in this field it will return as a string, and we can check this by saving it to a result,
#           which you would typically do when it comes to user input.
resultx = input("What is  your age? ")
#      \__> Now when you run this, you can pull that result later down the line in your code as it has saved
#           the input from the user.

print(f"The result is saved as {resultx}")
#      \__> Here you see the result is saved, and can be used at a later stage. However as mentioned before whatever
#           the user places into an input function, input will save that as a string it saves it as a string and not an interger,
#           so lets get the type to verify what type it is.

print(type(resultx))
#      \__> Here we can see it returning the result as <class 'str'>. So inorder to cast this or transform this into another
#           data type, what i need to do is cast float() on result or if you still want the int, then cast int() on the result
#           as follows

print("This is casting or transform the result to a float ", float(resultx))
print("This is casting or transform the result to a int ", int(resultx))
#      \__> Or waht you can do, is wrap the original input in a int() or floar() as this example shows

resulty = float(input("what is your age "))
#      \__> Here we wrapped the input field in a float
print("Here we can see the type for resulty", type(resulty))
#      \__> Here we can see the type for resulty <class 'float'>

resultz = int(input("what is your age "))
#      \__> Here we wrapped the input field in a int
print("Here we can see the type for resulty", type(resultz))
#      \__> Here we can see the type for resulty <class 'int'>

# __> keep in mind that whatever is input into a field will be considered and a string and the reason why you will
#    want to cast an input into a float or interger is maybe you will want to grab an index postiion so you
#    will most likey have to cast it.


print("\nList Comprehensions\n")
# List Comprehensions

# __> Essentially list comprehensions are a unique way of quickly creating a list with Python, You esentially
#    flattening a for loop.
#    If you find yourself using a for loop along with .append() to create a list, List comprehensions are a good alternative.
#    So lets imagine we have a sting called mystring and we say its "Hello"

mystringone = "Hello"
#      \__> Now you want to make a list for every character in this.

mylistone = []
#      \__> What you may do is start off with an empty list, and then say for letter in my string append letter
#           to my list, as an example

for letter in mystringone:
    mylistone.append(letter)
#      \__> If we check the result of this, you get back ['H', 'e', 'l', 'l', 'o']
print(mylistone)
#      \__> you get back ['H', 'e', 'l', 'l', 'o']

# __> So this is something thats really common for beginners to do, they create an
#    empty list and then iterate through some iterable and then they append whatever
#    this is or whatever element that is to their list.
#    There is actually a more efficient way to do this in python, and by efficent i
#    mean taking up less space in code as fas as the actual computation. its about the same,
#    so dont worry about saving computational time. if you find this method too confusing
#    then you can always go back to the for loop.

# __> So lets see how you can do the exact same thing on a single line.
#    what you do is you esentially break down the for loop into a list comprehension.
#    so first off all the for loop code will go inside the braces, you will remove the
#    second line and in place of that, add letter the very beginning, see example.

mystringtwo = "Vanya"

mylisttwo = [letter for letter in mystringtwo]
#      \__> Now when you run this, you get ['V', 'a', 'n', 'y', 'a']
print(mylisttwo)
#      \__> So whats actaully here, the logic is essentially a flattened
#           out foor loop because we're going to assume that the only action being taken in this
#           for loops is just appending whatever elements you want to your list.
#           Another example is,
#           essentially its the same as this mystring = "Vanya"
#                                            mylist = []
#
#                                            for letter in mystring:
#                                               mylist.append(letter)
#                                               print(mylist)

mylistthree = [x for x in "word"]

print(mylistthree)
#      \__> if i check out my list I get back ['w', 'o', 'r', 'd'], and just like a for loop "x" is a temporary
#           variable name that you can call whatever you want. So again its just element for element in and then
#           some sort of string, list or some other iterable object.

# __> So often what you going to see is something like this

mylistfour = [num for num in range(0, 11)]

print(mylistfour)
#      \__> so note my list are those actual numbers [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], so you have this
#           flattened out for loop. and you wondering is this all i can do? Its infact not all it can do,
#           you can begin to personize operations and the first variable name, for example if i wanted to grab
#           the square for every number in that range, what you can do is perform the operation seen below

mylistfive = [num ** 2 for num in range(0, 11)]

print(mylistfive)
#      \__> What you get back is the square for every number in that range [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
#           So what this is doing is essentailly flattening out the for loop
#           for letter in mystring:
#             mylist.append(letter ** 2)
#           thats what we doing when you say squared on the first variable. [num ** 2 for num in range(0, 11)]

# __> you can also add in statements into this, so lets say we only wanted grab the even numbers you can say

mylistsix = [x for x in range(0, 11) if x % 2 == 0]

print(mylistsix)
#      \__> Your output will be [0, 2, 4, 6, 8, 10], you and also do something like this

mylistseven = [x ** 2 for x in range(0, 11) if x % 2 == 0]

print(mylistseven)
#      \__> Now we get the even square numbers [0, 4, 16, 36, 64, 100]

# __> You can do more complex calculations in list comprehensions, for exmaple change celcius to fahrenheit an example of this is

celcius = [0,  10, 20,  34.5]

fahrenheit = [((9 / 5) * temp + 32) for temp in celcius]

print(fahrenheit)
#      \__> You result will be [32.0, 50.0, 68.0, 94.1]. This is exactly the same as doing the follow for loop

fahren = []


for temp in celcius:
    fahren.append(((9 / 5) * temp + 32))
print(fahren)
#      \__> you get back [32.0, 50.0, 68.0, 94.1], as an exercise see if you can build comparisons between the flattened version
#           and the normal or unflattened for loop

# __> are you able to do if else statements inside a list comprehension, yes you can but the order will be a little different.
#    before to continue this, readablitiy in your code is above all else, and should be the most important thing. Not try to do
#    slick one liners and list comprehensions can kind of fool you into thinking youre becoming a really good programmer, when
#    in fact your writing just kinf of really one liners that are really ugly and hard to read  when you come back a month later.
#
#    lets take a look at how this is done,

results = [x if x % 2 == 0 else "ODD" for x in range(0, 11)]
#      \__> This the complete revered order than before and can become confusing as it is the complete opposite order.
print(results)
#      \__> Your output will be [0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]

# Nested loop and a nested loop in comprehension
# __> Last note is to show, you can also do nested loops in the list comprehension, but before we look at that,
#    lets first look at a nested loop

mylist = []

for x in [2, 4, 6]:
    for y in [100, 200, 300]:
        mylist.append(x * y)

print(mylist)
#      \__> Your result is [200, 400, 600, 400, 800, 1200, 600, 1200, 1800], essentially what is happening here,
#           is taking 2 from x and multiplying it by each y numbers, and then repeating the same process for 4 and 6.
#           we can make it a little more obvious with the following example.

mylist = []

for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        mylist.append(x * y)

print(mylist)
#      \__> Your result will be [2, 20, 2000, 4, 40, 4000, 6, 60, 6000]
#           Note there is a way to do this with list comprehension and you going to sacrifice readability here

mylist = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(mylist)
#      \__> When you check the result you get back the same result as before, however readability is lowered.
#           [2, 20, 2000, 4, 40, 4000, 6, 60, 6000]
