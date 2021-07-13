###### ____.section11_RedirectionExercise

## Question 1

* Create a new file called all-species.txt that contains the combined contents of angela-survey.txt, nico-survey.txt, and juan-survey.txt. 
    * Do this using a single command!

<br>


#### Answer

> We used the **_cat_** command while providing it a path as well as the **_*_** asterix symbol to select all files within the directory as follows : **_cat section11_RedirectionExercise/Wildlife/* > section11_RedirectionExercise/Wildlife/all-species.txt_**

---

## Question 2

* The problem with the all-species.txt file is that it contains duplicate entries! 
    * Use a single command to sort the lines in alphabetical order, only sorting uniques, and send the output to a new file called sorted-animals.txt

<br>


#### Answer

> Using the **_sort_** command with option **_-u_** for unique as follows : **_sort -u section11_RedirectionExercise/Wildlife/all-species.txt > section11_RedirectionExercise/Wildlife/sort-animals.txt_** 

---

## Question 3

* Now, you go out for a nice morning stroll and stumble upon a large anaconda sunning itself on a log. You should add this observation to the list of species!!
    * Start by appending the current date to the end of the sorted-animals.txt file using a command (don't open the file manually!)
    * Then append the text "Green Anaconda" to the end of sorted-animals.txt

<br>


#### Answer

> Firstly we used the **_date_** command and appended it **_>>_** to the sorted list as follows : **_date >> sorted-animals.txt_**

> secondly we the used the **_echo_** command to append the text Green Anaconda to file as well as follows : **_echo Green Anaconda >> sorted-animals.txt_**

---

## Question 4

* Run the non-existent command ughhh and redirect any error messages so that they are appended to the sorted-animals.txt file.

<br>


#### Answer

> We used the standard error and redirected it to the file as follows : **_ughhh 2>> sort-animals.txt _**

---
