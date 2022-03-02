###### - section6_WorkingWithBranches

<br>

<!--
Section Header
-->

![section6Header](../../src/git/doc/section06Header.png 'Section 6 Header')

<!--
Table of Contents 
-->

### **Table of Contents**

+ [Introducing Branches](#introducing-branches)
    - [What is a branch?](#what-is-a-branch)
+ [The Master Branch (Or Is It Main?)](#the-master-branch-or-is-it-main)
+ [What On Earth Is HEAD?](#what-on-earth-is-head)
+ [Viewing All Branches With Git Branch](#viewing-all-branches-with-git-branch)
+ [Creating & Switching Branches](#creating--switching-branches)
    - [Creating a branch + various methods](#creating-a-branch--various-methods)
    - [Switching branches](#switching-branches)
+ [Another Option: Git Checkout Vs. Git Switch](#another-option-git-checkout-vs-git-switch)
+ [Switching Branches With Unstaged Changes?](#switching-branches-with-unstaged-changes)
    - [Switching branches while having unstaged modified files.](#switching-branches-while-having-unstaged-modified-files)
    - [Switching branches while having untracked files.](#switching-branches-while-having-untracked-files)
+ [Deleting & Renaming Branches](#deleting--renaming-branches)
    - [Deleting a branch](#deleting-a-branch)
    - [git branch -d < branch-name >](#git-branch--d--branch-name)
    - [git branch -D < branch-name >](#git-branch--d--branch-name-1)
    - [Renaming a branch](#renaming-a-branch)

<br>
<br>

<!--
Start of Document
-->

## **Introducing Branches**

<br>
<br>

### **What is a branch?**

<br>
<br>

![gitBranchOverview](../../src/git/gitBranchOverview.png 'An visual example of what git branching would look like')

<br>
<br>

When making a repository, you are by default on whats known as a master branch. Technically you always on a branch, just some treat the "master" branch as the main where all changes will be merged into. A branch is essentially a linear timeline of check points and at anytime can splinter off the master, main or original branch and onto its owns separate timeline.

When branching off, or making a new branch, that branch is its own separate isolation of whatever particular commit it branched from. This meaning, whatever happens in that branch, will only affect that branch and none of the others. **_(Unless merged with another branch)_**

In the above diagram, you can see how developers can branch off a specific commit and build a feature, or experiment with new features, also known a feature branching. These branches can be merged with what is known as the master, main branch at any given time, or can be left out completely to a much later date.

<br>
<br>

## **The Master Branch (Or Is It Main?)**

The master branch is the initial branch made when initializing a git repository. However some people find the term 'Master' offensive, _Hi, from 2022_, even though this started in 2020. Tech companies are now pushing no offensive language or language that can be seen as offensive. Apart from that, the master or main is commonly seen as the original branch where all other branches will merge into.

<br>
<br>

## **What On Earth Is HEAD?**

<br>
<br>

![gitHEAD](../../src/git/gitHEAD.png 'An example of git HEAD pointer')

<br>
<br>

A HEAD is a term within git, which put simply is a pointer that references your current location within a git repository. So as you move from branch to branch, the HEAD will reference the current location.
* To add some clarification, as coming back to this section later on.
* HEAD points the current branch and the branch references the latest commit on that branch.

Later in the course, we get into the idea of being able to 'time travel', this introducing the the idea of de-taching HEAD, where HEAD nolonger points to the branch, but a specific commit. The above image you can see that the HEAD is referencing that we are on lily's branch.

<br>
<br>

## **Viewing All Branches With Git Branch**

<br>
<br>

![gitbranchCommand](../../src/git/gitbranchCommand.png 'An example of the git branch command')

<br>
<br>

To view all current branches on a particular repo, you can use a command known as **git branch**. Looking at the example above, you can see all branches within a repo, the one you currently on has the **'*'** next to it.

<br>
<br

## **Creating & Switching Branches**

<br>
<br>

### **Creating a branch + various methods**

To create a branch, you can use the **git branch < branch-name >** command. There are other ways to make a branch:
* _older command_ **git checkout -b < branch-name >** (This also switches you over to the nee branch made)
* _newer command_ **git switch -c < branch-name >** (This also switches you over to the new branch made)

<br>
<br>

## **Switching branches**
To switch a branch, you use the **git switch < branch-name >**

<br>
<br>

## **Another Option: Git Checkout Vs. Git Switch**

git checkout is kinda the swiss army knife of git, it can do a lot of things. However what we focusing on is the ability to switch from branch to branch. git checkout is a older command than git switch.

<br>
<br>

## **Switching Branches With Unstaged Changes?**

There some things to look out for when switch branches

<br>
<br>

## **Switching branches while having unstaged modified files.**

<br>
<br>

![gitUnstagedModifiedBranchSwitch](../../src/git/gitUnstagedModifiedBranchSwitchErr.png 'An example of when trying to branch switch with an unstaged modified version of a file')

<br>
<br>

One of the errors that could arise, is when trying to switch to another branch just after modifying something on the current branch you in, without committing it.

In the image above, you can see the user gets a warning when trying to switch branches before committing any changes.

<br>
<br>

## **Switching branches while having untracked files.**

<br>
<br>

![gitUntrackedBranchSwitch](../../src/git/gitUntrackedBranchSwitch.png 'An example of when switching a branch while have an untracked file within the git repo')

<br>
<br>

Here is when something interesting happens. If you made a new file and did not add or commit this file to the git repo, git will just ignore and carry it over to the next branch.

In the image above you notice that a new file was created, and when checking git status, see that it is indeed untracked. Though are able to move between branches seamlessly while carrying over the file created.

<br>
<br>

## **Deleting & Renaming Branches**

<br>
<br>

## **Deleting a branch**

You can Delete a branch using the **git branch -d < branch-name >** command. Though when using this particular flag, you will have to have first merged that branch onto the master or main before being able to delete it. Then again, you can use another flag such as so:
* **git branch -D < branch-name >**, to forcibly remove a branch without having to merge it.
* **_Side Note_**: When deleting a branch you cannot be on said branch when deleting it.

<br>
<br>

### **git branch -d < branch-name >**

<br>
<br>

![gitbranchlowerdCommand](../../src/git/gitbranchlowerdCommand.png 'An example of deleting a git branch with the flag -d')

<br>
<br>

### **git branch -D < branch-name >**

<br>
<br>

![gitbranchupperDCommand](../../src/git/gitbranchupperDCommand.png 'An example of deleting a git branch with the flag -D')

<br>
<br>

## **Renaming a branch**

<br>
<br>

![gitbranch-mCommand](../../src/git/gitbranch-mCommand.png 'An example of renaming a git branch')

<br>
<br>

You can rename a branch almsot the same way you rename a file in linux, using the move flag -m.
* **git branch -m < new-branch-name >**, Take note that unlike deleting a branch you need to be on that specific branch before you can rename it.

In the image above you can see how the branch name was changed.

<br>
<br>

<!--
End of Document
-->