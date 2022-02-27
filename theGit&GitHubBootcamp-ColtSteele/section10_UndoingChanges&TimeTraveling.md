###### - section10_UndoingChanges&TimeTraveling

<br>

<!-- Section Header -->

![section10Header](../src/doc/section10Header.png 'Section 10 Header')

<!-- Table of Contents -->

### Table of Contents

+ [Checking out old commits](#checking-out-old-commits)
+ [Re-Attaching our Detached HEAD!](#re-attaching-our-detached-head)
+ [Referencing commits Relative to HEAD](#referencing-commits-relative-to-head)
+ [Discarding changes with git checkout](#discarding-changes-with-git-checkout)
+ [Un-modifying with git restore](#un-modifying-with-git-restore)
    - [Un-staging changes with git restore](#un-staging-changes-with-git-restore)
+ [Undoing commits with git reset](#undoing-commits-with-git-reset)
    - [git reset < commit/HEAD~1 >](#git-reset--commithead1)
    - [git reset --hard < commit/HEAD~1 >](#git-reset---hard--commithead1)
+ [Reverting commits with ... git revert](#reverting-commits-with--git-revert)

![divider](../src/doc/divider.png 'Divider')

<!-- Start of Document -->

## **Checking out old commits**

Checking out older commits is something like time traveling.
* **git checkout < f994it1 >** or **[git checkout HEAD~1](#referencing-commits-relative-to-head)**

This is how you can time travel back to previous commits. When doing so, it will place you in a de-tached HEAD state, that means HEAD no longer points to the Branch which references the latest commit on that branch. It points solely to that specific commit.

In de-tached HEAD state, you can can edit, make a new branch and work solely with previous content. Getting back to the commands, you can either use the commit hash to go back, or you can reference the HEAD, tilde key and how many commits back. 

<br>
<br>

## **Re-Attaching our Detached HEAD!**

To re-attach your HEAD to Branch, all you need to do is switch to the branch you were on. There a few ways one can do this:
* **git checkout < branch-name >**
* **git switch < branch-name >**
* **git switch -**
    * \__ _This last one is kind of like a shortcut, use case is if you forgot which branch you were on, you can just use a dash, and it will take you back to your last branch_

<br>
<br>

## **Referencing commits Relative to HEAD**

To reference commits relative to HEAD as explained above, you can type the command like so.
* **git checkout HEAD~1**
The HEAD~1 is basically saying, to go from HEAD back 1 commit.

<br>
<br>

## **Discarding changes with git checkout**

Discard changes with **git checkout HEAD < filename >** or **git checkout -- < filename >**, The **--** once again is just a shortcut way of doing things. However the command above, will restore any file to the latest commit on that branch.

<br>
<br>

## **Un-modifying with git restore**

So like **git checkout HEAD < filename >**, **git restore < filename >** does the same thing, Because some devs feel checkout does too many things, they started to add new commands to git, such as **git switch** & **git restore** to remove some weight from the checkout command.

<br>
<br>

### **Un-staging changes with git restore**

Another command within git restore, is the ability to unstaged files using **git restore --staged < filename >**, This just removes any staged files back to un-staged.

<br>
<br>

## **Undoing commits with git reset**

**git reset** comes in 2 flavours, you have **git reset < commit >** & **git reset --hard < commit >** including referencing HEAD as so **git reset HEAD~1**

<br>
<br>

### **git reset < commit/HEAD~1 >**

**git reset** resets back to a specific commit. If for example you go back 2 commits using the reset command, you will delete those commits up until the commit but not including the commit you reset to.

Another thing that happens, is that when just using git reset, it will keep the changes in the file as it was before removing the commits as uncommited work. 
    * _tip_ You can make another branch and then commit the work there if you wish to keep it.
In short, you lose the commits, but keep the changes.

<br>
<br>

### **git reset --hard < commit/HEAD~1 >**

**git reset --hard** is the same as **git reset** however instead of keeping the changes, it removes them.

<br>
<br>

## **Reverting commits with ... git revert**

**git revert < commit >** is similar to **git reset** with the only difference being that it keeps the commits and promps you to enter a commit message, the same way as git merge does. Basically Asking which changes to keep, Then makes a revert commit.

Where git reset goes backwards, git revert goes forward with a new commit, keeps previous commits, yet undoes changes up until whatever commit hash was input.

<br>
<br>

<!-- End of Document -->

![endDivider](../src/doc/endDivider.png 'End of Document')