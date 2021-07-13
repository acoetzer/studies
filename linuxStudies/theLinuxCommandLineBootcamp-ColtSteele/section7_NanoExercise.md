###### ____.section7_NanoExercise

## Part 1
## Question 1, 2, 3, 4

* Open up the recipe.txt file using nano
* On line 3, add your own name after Author: so that it says Author: Stevie Wonder or whatever your name is
* Whoever wrote this recipe didn't know how to spell "parmesan", so instead they wrote "parm".  Please update the two instances of "Parm" to "Parmesan".  You can do this manually or by using nano's replace feature.
* Write out your changes! Close the file.

<br>

#### Answer

> To open the file we used the command **_nano_** and the filename, in this case **_recipe.txt_**.

> To add the name, we just navigated to the location using the arrow keys.

> When fixing the spelling mistake, we used the shortcut **_ctrl + T_** and navigated though the words using the **_i_** keybind which stands for ignore, until we landed upon parm, we then used **_R_** to replace all. <br><br> Note that after replacing the word parm to parmesan, we had to continue with i until it reach the end of the document and passed the second parm inorder to repllace it.

> To save the file, we just hit **_Ctrl + O_** to write the changed to the document and then hit **_Ctrl + X_** to leave.

---

<br>
<br>

---

## Part 2
## Question 1

* Open up the website.html file with nano
* This html file contains a simple website for a fictional restaurant called "Ristorante Colt".  You recently purchased the restaurant and have decided to change its name! Please replace all instance of "Ristorante Colt" with your new restaurant's name.  Do this using a nano shortcut, rather than manually replacing each one.
* Save your changes and close the file!

<br>

#### Answer

> We again opened the file using the **_nano_** command and the filename this time was **_website.html_**

> We used the shortcut **_Ctrl + backslash_** to replace all names needing change. We entered the desired name to be changed and replaced with a different name.

> Again to save we use the shortcut **_Ctrl + O_** to write the changes and then again **_Ctrl + X_** to exit.

---

<br>
<br>

---

## Part 3
## Question 1, 2, 3

* The country-data.json file contains a large country dataset, with over 39,000 lines of json!
* Unfortunately, there is a typo on line 15399.  It says "Hondras" but it should say "Honduras".  Please fix this!  Rather than scrolling for a decade, use a nano shortcut to jump to line 15399.
* **Bonus**: Figure out how to tell nano to open the file at exactly 15399.


<br>

#### Answer

>  We opened the .json file using the **_nano_** command, but as the bonus asks, to try and open the error on a specific line, which can be done like so **_nano +15399 country-data.json_**. <br><br>If we opened the file first and then had to navigate to the said line, we could have used the shortcut **_Ctrl + Shift + Underscore_** and then enter the line number, which was in this case 15399.

---

## Bonus
## Question 1

* The review.txt file contains a text review of the Cacio E Pepe recipe from recipe.txt
* Open up the recipe.txt file using nano and scroll to the bottom.
* Using a nano shortcut we have not covered, insert the contents of review.txt at the bottom of recipe.txt. 

<br>

#### Answer

> We opened recipe.txt with the command **_nano_**, used the **_alt + slash keys_** to move from end to end and then used the shortcut **_Ctrl + R_** to insert another .txt file or to be more exact the review.txt file, which basically pasted the file contents of the review.txt into recipe.txt file.

---