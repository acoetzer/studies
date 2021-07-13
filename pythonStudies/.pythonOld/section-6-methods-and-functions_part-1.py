# My Python Notes
# Section 6 Part 1

# Methods and Functions

print("Methods and the Python Documentation")
# Methods and the Python Documentation

# How to find methods.

# __> We have already seen a few methods examples of methods, such as .append(), .sort() and .count() etc.. when learning about object
#    and data structure types in python.
#    Methods are essentialy functions that are built into objects and later on in the course we will learn how to create our own objects
#    and methods using object oriented programming in classes. However for now, I want to explore in more detail how to find methods and
#    understand more information about them.

#    In our case we are using Visual Studio Code, and we added an extension called pylance that essentially auto completes code, but we
#    can use that to see the various methods for a particular object.

#    Pylance should automatically appear when typing code however you can use the keys (ctr space) to activate the drop down if it doesnt.
#    Another method for you to find information about topics is to go to https://docs.python.org/3/

# Introduction to Functions

# __> Creating clean and repeatable code is a key part of becoming a programmer and functions in python allow us to create blocks of code
#    that can be easily executed many times without need to constantly rewrite the entire block of code. Currently, if we wanted to have
#    a piece of code run twice or call it mulitple times, we would have to copy and paste all the lines in that particular block of code
#    and then call it again. So we would have to rewrite that code.
#    Functions will essentially allow us to do this all within one line. Functions will be a huge leap forward in your capabilities as a
#    Python programmer, this means problems you are able to solve can also be a lot harder.


print("The def Keyword")
# The def Keyword

# __> def essentially allows us to make a function in python. Creating a function in Python requires a very specific syntax, including the
#    aforementioned def keyword, correct indentation, and proper structure.

# def syntax example


def name_of_function(name):
    """
    \__> So heres the first line of an example fuction, and it all starts with the (def) keyword, which essentially stands for the 
         definition of the function and this key word tells Python that hey!, what I am about to write is a function.

         The (name_of_function) which by the way you can decide what is the name, though take notice of the snake casing whereby there 
         is no spaces and only underscores, take note that the name is also in lower case letters. In general, by convention, Python 
         uses snake casing for the name of the function and this is by convention, so that when looking at someone else's code that you 
         can tell what is a function.

         Later on when we talk about OOP, class calls and the use of camel casing.

         You will notice that we have parenthesis here (), and parenthesis come at the end of the funtion. Later on we will see how we can
         pass on arguments or parameters into the function where arguments or parameters are essentially just words saying take this 
         variable and pass it into the function in order to work with it within the function.

         Finally you will notice a colon (:), which indicates an upcoming indented block, everything that will be indented is essentialy 
         inside the function.

         After all that, if you noticed we used triple quotation marks or multi line string, known as Docstring to make notes inside 
         this function. What it is essentially used for is to explain the function such as a comment, but in our case we used it as an example 
         to explain the def function.
    """
    print("Hello " + name)
#         \____> and then you going to write the code you want to run everytime you call this function. For now its a very simple code
#                that will print Hello (user) when you call the function.


name_of_function("Jack")
#       \ \____> Now functions can begin to get more complex, such as actually accepting a parameter or argument such as name, take note,
#        \       that the name variable, which could be any name, is placed inside the code, where we have concantenated it with Hello,
#         \      and also placed it inside the parenthesis. When we call our function, we directly input the string Jack within the
#          \     parenthesis. What you can do is use this as an argument to be passed by the user for example using the input() function.
#           \
#            \_> Take note that we didnt use a print() function to call or print this function, because print was already inside that
#                function, all we need to do was call the function.
#
#                Functions can accept arguments to be passed by the user. Here I have my function and it accepts this paramenter (name)
#                and what is going to do is say, print Hello plus name, so that essentially means that name should be a string and you going
#                to concantenate it with the string Hello.
#                So when you call your function as you did here, it says name_of_function("Jack"), the output will be Hello Jack.

