###### - section9_TheInsAndOutsOfStashing

<br>

<!-- Section Header -->

![section9Header](../src/doc/section09Header.png 'Section 9 Header')

<!-- Table of Contents -->

### **Table of Contents**

+ [Why we need git stash](#why-we-need-git-stash)
+ [Stash basics: git stash save & pop](#stash-basics-git-stash-save--pop)
    - [git stash | git stash save](#git-stash--git-stash-save)
    - [git stash pop](#git-stash-pop)
+ [Git stash apply](#git-stash-apply)
+ [Working with multiple stashes](#working-with-multiple-stashes)
+ [Dropping & Clearing the stash](#dropping--clearing-the-stash)

![divider](../src/doc/divider.png 'Divider')

<!-- Start of Document -->

## **Why we need git stash**

You would use git **git stash** or **git stash save** in cases where you ould need to swap branches before you have made a commit. You would think to just create a commit, however commits are seen as history of a particular project, so completing something halfway, is not an ideal commit. So this is why people would use git stash, among avoiding conflicts.

<br>
<br>

##  **Stash basics: git stash save & pop**

<br>
<br>

### **git stash | git stash save**

**git stash | git stash save** is the same thing. This command stashes work whether it be staged or unstaged.

<br>
<br>

### **git stash pop**

This command pops the contents within the stash completely out, removing it from the stash library. 

<br>
<br>

## **Git stash apply**

**git stash apply** is similar to git stash pop however where pop removes the contents of the stash, apply only applies the content while keeping the contents within the stash allowing you to use it on another branch. Essentially your could use this repeatedly.

<br>
<br>

## **Working with multiple stashes**

It is possible to store multiple stashes, each stash will have a stash id like so
* stash@{0}, stash@{1} or stash@{2} etc.

To retreive a particular stash, you can use the pop or apply command with the stash id
* **git stash pop stash@{2}** or **git stash apply stash@{1}**

<br>
<br>

## **Dropping & Clearing the stash**

You can also completely remove all stash or just one in particular by using
* **git stash drop stash@{id}**
* **git stash clear**
    * _note that clear will remove all stashes_

<br>
<br>

<!-- End of Document -->

![endDivider](../src/doc/endDivider.png 'End of Document')