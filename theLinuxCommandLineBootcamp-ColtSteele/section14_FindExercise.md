###### - section14_FindExercise

## Question 1

* Using find (and another command), count the number of case files that include "closed", in lowercase, in their name. You should find 980 cases.

<br>

#### Answer

* we used the **_find_** command in combination with option **_-name_** with the desired filename, we then piped it to the **_wc_** command with the option **_-l_** as follows : **_find linuxStudies/section14_FindExercise/Cases/ -name "*closed*" | wc -l_** 
    * Result was **_980_**

---

## Question 2

* Oh no, one of our new detectives labels his cases using "CLOSED" in all caps.  Find the 3 cases that have "CLOSED" in their name.

<br>

#### Answer

* We used the find command as follows : **_find linuxStudies/section14_FindExercise/Cases/ -name "*CLOSED*"_**
* The three files were :
    * case_1660_CLOSED.txt
    * case_2320_CLOSED.txt
    * case_2328_CLOSED.txt

---

## Question 3

* Get a total count of all closed cases that include "closed" in their name, uppercase or lowercase.   You should get a count of 983!

<br>

#### Answer

* we used the **_find_** command again with the option **_-iname_** for a case insentive search and the piped it to the **_wc_** command as follows :  **_find linuxStudies/section14_FindExercise/Cases/ -iname "*closed*" | wc -l_**
    * Result was **_983_**
---

## Question 4

* Get a count for the total number of open cases with odd numbered case numbers (find the open cases that have a 1,3,5,7, or 9 as the last digit in their case number).  You should get 519 cases.

<br>

#### Answer

* we used the **_find_** command in combination with **_-iname_** option, however looking at the structure of the filename we added a _set_ of odd numbers within brackets as in a range but this time as a set an example **_[13579]_** or **_[2468]_** before the word open and then piped it to the **_wc_** command as follows : **_find linuxStudies/section14_FindExercise/Cases/ -iname "*[13579]_open*" | wc -l_**
* Result was **_519_**

---

## Question 5

* Find the three empty cases

<br>

#### Answer

* we used the find command with the option -empty as follows : **_find linuxStudies/section14_FindExercise/Cases/ -empty_**
* The three files were :
    * case_2979_closed.txt
    * case_2900_open.txt
    * case_2950_open.txt
---

## Question 6

* Most of these files are quite small, but there are 3 pretty large case files.  Find the three files that are larger than 20k in size

<br>

#### Answer

* we used the find command this time with the option -type f to higlight only files and -size +20k as follows : **_find linuxStudies/section14_FindExercise/Cases/ -type f -size +20k_**
* The three files were :
    * case_1503_closed.txt
    * case_1995_open.txt
    * case_1647_open.txt

---

## Question 7

* Find the one case file that is larger than 150k and is closed

<br>

#### Answer

* we used the find command with a few options such as -type -size and -iname as follows : **_find linuxStudies/section14_FindExercise/Cases/ -type f -size +150k -iname "*closed*"_**
* The specified file found was :
    * case_1503_closed.txt

---

## Question 8

* No one has touched these case files in years, or at least no one should have touched these files, but sadly some corrupt detective recently tampered with one of the files. Sometime today he changed a single case from "closed" to "open" to spite an enemy of his.   Find the one case that has been modified more recently than the yesterday.txt file.  Watch the exercise intro video if you're confused!   You may need to read the man pages to find the correct command.

<br>

#### Answer

* for this we used the find command with a new option known as -newer with a reference as to what to compare it by as follows : **_find linuxStudies/section14_FindExercise/Cases/ -type f -newer linuxStudies/section14_FindExercise/Cases/yesterday.txt_**

---
