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
* When it comes to merging you have 2 types of merging.
    * Fast Forward merging
    * Merge Commit
        * _Side note: Merge commits can be with or without [merge conflicts](#merge-conflicts 'See what a merge conflict is')._
* To understand why we merge branches together, you need to understand the workflow, as illustrated.
<br>

![featureBranch](./src/featureBranch.png 'An illustration of what a feature branch is & why we merge branches')

<br>

* Above is known as a feature branch, this ties in with branches in section6. 
    * However, when doing a feature branch you would like to test a possible features on a completely isolated work enviroment that doesnt affect the master branch and hurt the original code. 
        * If the feature gets accepted into the project, you need a way to merge that work into the main project, hence git merge. 


# **Visualizing Merges**
### **Fast Forward Merges**
![fastForwardMerge](./src/fastForwardMerge.png 'An illustration of a fast forward merge')

<br>

* 