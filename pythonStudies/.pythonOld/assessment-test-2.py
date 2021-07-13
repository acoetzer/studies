# Assessment Test 2


print("ASSESSMENT TEST 2")

print("\n----------Question 1----------")
# Question 1
print("Use for, .split() and if to create a Statement that will print out words that start with 's' in the following\n(Print only the words that start with s in this sentence)")


# Code 1
st = "Print only the words that start with s in this sentence"

for word in st.split():
    if word[0] == "s":
        print(word)
#         \____> What we do here is we create a list out of the string using the .split() method. Take note of where we add the .split().
#                We then follow it up with control flow, saying that if  the index 0 of the word in the now newly created list is equal to 's',
#                return that word. What happens if the word begins with a upper case, well it wont print, but there are ways to still get the word,
#                as shown in the examples below.

st = "Sam Print only the words that start with s in this sentence"

for word in st.split():
    if word[0].lower() == "s":
        print(word)
#         \____> Here you get back the capital word 'Start' because you assigned a .lower() method to th index of that particular word.
#                Another method of doing this is.

for word in st.split():
    if word[0] == "s" or word[0] == "S":
        print(word)
#         \____> Here is another method and take not of the logical opertor "or", here you cannot use and because and states both
#              values need to be true, and a single s cannot be both upper and lower so you use the logical operator or, which states
#              that either or need to be true for it to be true, so either lower s or upper S.


print("\n----------Question 2----------")
# Question 2
print("Use range() to print all the even numbers from 0 to 10.")

for num in range(0, 11):
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd Number: {num}")
#         \____> So here we did a for loop, however you could have done it like so as well

print(list(range(0, 11, 2)))
#         \____> That would have given the output of [0, 2, 4, 6, 8, 10] or another way is

for num in range(0, 11, 2):
    print(num)


print("\n----------Question 3----------")
# Question 3
print("Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3")

mylist = [x for x in range(1, 51) if x % 3 == 0]

print(mylist)


print("\n----------Question 4----------")
# Question 4
print("Go through the string below and if the length of a word is even print 'Even' string is as follows\n(Print every word in this sentence that has an even number of letters)")

st = "Print every word in this sentence that has an even number of letters"

for word in st.split():
    if len(word) % 2 == 0:
        print(f"({word}) is EVEN, has {len(word)} letters")
    else:
        print(f"({word}) is ODD, has {len(word)} letters")


print("\n----------Question 5----------")
# Question 5
print("Write a program that prints the integers from 1 to 100. But for multiples of three print 'Fizz' instead of the number, and for the multiples of five print 'Buzz'. For numbers which are multiples of both three and five print 'FizzBuzz'")

for y in range(1, 101):
    if y % 3 == 0 and y % 5 == 0:
        print(f"{y} FizzBuzz")
    elif y % 3 == 0:
        print(f"{y} Fizz")
    elif y % 5 == 0:
        print(f"{y} Buzz")
    else:
        print(f"{y}")
#         \____> Take note, that we started to check for 3 and 5 before the others.
#                Reason for that is if 3 or 5 is first, it will print out those instead rather than both.
#                So keep that in mind.


print("\n----------Question 6----------")
# Question 6
print("Use List Comprehension to create a list of the first letters of every word in the string below:\n(Create a list of the first letters of every word in this string)")

st = "Create a list of the first letters of every word in this string"

mylist = [letter[0] for letter in st.split()]

print(mylist)
