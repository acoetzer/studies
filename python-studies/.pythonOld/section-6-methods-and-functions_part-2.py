# My Python Notes
# Section 6 Part 2

# Methods and Functions

from random import shuffle
print("Interations between Python Functions")
# Interations between Python Functions

# __> Typically a python script or notebook contains several functions interacting with each other.
#    Lets create a carnival guessing game called Three Cup Monte to show how functions can interact with one another.
#
#    Basically Three Cup Monte is where you have 3 cups and underneath is a red ball, and they proceed to shuffle the cups and you need
#    to guess where the red ball is.

#    Our simple game wont actually show the caps or ball, instead we will simply mimic the effect with a Python list. It will also not show
#    the shuffle to the user, so the guess is completely random.

# __> Just a quick note to show how to shuffle a list in python, as python actually comes with a built in random module and the way you
#    import the shuffle function is like so

#         \____> this will essentially inport shuffle from the random library, and as an example lets see how and if it works

ex1 = [1, 2, 3, 4, 5]


shuffle(ex1)

# print(f"\nThis is just testing the shuffle library. My list before the shuffle was [1, 2, 3, 4, 5] and after {ex1}")
#         \____> So our shuffle works as we can see this particular output was [2, 3, 4, 1, 5]


    # Three Cup Monte
# __> The first step of this game is that we need to make our own version of the shuffle function, and reason for this is that the 
#     shuffle function as mentioned before is an inplace function and you cant actually return anything from the shuffle function.


def shuffle_list(mylist):
    """
    \__> Take note that our function will shuffle mylist as well as return our list. 
         Adding just a little functionality on top of the built in shuffle, since the built in shuffle wont return anything as it 
         does it in place, and we actually want to return it and use it as a result here.
    """
    shuffle(mylist)
    return mylist
#         \____> So we have a function that can shuffle this list and return the value each time.
#                So what is our actual game list going to look like?

# game_list = [" ", "O", " "]
#         \____> So our game list, is just going to be 3 strings, with 1 of them representing the ball with a capital O. So eventially what
#                we going to do is call shuffle list on my game list and then it will shuffle this around and the O may or may not be in
#                the same spot.
#                Next we need to create a function that can take in a players guess. So the player after the list is being shuffled is going
#                to guess the location. We wont display where the list is before we shuffle.


def player_guess():
    """
    \__> We created a function called player guess that takes in no parameters. 
         We have a plpaceholder variable guess with an empty string that will save the users input for later. 
         We then want, if for example the user inputs an incorrect answer, to continue to ask it for an input, by adding a while loop 
         saying, while guess is not in the is specific list or parameter defined by the not in keywords, go ahead and continue to ask 
         for input and once all that is done, it will go ahead an return guess as an interger.
         You will notice we wrapped guess in an int, as user input will always return a string, which is also why our while loop is 
         checking for a string version of 0, 1, 2.
    """
    guess = ""

    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0,1 or 2: ")

    return int(guess)

# __> So we just need one more function, which is to essentially combine this list which has been shuffled with the players guess. So I
#    just need to check if my guess was correct or not.


def check_guess(mylist, guess):
    """
    \__> This is where the functions start to interact together, because we will pass in the mylist and the users guess, so that means, 
         I should have called player guess and my shuffle list function before calling this check guess function and so what we going to do
         at the end of this is write a little script that essentially calls the functions in the correct order.
    """
    if mylist[guess] == "O":
        print("Correct!")
    else:
        print("Wrong Guess")
        print(mylist)
#         \____> Note in this case, I dont really care about returning anything becuase this will essentially be the last line in my little
#                script.
#                So we have our functions defined and now its time to ser up a little bit of logic as a final script.
#                So if you dealing with this in a .py file its very common to have definitions at the top and then at the bottom you have the actual
#                logic to be called here.


# INITIAL LIST
game_list = [" ", "O", " "]

# SHUFFLE LIST
shuff_list = shuffle_list(game_list)

# USER GUESS
guess = player_guess()

# CHECK GUESS
check_guess(shuff_list, guess)
