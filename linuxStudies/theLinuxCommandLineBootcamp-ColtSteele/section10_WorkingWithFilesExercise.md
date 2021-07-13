###### ____.section10_WorkingWithFilesExercise

## Part 1
## Question 1

* Use a command to print out the entire contents of the poem.txt file. 
    * Use an option so that the output also includes line numbers.

<br>

#### Answer

> To print the entire contents of the poem.txt file we used a command known as **_cat_** and then the filename.

> So we used **_man_** command on **_cat_** to find an option to allow us to print the line numbers which was the option -n or the long form --numbers as an example : **_cat -n poem.txt _**

---

## Question 2..., 3, 4

* That is a headache to read all at once! Read poem.txt using less instead. 
    * Scroll down one line at a time
    * Scroll up one line at a time
    * Scroll down one "page" at a time
    * Scroll up one "page" at a time
* Search within less for the term "Dog".  Can you find the line that contains it?

* **_Bonus_** : can you run a case-insesitive search?  The poem contains both "dog" and "Dog" on separate lines.

<br>

#### Answer

> To view the poem in less, we use the **_less_** command like so : **_less poem.txt_**

>> To scrol down one line at a time, we can use the **_arrow key down_** or hit **_return_** key to move down one line at a time.

>> To scroll up one line at a time, we can use the **_Ctrl + T_** or the **_up arrow key_** on the keyboard

>> To scroll down one page, we use the **_Ctrl + V_** keyboard shortcut or the **_spacebar_**

>> To scroll up one page we use the **_Ctrl + B_** Keyboard Shortcut

> To search within less you use the **_forward  slash /_** key and enter the desired word, and the line that contains Dog is as follows : **_The Beggars Dog & Widows Cat_**

> To do a case-insensitive search, you will have it input **_-I_** followed by return and then enter the name, there is another version **_-i_** however this only works for lowercase search, if you had to search with uppercase it will not ignore the case sensitivness.

---

## Question 5, 6...

* Now it's time to do some research! 
* Find the option to tell less to open with lines numbers displayed. 
    * Open poem.txt this way
* Then find the "command" you can type into less to go to exactly 50% of the way through the file.
    * Use a command to find the number of words in poem.txt
    * Run a command to print out the first 4 lines of poem.txt
    * Run a command to print out the last 8 lines of poem.txt

<br>

#### Answer

> To open less while displaying the line numbers, we use the option **_-N_** like so : **_less -N poem.txt_**

> The command within less to go exactly halfway is by entering the number and then pressing the **_%_** key and everythig will disappear and it will locate 50 %.

>> To find the number of words within the poem we use the **_wc_** command, more specifically we use the **_wc -w_** for only seeing the amount of words.

>> To print the first 4 lines of the poem, we use the **_head_** command and again more specifically we use the **_head -n_** command as follows : **_head -n 4 poem.txt_** 

>> To print the last 8 lines of poem.txt, we used the **_tail_** command, and once again more specifically **_tail -n_** as follows : **_tail -n 8 poem.txt_**

---

## Part 2
## Question 1

* Run a command to print out the lines in purchases.txt in reverse order (last line printed first)

<br>

#### Answer

> Inorder to print the last line first, we use the **_tac_** command as follows : **_tac purchases.txt_**

---

## Question 2

* Run a command to print out the lines in purchases.txt, sorted alphabetically.

<br>

#### Answer

> To sort the file alphabetically we use the **_sort_** command as follows : **_sort purchases.txt_**

---

## Question 3

* Run a command to count the number of lines in purchases.txt

<br>

#### Answer

> To count the number of lines we use the **_wc_** command and more specifically the **_wc -l_** command as follows : **_wc -l purchases.txt_**

---

## Question 4

* Run a command to print out the lines in purchases.txt, sorted by the price (the final column) in the dataset in REVERSE order (highest price to lowest price)

<br>

#### Answer

> In order to sort the purchases.txt file inorder of the specified demands, we used the **_sort_** command and more specifically the sort **_-r(reverse) -k(columb) N_** as follows : **_sort -rk 3 purchases.txt_**

---