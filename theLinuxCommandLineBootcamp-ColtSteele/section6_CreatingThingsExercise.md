###### - section6_CreatingThingsExercise

## Question 1, 2

* Create a new folder called my-app
* Navigate to my-app and inside create two new empty files called README.md and package.json

<br>

#### Answer

> To create a new directory, we used the **_mkdir_** command to make my-app as follows : **_mkdir my-app_**.

> We created the two files using the **_touch_** command as follows : **_touch README.MD package.json_**

---

## Question 3

* Still inside of my-app create a new folder called public. Without cd-ing into public, create an index.html file inside of it.

<br>

#### Answer

> We again used the **_mkdir_** command as follows : **_mkdir public_**

> We then without cd-ing into public made the .html file with the **_touch_** command, by providing it with a path to public as follows : **_touch public/index.html_**

---

## Question 4

* Create a new folder called src inside of my-app.  Navigate inside of it.

<br>

#### Answer

> Simple we use the **_mkdir_** command to make the src and then cd'd into it using the **_cd_** command

---

## Question 5

* Using a single line, create the following four files inside of src: App.css, App.js, index.css, and index.js

<br>

#### Answer

>  Using the **_touch_** command we made the four files as follows : **_touch App.css App.js index.css index.js_**

---

## Bonus Question

* Using a single command, create a new directory inside of src called components, and inside of that new components directory create a new directory called Navbar.   Do this using a single command, without first creating the components directory.

<br>

#### Answer

> So inorder to make the directories without first creating the parent directory, we had to search the _man page_ for _mkdir_ and for an option that allowed for creating parent directories first. 

> So the option used was **_-p or --parents_** and the command used was **_mkdir --parents components/Navbar_** 

---

## Folder/File Layout


<br>

.:
package.json  public  README.MD  src

./public:
index.html

./src:
App.css  App.js  components  index.css  index.js

./src/components:
Navbar

./src/components/Navbar:

<br>

> Using the command ls -R, we can list subdirectories recursively and show the layout of a particular folder and its sub directories.