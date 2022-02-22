###### - section5_NavigationExercise

## Question 1, 2

* Open a new terminal window. Navigate to the Farm folder.
* List the contents of the Farm directory.

<br>

#### Answer

> cd Downloads/theLinuxCommandLineBootcamp_Exercises/section5_FarmExercise/Farm/

> To make sure that we are in the farm directory, we can use the **_pwd_** command to print the current working directory. <br> Which is : **_/home/z1600k1/Downloads/theLinuxCommandLineBootcamp_Exercises/section5_FarmExercise/Farm_** <br> If we run the **_ls_** command we see two folders : **_Coop  Stable_**

---

## Question 3, 4

* "Move" into the Coop folder.
* List the contents of the Coop folder.

<br>

#### Answer

> To move into the Coop folder we use the **_cd_** command as follows : **_cd Coop/_**

> When we run the **_ls_** command we see two folders : **_Chickens  Geese_**

---

## Question 5, 6, 7

* "Move" into the Chickens folder.
* List out the chickens in the Chickens folder.  How many are there?
* One of the chickens is very very old, which one is it? (which file in the Chickens folder has the oldest modification time?) Use a command to figure it out!

<br>

#### Answer

> We use the **_cd_** command to move into the Chickens folder as follows : **_cd Chickens/_**

> If we run the **_ls_** command, we see these chickens(files) listed as so : **_Buckbeak  Elvis  Ethel  Frida  Hippo  Jaba_** <br> There are six chickens(files)

> We used a option within the **_ls_** command known as **_--sort=time_** which will list the newest modification time first. In this case we see that by running **_ls -la --sort=time_** that **_Elvis_** is the oldest chicken(file) with its modification time being **_Jan 1 1980_**

---

## Question 8, 9, 10

* In a single command, move from the Chickens directory to the Geese directory.  Consult the folder structure written out above if needed.
* How many geese (files) are in the Geese directory?
* One of the geese is sitting on a golden egg!  It's larger than the other geese. Which one is it?  (which file in the Geese folder is the largest?).  Use a command to figure it out!

<br>

#### Answer

> With a single as so : **_cd ../Geese/_** we can move from the Chickens folder to the Geese folder.

> If we run the **_ls_** command, we can see 4 geese(files) listed within the folder.

> If we run the **_ls -lah --sort=size_**, hence we added the --human-readable option, we see that **_Muffin_** has the golden egg with a file size of **_15_**.

---

## Question 11, 12, 13

* Navigate to the Horses directory.  Consult the folder structure written out above, if needed.
* How many horses are in the Horses directory?
* Wait! There is a hidden horse in the Horses directory! What is it's name??

<br>

#### Answer

> When moving from the current directory : **_/home/z1600k1/Downloads/theLinuxCommandLineBootcamp_Exercises/section5_FarmExercise/Farm/Coop/Geese_**, we use the command **_cd ../../Stable/Horses/_** to move in one line to the horses directory.

> When running the **_ls_** command we see that there are 4 horses(files) in the folder : Archer  Buttons  Cookie  Jett

> We used the **_ls -la_** command to see the hidden horse(file) and its name is : **_.Troy_**

---

## Bonus Exercise 

* List out the contents of the Horses directory as a comma separated list.  You'll need to dig into the man pages to find the correct option.  Perhaps search the ls man page for "comma"?

<br>

#### Answer

> First when we **_man ls_** we search the man page by pressing **_/_** and then entering the word comma and we came up with the result of using the option -m.

> So when running **_ls -am_** we see all files seperated by a comma as follows : **_., .., Archer, Buttons, Cookie, Jett, .Troy_**

