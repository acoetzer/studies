###### - section5_CommitsInDetail(AndRelatedTopics)

<br>

<!--
Section Header
-->

![section5Header](../../src/git/doc/section05Header.png 'Section 5 Header')

<!--
Table of Contents 
-->

### **Table of Contents**

+ [Keeping your git commits atomic](#keeping-your-git-commits-atomic)
+ [Commit messaging](#commit-messaging)
    - [Past or present tense](#past-or-present-tense)
+ [Escaping VIM & Configuring Git's Default Editor](#escaping-vim--configuring-gits-default-editor)
    - [git config --global core.editor 'code --wait' ](#git-config---global-coreeditor-code---wait)
+ [A Closer Look At The Git Log Command](#a-closer-look-at-the-git-log-command)
    - [git log --oneline](#git-log---oneline)
    - [Example](#example)
+ [Fixing Mistakes With Amend](#fixing-mistakes-with-amend)
    - [git commit --amend](#git-commit---amend)
+ [Ignoring Files w/ .gitignore](#ignoring-files-w-gitignore)

<br>
<br>

<!--
Start of Document
-->

## **Keeping your git commits atomic**

The idea for keeping your commits made in git atomic means to try and keep your commits separate and organized for a better word. Almost as if your categorizing your commits. This is done so that if you ever need to go back that you do not undo a lot of changes. 

As an example if you building a website, you just made a nav bar, it would be wise to commit and comment making nav bar. 

<br>
<br>

## **Commit messaging**

<br>
<br>

### **Past or present tense**

According to the official documentation of git, its in best practice to keep your commits in the present tense.

<br>
<br>

## **Escaping VIM & Configuring Git's Default Editor**

<br>
<br>

### **git config --global core.editor 'code --wait'**

<br>
<br>

### **Link:** [A list of command for changing your default editor](https://git-scm.com/book/en/v2/Appendix-C%3A-Git-Commands-Setup-and-Config 'A list of command for changing your default editor')

When installing git on a device other than windows, when committing with the git commit command without the **(-m '')** flag, git will tend to opn in the default editor such as Vim or Nano. To change the default editor one can use the **git config --global core.editor 'whatever editor you use here'**

<br>
<br>

## **A Closer Look At The Git Log Command**

<br>
<br>

### **git log --oneline**

When using the **git log** command you are give a log that takes up a lot of space within the terminal, and there is a flag you can add it to make the log output neater and more compact.
* **git log --oneline** will compact the output of the git log command

<br>
<br>

### **git log**

<br>
<br>

![gitlogCommanda](../../src/git/gitlogCommanda.png 'Example of git log without a compact output')

<br>
<br>

### **git log --oneline**

<br>
<br>

![gitlogCommandb](../../src/git/gitlogCommandb.png 'Example of compact git log output')

<br>
<br>

## **Fixing Mistakes With Amend**

<br>
<br>

### **git commit --amend**

You can use the amend command to go back one previous commit to change or edit that commit incase you left something out or made a mistake. An example would be something like:
    
* **git commit -m 'some commit'**
* **git add < forgotten file >**
* **git commit --amend**

<br>
<br>

## **Ignoring Files w/ .gitignore**

<br>
<br>

### **Link:** [Website that can give you some default .gitignore starter templates](https://www.toptal.com/developers/gitignore 'Website that can give you some default .gitignore starter templates')

<br>
<br>

When committing files with git, it is possible to tell git to ignore certain files there not always having to add each file separately in fear of mistakenly adding a file that you want ignored. An example of some file you would want ignored can be:
* Secrets, API_Keys, Credentials, etc.
* Operating system files (DS_Store on a Mac)
* Log Files
* Dependencies & Packages
So to do this, you would make a file named .gitignore in the main directory where your git repository is. Then add all the files you want git to ignore. Some possible file types: 
* .DS_Store (Will ignore files named .DS_Store)
* folderName/ (Will ignore entire folder or directory)
* *.log (You can also use wildcard, so will ignore every file that ends in .log no matter whats written before that)
The next time you run git, it will ask if your want to add and commit the .gitignore and yes you do want to do that. You will also notice that the said ignore files will no longer appear when checking your repo, even when making changes to said files.

<br>
<br>

<!--
End of Document
-->