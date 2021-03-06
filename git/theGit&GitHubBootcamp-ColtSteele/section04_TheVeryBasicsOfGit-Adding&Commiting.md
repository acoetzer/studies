###### - section4_TheVeryBasicsOfGit:Adding&Committing

<br>

<!--
Section Header
-->

![section4Header](../../src/git/doc/section04Header.png 'Section4 Header')

<!--
Table of Contents 
-->

### **Table of Contents**

+ [What is a Git repo](#what-is-a-git-repo)
+ [Our first commands](#our-first-commands)
    - [Git init & Git status](#git-init--git-status)
+ [The mysterious .git folder](#the-mysterious-git-folder)
+ [A common mistake](#a-common-mistake)
+ [The committing workflow overview](#the-committing-workflow-overview)
+ [Staging changes with the git add command](#staging-changes-with-the-git-add-command)
+ [Finally, the git commit command](#finally-the-git-commit-command)
+ [The git log command](#the-git-log-command)

<br>
<br>

<!--
Start of Document
-->

## **What is a Git repo**

A git repo is a workspace which tracks and manages files within a folder. _Repo is short for repository_ 

## **Our first commands**

<br>
<br>

### **Git init & Git status**

<br>
<br>

![repoJarDiagram](../../src/git/repoJarDiagram.png 'Diagram illustrating a git repository')

<br>
<br>

**git status** is generally used to check the status of a repo. Another use is to check weather or not a folder is already a repo, or check the status of a given repo just before committing.

**git init** is used to great or initialize a git repository. This process tends to only happen once during a project. The folder you wish to initialize will also initialize the sub-directories and do not need to be initialized again.

<br>
<br>

## **The mysterious .git folder**

<br>
<br>

![hiddenGitFolder](../../src/git/hiddenGitFolder.png 'Illustrating the .git folder within a git repo')

<br>
<br>

When initializing a repository within a folder, it will create an empty hidden .git folder. This is where git store all that repository's history and logs.

In the example above you see the **.git** folder within a repository for the folder studies.

<br>
<br>

## **A common mistake**

There are times when you would make a repo within a repo. The way one removes this error, is to delete that specific .git folder. In order to combat that mistake, that is why you would use git status first. Its important to remember that git works from top down.

Anything inside the initial repository, will be added to the git repo this including sub-directories.

<br>
<br>

## **The committing workflow overview**

<br>
<br>

![gitWorkflowOverview](../../src/git/gitWorkflowOverview.png 'Illustration showing the git workflow of committing a file')

<br>
<br>

When it comes to committing within git, there are somewhat 2 commands that one has to go through.
* **git add < file1 > < file2 >**
* git commit -m 'comment'
The comment is a summarized description of what is being committed, However, before any of these commands can take affect. You will need to add, change or modify the contents within a git repository. There are essentially 3 parts to this workflow of committing a file to git.

<br>
<br>

## **Staging changes with the git add command**

<br>
<br>

![gitaddCommand](../../src/git/gitaddCommand.png 'Example of a git add command')

<br>
<br>

We use the **git add** command to stage changes to be committed. **git add** is 1 of 2 stages in order to commit work to a git repository. This process allows you to add or group specific files and folders separate from each other as seen below.

Seeing the image above you can see how **git add** allows you to add specific files separate from other files. In this case we staging all the src image files first and then committing it.

<br>
<br>

## **Finally, the git commit command**

<br>
<br>

![gitcommitCommand](../../src/git/gitcommitCommand.png 'Example of a git commit command')

<br>
<br>

We then use the **git commit -m 'comment'** command to commit changes that are in the staging area to the repository. This is the 2nd stage of committing work in the order of committing workflow. The example below expands on the above demonstration, showing that after adding the work to the staging area you can then commit the work.

<br>
<br>

## **The git log command**

<br>
<br>

![gitlogCommand](../../src/git/gitlogCommand.png 'Example of the git log command')

<br>
<br>

The **git log** command shows the history of previous commits made in that repository. The above example shows the command **git log --oneline**, which displays each log entry on a single line.

<br>
<br>

<!--
End of Document
-->