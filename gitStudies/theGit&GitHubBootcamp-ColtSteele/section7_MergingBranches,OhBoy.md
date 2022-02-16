###### ____section7_MergingBranches,OhBoy

<br>

<!-- Table of Contents -->

### Table of Contents
- [Introduction to Merging](#introduction-to-merging)
    - [What is Merging & how & why we do it?](#what-is-merging--how--why-we-do-it)
- [Visualizing Merges](#visualizing-merges)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)

<br>
<br>

# **Introduction to Merging**
### **What is Merging & how & why we do it?**
* Merging in git is used when wanting to add the contents of another branch into said branch you wish to merge into.
    * Generally, this is your master branch or main.
* The way you merge in git is by using the following command **git merge < branch-name >**.
    * You also want to be on the branch you want to be merged into. 
        * As an example, if you want to merge bugfix branch into your master branch, then you need to be on the master branch. 
* When it comes to merging you have 2 types of merging.
    * Fast Forward merging
    * Merge Commits
        * _Side note: Merge commits can be with or without [merge conflicts](#merge-conflicts 'See what a merge conflict is')._
* To understand why we merge branches together, you need to understand the workflow, as illustrated.

### **Feature branch**
<br>

![featureBranch](./src/featureBranch.png 'An illustration of what a feature branch is & why we merge branches')

<br>

* Above is known as a feature branch, this ties in with branches in section6. 
    * However, when doing a feature branch you would like to test a possible features on a completely isolated work enviroment that doesnt affect the master branch and hurt the original code. 
        * If the feature gets accepted into the project, you need a way to merge that work into the main project, hence git merge. 


# **Visualizing Merges**
### **Fast Forward Merges**

<br>

![fastForwardMerge1](./src/fastForwardMerge1.png 'An illustration of a fast forward merge')

<br>

### **Essentially what a fast forward merge looks like in a simplified form**

<br>

![fastForwardMerge2](./src/fastForwardMerge2.png 'A simplified illustration of a fast forward merge')

<br>

* A fast forward merge is essentially when the branch being merge into has no further commits made from point of splintering into another branch. 
    * Looking at the diagram above you notice the 2 branches, Master & Bugfix, Master remains in place with no further commits made to its branch.
    * However the bugfix branches continues further and later when using **git merge** you basically just catching up the master branch to that the HEAD of the branch being merge in. 
        * _Which in this case is the bugfix branch_. 

### **Merge Commits**



<br>

![mergeCommit](./src/mergeCommit.png 'An example of merge commit without a conflict')

<br>

* Above is what a merge commit would look like.

<br>

### Merge Commit without Conflict

<br>

![mergeCommitWithoutConflict](./src/mergeCommitWithoutConflict.png 'Illustrating a merge commit that results in a conflict')

<br>

### Merge Commit with Conflict

<br>

![mergeCommitWithConflict](./src/mergeCommitWithConflict.png 'Illustrating a merge commit that results in a conflict')

<br>

# **Resolving Merge Conflicts**