# __> Typically we use the return keyword to send back the result of the function, instead of just printing it out. If we look back at the
#    example, we basically just had print inside that function, in general you rarely just going to have a print inside of a function
#    because you might as well just call the print function.
#    Instead, youre going to use what is known as the return keyword and return allows us to assign the output of the function to a new
#    variable. We will have a much deeper understanding of the return keyword later in the course. Just keep in mind a really common
#    question is what is the difference between return and print inside a function. We will clarify that as we go through some examples
#    but for now, lets look at very simple exmaple of return.


def add_function(num1, num2):
    """
    \__> We created a function called add_function, and it took 2 arguments or parameters which is num1 and num2. Keep in mind you can call 
         these variables whatever you like. So its very flexible in the naming scheme.
    """
    return num1 + num2
#         \____> and then its going to return the result of num1 and num2 when assigned to a variable. You should also notice here that
#                return doesnt have any parenthesis attached to it, unlike the print() function.
#                So return then allows you to save the result to a variable which print does not.


result = add_function(1, 2)
#         \____> So that means, when i call add_function(1, 2), I'm saying num1 is 1 and num2 is 2, and so what its going to do inside of the
#                function is 1 plus 2 or essentailly num1 + num2.
#                Which will return 3, and because we used return, we can now save that result to a variable for example "result" which
#                is equal to whatever add function (1, 2) will return to me.
print(result)
#         \____> So in that case if I were to later on print the result, or use it somewhere else in my code, it will return the number 3.

# __> So most functions as mentioned will use return. rarely will a function only print.


print("Basics of Python Functions")
# Basics of Python Function

# Some Examples


def say_hello():
    print("Hello Basics of Python")
#         \____> Notice that when we start, syntax highlighting works for the def keyword. we then decide on the name of our function.
#                Notice that after the parenthesis and colon, an indentation will occur letting us know that we are inside that block
#                of code and anything inside this black of code will execute when calling the function. Example we have print hello,
#                and if we run the function like below


say_hello()
#         \____> It will execute the block of code and do whatever its suppose to do, in this case it is going to print "Hello ...",
#                take note that we did not use the print function as the funtion itself has the print function inside it. If we have
#                more complex code like for example multiple print statements inside the function, you only need to use 1 line of code
#                to essentially print out the other lines, as the example below.


def say_goodbye():
    print("I")
    print("am")
    print("saying")
    print("Goodbye!")
#         \____> Notice that when we call the function, all the the print statesments will print out.


say_goodbye()

# __> Take note that when we called both functions, we used parenthesis at the end, just like the print function. If we didnt use or add
#    the parenthesis, Python will not execute the function instead Python will tell you that say_hello or say_goodbye is just a function.
#    So inorder to execute the function you need to add on the parenthesis.
#    The main point of a function is to execute the block of code, especially when you plan on repeating that block of code.

# __> Realistically speaking, we're probably going to take some input parameters or input arguments into our function for example name.
#    Lets overwrite the previous function.


def say_hello(name):
    """
    \__> We have inserted a Parameter called "name" and then its going to print out Hello + "any name".
    """
    print(f"Hello {name}")
#         \____> Take note here the we placed the name parameter inside the f"string literal insidde the code. So whenever we call this
#                fucntion and input a argument, it will then include that into its output where we add name in in the fstring literal.


say_hello("Bob")
#         \____> So if we pass in the string "Bob" it will print out, Hello Bob. Take note that the variable within the paranthesis, can
#                be named whatever you want, however inside the function would have to match up as well, even though you can name it
#                anything you want, typically what you should be doing to providing names that fit with what it will be used for, same goes
#                for the function name.

