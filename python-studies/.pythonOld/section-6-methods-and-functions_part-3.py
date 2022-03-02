#  My Python Notes
# Section 6 Part 3

print("*args and **kwargs")
# (*args) and (**kwargs)

#__> args and kwargs stand for arguments and key word arguments., they are denoted by the astrix symbol. 
#     \__> (*args) one for args
#          (**kwargs) for kwargs
#  
#    They allow you to place a infinite or arbitrary amount of parameters in a function call, without having to 
#    predefine a set of parameters before hand.  
#    Lets look at some examples.

#__> predefining some parameters before hand.

def myfunc(a, b, c = 0, d = 0, e = 0):
    # Returning the sum of the arugments
    return sum((a, b, c, d, e)) * 0.05
#         \____> So what is actually happening here is that we have a function that has multiple predefined 
#                parameters and things to take note here are. 
#                
#                1. The prefedined parameters have a default value equal to 0. 
#                    \__> Note that if this is not done, python will expect all those parameters to be filled, 
#                         and you can see a lot of issues arising from something like this. 
#                2. If a user only wants 2 arguments and default values were not inserted it would 
#                   throw out an error.
#                3. The user might input more parameters than is currently available. 

x = myfunc(10, 20, 30)
print(x)

print(myfunc(10, 20, 30))
#         \____> Some side notes to mention here is. 
#                
#                1. a, b ,c ... are what is known as positional arugments, which means that 10 is a, 20 is b, 
#                   30 is c and so forth. 
#                2. Another note to take in is the difference between first returning the function to a variable 
#                   and then printing it and just print the function directly. 
#                   When should you do this, and that is when you only going to use the function once in your code.


#__> What if we want to work with more arguments without predefining a set amount of parameters? 
#    This is where we can use (*args) and (**kwargs) for this very purpose. 
#    Lets see an example of that.

# Function while use args and kwargs

def myfunc(*args):
    print(args) # To see what args looks like.
    return sum(args) * 0.05
#         \____> One thing to take note here is you can treat args as though its passing in a tuple of parameters.
#                
#                Side note, you dont need to repeat the astrix symbol within the block of code, just the name 
#                assigned to it, which by the way can be anything you want it to be.

print(myfunc(10, 20, 30, 40, 50, 60, 70))


#__> We looked at how to add an arbitrary amount of arguments to a function with (*args) parameter. 
#    Python also allows for an artibrary amount of key word arguments. 
#    The difference between the two is you can think of (*args) as tuples coming in and (**kwargs) as a dictionary.

  