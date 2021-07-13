###### ____.section8_DeletingCopyingandMovingExercise

## Question 1 -- 8

* Before we can delete, move, or copy things...we need things! It's time to get some more practice using touch and mkdir
    * Please create a new directory somewhere on your machine called Bootcamp.  Inside of it, create the the folders and files indicated below:
        
        * > **Bootcamp/**
          > <br> __________ **FallCohort/**
          > <br> ____________________ _Italo.txt_
          > <br> ____________________ _Edgar.txt_
          > <br> ____________________ _Linus.txt_
          > <br> ____________________ _Sara.txt_
          > <br> ____________________ _Silvio.txt_
          > <br> ____________________ **Waitlist/**
          > <br> ______________________________ _Hanna.txt_
          > <br> ______________________________ _Haris.txt_
          > <br> ______________________________ _Netta.txt_
          > <br> __________ **WinterCohort/**
          > <br> ____________________ _Santiago.txt_
          > <br> ____________________ _Iris.txt_
          > <br> ____________________ _Naomi.txt_

<br>

1. Sadly Edgar had to drop out of the course.  Delete the Edgar.txt file in FallCohort
2. This means we now have space in our Fall Cohort to move someone off of the waitlist.  Please move Netta.txt from the Waitlist folder into the FallCohort folder.
3. Please delete the Waitlist folder and its contents
4. It turns out that I misspelled Sara.  She spells her name "Sarah" with an "h" at the end.  Please rename the Sara.txt file to Sarah.txt
5. Unfortunately Italo is having a bit of a personal emergency, and he would like to move to our WinterCohort.  Please move the Italo.txt file from FallCohort to the WinterCohort folder
6. Oh no, our entire Winter Cohort had to be cancelled because of a worldwide pandemic :(   We decided to bump all of the scheduled winter students to spring. In the Bootcamp directory create a copy of the WinterCohort folder called SpringCohort
7. Please rename the WinterCohort folder to WinterCohortCANCELLED
8. Oh no! We're going out of business. Please delete the entire Bootcamp directory

<br>

---

#### Answer Part 1

> First we created some directoires using the **_mkdir_** command like so **_mkdir section8_DeletingCopingandMovingExercise/Bootcamp/FallCohort/Waitlist_** and then the final WinterCohort Folder **_mkdir section8_DeletingCopingandMovingExercise/Bootcamp/WinterCohort_**.

> Second we made some files with the **_touch_** command in all required directories, here is a an example **_touch Italo.txt Edgar.txt Linux.txt Sara.txt Silvio.txt_**

<br>

#### File Layout After Instructions
> .:
<br>Bootcamp

> ./Bootcamp:
<br>FallCohort  WinterCohort

> ./Bootcamp/FallCohort:
<br>Edgar.txt  Italo.txt  Linux.txt  Sara.txt  Silvio.txt  Waitlist

> ./Bootcamp/FallCohort/Waitlist:
<br>Hanna.txt  Haris.txt  Netta.txt

> ./Bootcamp/WinterCohort:
<br>Iris.txt  Naomi.txt  Santiago.txt

<br>

#### Answer Part 2
#### All commands are done from a parent directory : <br>**_Downloads/linuxStudies/section8_DeletingCopingandMovingExercise/Bootcamp_**

<br>

> 1. We removed Edgar with the **_rm_** Command as so **_rm FallCohort/Edgar.txt _**

> 2. We moved Natta.txt using the **_mv_** Command as so **_mv FallCohort/Waitlist/Netta.txt FallCohort/_**

> 3. We removed the Waitlist Directory using the rm Command as so **_rm -ri FallCohort/Waitlist/_** we also added a safety check with option **_i_** for prompting us before removing and this is the prompt.

> rm: descend into directory 'FallCohort/Waitlist/'? y
> <br>rm: remove regular empty file 'FallCohort/Waitlist/Hanna.txt'? y
> <br>rm: remove regular empty file 'FallCohort/Waitlist/Haris.txt'? y
> <br>rm: remove directory 'FallCohort/Waitlist/'? y

> 4. We renamed Sara.txt to Sarah.txt using the **_mv_** Command as so **_mv FallCohort/Sara.txt FallCohort/Sarah.txt_**

> 5. We moved Italo.txt from Fall to Winter Cohort using the **_mv_** Command as so **_mv FallCohort/Italo.txt WinterCohort/_**

> 6. We created a copy of the Winter Cohort and renamed it to SpringCohort using the **_cp_** Command as so **_cp -r WinterCohort/ SpringCohort/_**

> 7. We renamed the directory using the **_mv_** Command as so **_mv WinterCohort/ WinterCohortCANCELLED/_**

> 8. We removed the entire directory using the **_rm_** Command as so **_rm -r Bootcamp_** but not before making a back up of it using the **_cp_** command like so **_cp -r Bootcamp/ BootcampBackup_**