# say_hello()
#         \____> lets imagine now that we didnt add an argument inside the parenthesis and kept the parenthesis empty.
#                Python would then give you an error, saying the function is missing 1 required positional argument. So essentailly
#                telling you, hey we need to know what "name" is, inorder to execute this block of code.
#
#                So how can we fix this?
#                Well 1 way is to just input the missing value or the other way is we could provide a default value by adding an "=" sign
#                like so


def say_hello(name="Default"):
    print(f"Hello {name}")


say_hello()
#         \____> Here you can see the default value has executed and it prints out Hello Defualt when we leave the parenthesis blank.


# __> So as mentioned before when it comes to a function call we not typically going to be using the print function, instead we going to
#    be use the return keyword.
#    Lets look at an example of this

def add_num(num1, num2):
    """ 
    \__> One of the most common questions is what is the difference between a print statement and a return statement? 1 is that a 
         print statement cannot be assigned to a variable whereas the return statement can.
         So the main difference, is return, instead of just printing out the results, will actually allow you save them as a variable.
         Basically return, allows you to save the output of a function to a variable.
    """
    return num1 + num2


result = add_num(10, 20)
#         \____> Notice because we using return, we are able to assign it to a variable called result.

print(result)
#         \____> Then later in my code, I can call result and it will give me the output or result of the variable. Lets actually see
#                this between the 2 functions


def print_result(a, b):
    print(a + b)


def return_result(a, b):
    return a + b

#         \____> Take note of the parenthesis, that for return you dont need to use parenthesis.
#                Here we can actually see the difference between the 2 statements.
#                Lets start off by running the print result function.


print_result(50, 50)
#         \____> This is essentially just printing out the result, if you had to assign this to variable, for example test, and you check
#                the type of that variable, you will notice the return as None type.

test = print_result(50, 50)
#         \____> technically this still prints the result but its not returning anything, but as you see below, the class type for variable
#                test, is a none type.

print(type(test))
#         \____> <class 'NoneType'>


# __> Lets to imagine you want to save the result of the function, you would want to use the return statement.

result = return_result(100, 100)

print(result)
#         \____> Here you can see the output, and when checking the type you see the class type int, confirming this is infact assigned to a
#                variable.

print(type(result))
#         \____> Here you get back <class 'int'>

# __> Now that doesnt mean you cannot use print and return together, if for some reason, and keep in mind its not super common to do this,
#    that you want to see both the printed result and be able to return it then you could do something like this.


def myfunc(a, b):
    """
    You can go ahead and print the result to inform the user as well as save the output to a variable
    """
    print(a + b)
    return a + b
#         \____> Again this is not super common to do this, however when you debugging as a beginner, this can be useful to see as you go along
#                what the output will be, almost like the best of both worlds, so you can see whats going on internally.

# __> Take note that we have just been saying a + b in the functon, though we havent really check what the data types were.


def sum_numbers(num1, num2):
    return num1 + num2
#         \____> Nowhere are we checking to see if these are numbers,  and that is because Python is dynamically typed, whereas other languages
#                are statically typed meaning you have to make sure and define the data type of a variable before you call a variable.
#
#                Python however is dynamically typed, which means you dont need to specify before hand what data type you expect num1 and num2 to
#                be. That allows you to code much faster, but it also leaves you open to possible bugs, for example making sure you using the
#                correct data type, lets take a look at an example


ex1 = sum_numbers(1, 2)

print(ex1)
#         \____> Notice here you you have intergers and will output the answer 3, whereas below

ex2 = sum_numbers("1", "2")

print(ex2)
#         \____> You have strings and the output will be 12, both will add together in python, exept the values and data types will be incorrect.
#
#                So when taking user input, remember that the input function, turns everything to a string, so if you making a function that will
#                require user input, be sure to check what type of data it is before returning a result.
#                1 way could be to wrap the input in an int or float, essentailly converting it.
#                later on we can see various ways to address this issue.


print("Logic with Python Functions")
# Logic with Python Functions

# Using logic inside a function

# __>  Lets take a look back at the mod function, %

