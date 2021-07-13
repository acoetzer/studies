###### ____.section4_GettingHelpExercise

## Question 1.

* There is a command called whoami. Before you run it, read the manual page entry on it. 
* From the manual page entry, can you tell if it needs any options or arguments? What does it do?

<br>

#### Answer

* **Print the user name associated with the current effective user ID**, basically prints the username of the currently logged in user.

---

## Question 2.

* Now try running it! What happens?

<br>

#### Answer

* It prints my current username **z1600k1**

---

## Question 3.

* There is another command called who.  Without turning to Google, figure out what it does! Does it require any arguments or options to run?

<br>

#### Answer

* The **who** command prints information about users who are currently logged in, it does not require any options or arguments to run as they are optional denoted by the "[ brackets ]" in the man pages.

---

## Question 4.

* Use the who command to print out the time of the most recent system boot.  You'll need to find an option to help you do this!

<br>

#### Answer

* **[-b, --boot]** is used to print the time of the last system boot.

* When running the command, this is the result : **_system boot  2021-06-10 10:15_**

---

## Question 5.

* Run a command to figure out whether the echo command is a a binary, a shell-built in, or an alias.

* Do the same for  the date command

<br>

#### Answer

* To accomplish this we will use the **_type_** command for example **_type echo_** and the result is : **_echo is a shell builtin_**

* Its the same for for the **_date_** command, answer is : **_date is /usr/bin/date_**