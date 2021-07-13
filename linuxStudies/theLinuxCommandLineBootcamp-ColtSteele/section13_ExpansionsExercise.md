###### ____.section13_ExpansionsExercise

## Part 1
## Question 1

* Create the following 60 files using a single command with the powers of expansion!
    * morning-day-1 to 30
    * afternoon-day-1 to 30

<br>

#### Answer

> To achieve this we used the brace expansion **_{}_** as follows : **_touch section13_ExpansionsExercise/{Morning,Afternoon}-day-{1..30}_**

---

## Question 2

* For this next bit, you'll need to use the following command: date +"%m-%d-%y" <br>This command will print out the current date using the format month-day-year, like 09-19-21. Use this command to create a new file with the name todos-DATE.txt, where DATE is the output of the above date command. <br>For example, if we ran the command on September 19th 2021, the resulting file would be named todos-09-19-21.txt.  

<br>

#### Answer

> we performed command subsitution **_$()_** while creating a file with the **_touch_** command as follows : **_touch todos-$(date +%m-%d-%y).txt_**

---

## Part 2
## Question 1

* Using the files that we created in the previous section...
    * List out all the files that end with the number 9.
    * List out all the filenames where the second to last character is 1.
    * List out all the files that start with afternoon and then end with the number 7.
    * Make a new folder called Mornings, and move all the files that start with morning inside of it.

<br>

#### Answer

> **_ls *9_**

> **_ls *1?_**

> **_ls Afternoon*7_**

> **_mv Morning* Mornings/_**

---

## Part 3
## Question 1

* Using a SINGLE command (with expansion), create the following folder structure.  You will need to use the -p option with mkdir!
    
    * > **year/**
      > <br>__________ **Winter/**
      > <br>____________________ **Yard/**
      > <br>____________________ **House/**
      > <br>__________ **Spring/**
      > <br>____________________ **Yard/**
      > <br>____________________ **House/**
      > <br>__________ **Summer/**
      > <br>____________________ **Yard/**
      > <br>____________________ **House/**
      > <br>__________ **Fall/**
      > <br>____________________ **Yard/**
      > <br>____________________ **House/**  


<br>

#### Answer

> While using mkdir command with option -p for parent as well as the brace expansion **_{}_** method we could make multiple directories and sub directories as follows : **_mkdir -p year/{Winter,Spring,Summer,Fall}/{Yard,House}_**

#### Final folder and file structure

> section13_ExpansionsExercise/year/:
<br> Fall  Spring  Summer  Winter

> section13_ExpansionsExercise/year/Fall:
<br> House  Yard

> section13_ExpansionsExercise/year/Fall/House:

> section13_ExpansionsExercise/year/Fall/Yard:

> section13_ExpansionsExercise/year/Spring:
<br> House  Yard

> section13_ExpansionsExercise/year/Spring/House:

> section13_ExpansionsExercise/year/Spring/Yard:

> section13_ExpansionsExercise/year/Summer:
<br> House  Yard

> section13_ExpansionsExercise/year/Summer/House:

> section13_ExpansionsExercise/year/Summer/Yard:

> section13_ExpansionsExercise/year/Winter:
<br>House  Yard

> section13_ExpansionsExercise/year/Winter/House:

> section13_ExpansionsExercise/year/Winter/Yard:


---

## Question 2

* Finally, in each of the Yard/ and House/ Directories create a todos.txt file and a done.txt file. <br>Do this with a single line, without changing directories! Use expansion! The resulting folder/file structure should look like this:

    * > **year/**
      > <br>__________ **Winter/**
      > <br>____________________ **Yard/**
      > <br>______________________________ _todos.txt_
      > <br>______________________________ _done.txt_ 
      > <br>____________________ **House/**
      > <br>______________________________ _todos.txt_
      > <br>______________________________ _done.txt_   
      > <br>__________ **Spring/**
      > <br>____________________ **Yard/**
      > <br>______________________________ _todos.txt_
      > <br>______________________________ _done.txt_   
      > <br>____________________ **House/**
      > <br>______________________________ _todos.txt_
      > <br>______________________________ _done.txt_   
      > <br>__________ **Summer/**
      > <br>____________________ **Yard/**
      > <br>______________________________ _todos.txt_
      > <br>______________________________ _done.txt_   
      > <br>____________________ **House/**
      > <br>______________________________ _todos.txt_
      > <br>______________________________ _done.txt_   
      > <br>__________ **Fall/**
      > <br>____________________ **Yard/**
      > <br>______________________________ _todos.txt_
      > <br>______________________________ _done.txt_   
      > <br>____________________ **House/**
      > <br>______________________________ _todos.txt_
      > <br>______________________________ _done.txt_ 



<br>

#### Answer

> So it's important to note that you can input multiple files in directories which also include sub-nested directories with the brace expansion **_{}_** method as follows **_touch year/{Winter,Fall,Summer,Spring}/{Yard,House}/{todos.txt,done.txt}_**

#### Final folder and file structure layout

> section13_ExpansionsExercise/year/:
<br> Fall  Spring  Summer  Winter

> section13_ExpansionsExercise/year/Fall:
<br> House  Yard

> section13_ExpansionsExercise/year/Fall/House:
<br> done.txt  todos.txt

> section13_ExpansionsExercise/year/Fall/Yard:
<br> done.txt  todos.txt

> section13_ExpansionsExercise/year/Spring:
<br> House  Yard

> section13_ExpansionsExercise/year/Spring/House:
<br> done.txt  todos.txt

> section13_ExpansionsExercise/year/Spring/Yard:
<br> done.txt  todos.txt

> section13_ExpansionsExercise/year/Summer:
<br> House  Yard

> section13_ExpansionsExercise/year/Summer/House:
<br> done.txt  todos.txt

> section13_ExpansionsExercise/year/Summer/Yard:
<br> done.txt  todos.txt

> section13_ExpansionsExercise/year/Winter:
<br> House  Yard

> section13_ExpansionsExercise/year/Winter/House:
<br> done.txt  todos.txt

> section13_ExpansionsExercise/year/Winter/Yard:
<br> done.txt  todos.txt

---
