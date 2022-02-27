###### - section7_MergingBranches,OhBoy

<br>

<!-- Section Header -->

![section7Header](../src/doc/section07Header.png 'Section 7 Header')

<!-- Table of Contents -->

### Table of Contents

+ [Introduction to Merging](#introduction-to-merging)
    - [What is Merging & how & why we do it?](#what-is-merging--how--why-we-do-it)
    - [Feature branch](#feature-branch)
+ [Visualizing Merges](#visualizing-merges)
    - [Fast Forward Merges](#fast-forward-merges)
    - [Essentially what a fast forward merge looks like in a simplified form](#essentially-what-a-fast-forward-merge-looks-like-in-a-simplified-form)
    - [Merge Commits](#merge-commits)
+ [Generating Merge Commits](#generating-merge-commits)
    - [Merge Commit without Conflict](#merge-commit-without-conflict)
    - [Merge Commit with Conflict](#merge-commit-with-conflict)
+ [Resolving Merge Conflicts](#resolving-merge-conflicts)
    - [The multi step process to resolving merge conflicts](#the-multi-step-process-to-resolving-merge-conflicts)

![divider](../src/doc/divider.png 'Divider')

<!-- Start of Document -->

## **Introduction to Merging**

<br>
<br>

### **What is Merging & how & why we do it?**

Merging in git is used when wanting to add the contents of another branch into said branch you wish to merge into. Generally, this is your master branch or main. The way you merge in git is by using the following command **git merge < branch-name >**.

You also want to be on the branch you want to be merged into. As an example, if you want to merge bugfix branch into your master branch, then you need to be on the master branch. When it comes to merging you have 2 types of merging:
* Fast Forward merging
* Merge Commits
_Side Note: Merge commits can be with or without [resolving merge conflicts](#resolving-merge-conflicts 'See what a merge conflict is')._

To understand why we merge branches together, you need to understand the workflow, as illustrated.

<br>
<br>

### **Feature branch**

<br>
<br>

![featureBranch](../src/featureBranch.png 'An illustration of what a feature branch is & why we merge branches')

<br>
<br>

Above is known as a feature branch, this ties in with branches in section6. However, when doing a feature branch you would like to test a possible features on a completely isolated work enviroment that doesnt affect the master branch and hurt the original code. If the feature gets accepted into the project, you need a way to merge that work into the main project, hence git merge. 

<br>
<br>

## **Visualizing Merges**

<br>
<br>

### **Fast Forward Merges**

<br>
<br>

![fastForwardMerge1](../src/fastForwardMerge1.png 'An illustration of a fast forward merge')

<br>
<br>

### **Essentially what a fast forward merge looks like in a simplified form**

<br>
<br>

![fastForwardMerge2](../src/fastForwardMerge2.png 'A simplified illustration of a fast forward merge')

<br>
<br>

A fast forward merge is essentially when the branch being merge into has no further commits made from point of splintering into another branch. Looking at the diagram above you notice the 2 branches, Master & Bugfix, Master remains in place with no further commits made to its branch.

However the bugfix branch continues further and later when using **git merge** you basically just catching up the parent or desired branch to the HEAD of the branch being merge in. _Which in this case is the bugfix branch being merge back into the parent branch_. 

<br>
<br>

### **Merge Commits**

<br>
<br>

![mergeCommit](../src/mergeCommit.png 'An example of merge commit')

<br>
<br>

## **Generating Merge Commits**

A merge commit happens when the parent branch continues to provide commits that other branches do not have. The above diagram is an example of a "[Merge Commit](#merge-commits 'An example of a merge commit')". You see the **Bugfix** branch split a commt earlier from the parent branch and therefor doesnt have the most rcent commit information from said parent branch.

When merging, you will generate what is known as a merge commit, this explaining that a particular branch has been merged with current branch whether it be master or something else. However there can be merge conflicts that appear, you can also have a merge commit with any conflicts and we will explore how that works.

<br>
<br>

### **Merge Commit without Conflict**

<br>
<br>

![mergeCommitWithoutConflict](../src/mergeCommitWithoutConflict.png 'Illustrating a merge commit without a conflict')

<br>
<br>

Above is an example illustration of what a merge commit without a conflict would look like. To generate a merge commit without any conflicts, although its not as black n white as avoiding overlaps or not changing a particular file being worked on in another branch. 

In general thats a very straight forward approach to avoid conflict. However in the real world multiple developers won't wait for something to be approved before continuing with their own work. This is why its important to understand what merge conflicts are.

<br>
<br>

### **Merge Commit with Conflict**

<br>
<br>

![mergeCommitWithConflict](../src/mergeCommitWithConflict.png 'Illustrating a merge commit that results in a conflict')

<br>
<br>

Taking a look at the above illustration, we see a very crude example of what a merge conflict is and as before this happens when the parent branch has commits that the current branch no longer has and somehow comes into conflict with what is on the parent branch.

Again a rough example of this, when there is overlap with 2 different sets of information, as an example line 4 says hello on the master branch, yet on the bugfix branch line 4 has Hola. Again this is a very crude example of a merge conflict but the key is understanding how it happens and how to resolve it.

<br>
<br>

## **Resolving Merge Conflicts**

<br>
<br>

![mergeCommitConflictMarkers](../src/mergeCommitConflictMarkers.png 'An example ofmerge conflict markers')

<br>
<br>

When it comes to resolving merge conflicts, the first thing you notice is above in the illustration which shows you what you would expect to see. You will see this in your default editor when trying to merge and receiving a **CONFLICT** error. Depending on your editor, it can either have some automated functions to make it easier to remove the markers and merge options, or you will have to remove them manually.

Breaking down the markers we see from top down **<<<< HEAD**, This indicates the current changes on the branch being merged into. Going down to the middle we see what separates **====** the current changes from incoming.

At the bottom we see the incoming changes, with the branch name as so **>>>> Bugfix**

<br>
<br>

### **The multi step process to resolving merge conflicts**

When it comes to resolving merge conflicts there is a multi step process to follow.
1. Open up the file(s) with the merge conflicts
2. Edit the file(s) to remvoe the conflicts, Decide which branch's content you wish to keep. Or keep the content from both.
3. Remove the conflict markers as illustated [here](#resolving-merge-conflicts "An illustration of conflict markers")
4. Add your changes and then make a commit.

<br>
<br>

<!-- End of Document -->

![endDivider](../src/doc/endDivider.png 'End of Document')