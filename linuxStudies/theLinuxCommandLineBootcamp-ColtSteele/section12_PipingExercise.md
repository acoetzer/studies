###### ____.section12_PipingExercise

## Question 1

* Count the number of Pokemon files in the PokeDex/ folder. You'll need to combine commands to make this work!

<br>

#### Answer

> We used a combination of the **_ls_** command including the option **_-1_** to list each file on it own line. So that we do not include the word or line/heading "total", ensuring it only selects files with a pipe to the **_wc_** command and the option **_-l_** to count the lines as follows : **_ls -1 section12_PipingExercise/PokemonExercise/PokeDex/ | wc -l_** 

> The total number of files/pokemons was **_719_** or **_720_** including the heading "total"

---

## Question 2

* Next, create a new single file called all-pokemon.txt in the PokemonExercise folder (NOT the PokeDex folder)that contains the LOWERCASED name of every single Pokemon file in the directory, sorted in numerical order! 

<br>

#### Answer

> We used the **_ls_** command with option **_-1_** to list only the file names, we then sorted the file numerically using the **_sort_** command with **_-n_** option and then we use the **_tr_** command and changed the sets A-Z to a-z so that all words become lowercased and then save or output that informaition to a .txt file as follows : **_ls -1 section12_PipingExercise/PokemonExercise/PokeDex/ | sort -n | tr A-Z a-z > section12_PipingExercise/PokemonExercise/all-pokemon.txt_**

---

## Question 3

* Now that we have this file that includes all the Pokemon in numerical order, let's print out the three pigeon-related Pokemon: pidgey, pidgeotto, and pidgeot.  Using the command-line, print out lines 16-18. 

<br>

#### Answer

> For this we use only the **_head_** and **_tail_** command as follows : **_head -18 section12_PipingExercise/PokemonExercise/all-pokemon.txt | tail -3_** which in turn gave us the desired output.

---

## Question 4

* Next, up let's isolate the original 151 Pokemon.  Using a single pipeline...
    * output the first 151 lines of the all-pokemon.txt file
    * remove all digits 0-9 from the lines (using tr )
    * sort the now number-less lines alphabetically
    * store the new result in a file called original-151.txt in PokemonExercise

<br>

#### Answer

> We first used the **_head_** command to isolate the first 151 pokemon, and then used **_tr_** command with option **_-d_** and set **_0-9_** to remove the digits, we then sorted the list alphabetically using the **_sort_** command and then we output the file as instructed as follows : **_head -151 section12_PipingExercise/PokemonExercise/all-pokemon.txt | tr -d 0-9 | sort > section12_PipingExercise/PokemonExercise/original-151.txt_**

> Alternatively we could also use **_tr -d [:digit:]_** to remove digits

---