ex1 = 2 % 2
#         \____> The result will essentially be 0 as there are no remainders.
#                If we were to say 3 % 2 as below

ex2 = 3 % 2
#         \____> The result would equal to 1, as 2 goes into 3 once with a remainder of 1.

# __> So how can we use this to check if a number is even. Well, with a number say for example 20 % 2 should be equal to 0 when essentailly means
#    its even. So we could check this with an example below.

ex3 = 20 % 2 == 0
#         \____> This now should return the boolean value True because it has no remainder.

ex4 = 21 % 2 == 0
#         \____> whereas this returns the booleans value of False because its has a remainder of 1.

# __> So lets construct this into a function so that we can place any number and get the result without having to retype the code over and over again.


def even_check(number):
    result = number % 2 == 0
    return result


print(even_check(20))
#         \____> This should return True.

print(even_check(21))
#         \____> This should return False.

# __> Now for beginners its really common to separate things out into multiple lines like the function above, however you dont need to save result
#    as a parameter, you can just directly return the fucntion like the example below.


def even_check(number):
    return number % 2 == 0


print(even_check(20))
#         \____> And this still gives you the same output, which is True.

# __> We have seen that we can check if a number is even or not.
#    So lets go ahead and check inside a list.

# This new function will
# RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST
# Again, there just needs to be a single number inside of a list and the list can be as long as you want.


def check_even_list(num_list):

    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
#         \____>


print(check_even_list([1, 3, 5, 7, 9]))
#         \____> It returns the value None as there are no even numbers
print(check_even_list([2, 4, 6, 8, 10]))
#         \____> it returns True, as there is an even number, we can go ahead an check other examples to make sure it works.
print(check_even_list([2, 1, 1, 3, 5]))
#         \____> Here the first number is even and it should return True.
print(check_even_list([3, 1, 1, 3, 4]))
#         \____> Here the last number is even and should also return True.

# __> Essentially what this function is doing is looping through each of the numbers until it finds an even value. and then it just breaks
#    out of the function and returns True.
#    Infact, you can think of this return statement as essentially going to break off the entire function and the end the function. So once
#    you call return thats it, the function is over.

# __> Our fucntion doesnt return anything, if there is no even number in the list.
#    lets say we actually wanted to return false. How can we fix the function above. A super common mistake a beginner would make is to
#    change else statement to return false, example below.


def check_even_list(num_list):

    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            return False  # WRONG!!!

#         \____> This is wrong, why is it wrong?, as we mentioned, you can think of return as essentially breaking out of this function.
#                So why is wrong to put return False here, when it was correct to put return True, so often beginners make the same mistake
#                thinking all returns should have the same level of indentation.
#                However thats actaully not true, because look what will happen here.


#                Were going to say for number in num_list, and then the very first time that a number is not even, its going to just return
#                False.
#                Essentially saying that this if else statement is only going to be able to check one number because both conditions will
#                immediately return something.
#                If we were to run this.
print(check_even_list([1, 3, 5]))
#         \____> It will return False, however lets add an even number in the middle and see what happens
print(check_even_list([1, 2, 5]))
#         \____> It again returns False, where it should return True, but noitce it returns false because its essentially only checking the
#                first number since there are a return call on either condition that the first number has. So that mean the else return should
#                actually not be there. Well where should it be? Well I want to make sure i have already checked every single number and whether
#                or not its even by the time I return False.


def check_even_list(num_list):

    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False
    #         \____> So the return False should actually be an indentation with the for loop here. So lets go ahead and run this.


print(check_even_list([1, 2, 5]))
#         \____> Notice that this not returns True, the its gone through the for loop first, even though 1 was an odd number in the
#                beginning, it essestially passed. If we change the numbers to all odd numbers, lets see our result

print(check_even_list([1, 3, 5]))
#         \____> It now returns False.

# __> Again its a super common mistake that beginners make is that think think all returns need to be indented together, when they dont
#    need to be. However its important to understand the logic of whats happening here,
#    We want to loop through all the numbers first, and we can use these pass statements as placeholders to essentially say dont do anything.
#    That will be very useful when you have a functionthat needs or requires multiple return statements. Lets to expand the complexity of this
#    function and return all the even numbers in the list, instead of just saying True or False.


def check_even_list(num_list):
    # Return the even numbers, and if there are no even numbers to just go ahead and return an empty list.

    # Placeholder
    even_number = []

    for number in num_list:
        if number % 2 == 0:
            even_number.append(number)
        else:
            pass
    return even_number
#         \____> taking a look at the placeholder comment inside the function. It is very common that at the top of a function call if you
#                intend to return something and you dont have it defined as an argument inside the parenthesis, to define it on top of your
#                function call, in this case even_number = [].
#                So often you will have placeholder variables at the top of the function.
#                So here, even numbers is essentially a place holder for what I eventually will return, so when it does return the even numbers,
#                it will return it as a list and then whereas num_list in the parenthesis, is the input argument.

#                Lets go ahead and look at the logic behind this function, you have a paceholder variable that will beused to return an even
#                list of number, so you created a for loop to iterate through the numbers and if those numbers are divisable by 2 and are equal
#                to 0, then go ahead and append those numbers to the even numbers list. else if number are uneven, then pass. then lastly you
#                want to return the variable even number.
#                Take note the Return is lined up with the for loop, you essentially want to go through the entire for loop, before you run the
#                return function.


print(check_even_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#         \____> You get a return as follows [2, 4, 6, 8, 10]

# __> As an experiment lets to change the the even number to a empty string and see what it returns.


# def check_even_string(num_string):

#    even_string = ""

#    for number in num_string:
#        if number % 2 == 0:
#           even_string.append(number)

#        else:
#            pass
#    return even_string

#print(check_even_string([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#         \____> This is not going to work, as python will tell you the string, does not have an attribute .append.

# __> for the sake of learning and experimenting.
#    lets make a function that will print out all the letters of LlamaCoda, however lets make it more complex that when
#    it gets to letter c it will just skip and continue printing the rest of the word as well as you not allowed to use the print function
#    within your function.

def my_word(word):

    our_name = ""

    for letter in word:
        if letter == "c" or letter == "C":
            continue
        else:
            our_name += letter

    return our_name


my_example = my_word(input("Enter what you want here "))

print(f"Haha, we removed all the c letters in your words {my_example}")
#         \____> For added messure we also input the user input function.
#
#                However lets to understand the logic behind what we did.
#                We created a function whereby we did not want to add a print statement and only use return, we know now that strings
#                cannot accept the .append methods like a list, also we did not want the output to be in list form, but as a string.
#
#                So we made a temporary varaible named our_name within the function and assigned an empty string to it.
#                We then created a for loop to iterate through the users input represented by the word parameter and when it reached the
#                letter c, it would essentially skip/continue that letter and continue to loop through the rest of the input concantenating
#                it to the empty string variable.
#
#                However because we could not append the letters to a string we decided to concantenate it to the string variable as it
#                loops through each letter or character within the word parameter and when it find the condition its looking for, it will
#                essentially skip or continue past it and then continue to execute the else statement.
#
#                Once it has gone through the entire loop, it will then return the temporary variable our_name and we can then assign that
#                to a varaible and call it later in our code.

#                Most important thing here to remember is that the return statement is outside of the for loop, as well as once the return
#                statement has executed, the function is over and wont continue to run. The other important thing to remember is that you
#                can essentailly have a temporary variable at the top of the function.

#                Take note that if we placed the return inside the for loop, that after the first iteration, the function would end, because
#                as we mentioned before once you execute the return statement, the function is over. So in this case if you were to place
#                return inside the function you would be left with only the letter "L". So you would want to make sure that you are able to go
#                through your entire for loop before executing a return.


print("Functions and Tuple Unpacking")
# Functions and Tuple Unpacking
# How we going to return multiple items from a function with tuple unpacking.

# __> Recal that we previously seen that we can loop through a list of tuples and unpack the values within them. As an example lets creates a
#    list of tuples

stock_prices = [("GOOG", 200), ("APPL", 400), ("MSFT", 800)]

for item in stock_prices:
    print(item)
#         \____> This will return a list of tuples

# ('GOOG', 200)
# ('APPL', 400)
# ('MSFT', 800)

# __> We also know we can do tuple unpacking. Which means I can actually individually grab the items from these tuples.

for ticker, price in stock_prices:
    print(ticker)
#         \____> Here as we run this, its unpacked just the ticker values as seen below, so you can do different things like below.

# GOOG
# APPL
# MSFT

for ticker, price in stock_prices:
    print(price + (0.1 * price))
#         \____> Imagine you wanted to see what a 10% increase on the stock price would look like. Your output would be as follows.

# 220.0
# 440.0
# 880.0

# __> That is tuple unpacking, now we have seen how we can do this with a for loop, but we can also do it with a function. So a function
#    can actually return things as tuples and then we can unpack the result from the function.
#    Lets create a more complicated example here by making a list of tuples called work hours that holds the employee's name as well as
#    their work hours they worked for that particular month.

work_hours = [("Micheal", 100), ("Pam", 4000), ("Dwight", 2000)]
#         \____> So we have their work hours and now we want to do is see who will be the employee of the month or the employee of the
#                year and the way it will be judged will be the employee that has worked the most hours.
#                We also want to return not only the employee name but also the amount of hours they have worked.
#                So we need a function that can actually then go through these tuples and then see the name and the corresponding hours
#                and keep track of the name that has the most hours.

# __> So lets create a fcntion called employee check and it will accept work_hours as its parameter.


def employee_check(work_hours):
    """ 
    As mentioned before, typically we going to have place holder variables when it comes to logic at the very top of the fuction.

    """
    current_max = 0
    employee_of_month = ""

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    # In the end we intend to return a tuple, that says, employee of the month and the max hours they have worked.
    return (employee_of_month, current_max)

#         \____> Why do we have current max below equal to 0, and what is it going to do?
#                Well, what current max is going to do is start off at 0 and then its going to compare each employees hours to the
#                current max hours in the tuple list.
#                If they beat the curent max hours, then It will reset the current max to their value and It will reset the employee of
#                the month to there name.
#
#                So we have to do a for loop to can see this and some tuple unpacking.
#                So we created a tuple unpacking structure, employee and hours for the tuple list work_hours.
#                We then gave some logic underneath saying that if hours, is greater than the current max variable,
#                then reset current max to be equal to those hours and employee of month variable to be equal to that particular employee
#                or string.
#                And the else, pass so that the for loop will run through the entire list before executing a return.

#                So essentially whats happening here, is the for loop is going through the list, and as it comes across its first tuple pair,
#                it will set that as the max to beat, it will then loop back and check the next tuple pair and if that beats the current max,
#                it will then reset the value of current max to that and continue on with the list until it reaches the end, if it comes a
#                across a tuple pair that doesnt beat the current max, it will just pass as we gave the else statement the command to do
#                nothing else.


result = employee_check(work_hours)

print(result)
#         \____> We can see that it has taken the highest value of worked hours and given the result in a form of a tuple, even though pam
#                was in the middle it kept her standing as Dwight could not beat her current max.

# ('Pam', 4000)

name, hours = employee_check(work_hours)
#         \____> So just like the for loop, where we said ticker, price, we can unpack the return of a function in a similair fashion if a
#                function returns back a tuple.

print(name)
print(hours)
#         \____> So now we can perform tuple unpacking with a function call.

# Pam
# 4000
