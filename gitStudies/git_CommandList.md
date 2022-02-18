###### ____.git_CommandList

<br>
<!-- Table of Contents -->

### Table of Contents
- [Git Configuration Command Table](#git-configuration-command-table)
- [Git basic Command Table](#git-basic-command-table)

<br>
<br>

### **Git Configuration Command Table**
|Command|Description|
|:---|:---|
|a) git config --global user.name 'Username' <br> b) git config user.name|This sets the global username for git <br> This calls upon the config file, to view the current username.|
|git config --global user.email 'Email Address' <br> git config user.email|This sets the global email for git <br> This calls upon the config file, to view the current user email.|
|git config --global core.editor 'User preferred Editor' <br> git config core.editor|This sets the default editor for the use with git <br> This calls upon the config file, to view the current default editor.|

<br>

### **Git basic Command Table**
|Command|Description|
|:---|:---|
|git init|Initialize a git repository.|
|git status|Checks the status of said repository, indicating whether or not.|
|git add < filename >|This adds any unstaged or untracked files to the staging area of git for preperation of the git command.|
|git commit <br> git commit -m '_Commit Message_' <br> git commit -a -m '_Commit Message_' <br> git commit --amend|git commit will commit any files that were added to the staging area with the git add command. You can also amend a previous commit with the --amend flag (However this only works with one commit behind)|
|git log <br> git log --oneline|git log will show the history of commits made in a repository.|
|git branch <br> git branch -v  <br> git branch < new-branch > <br> git branch -m < renamed-branch > <br> git branch -d < branch-name > <br> git branch -D < branch-name >|git branch can be used to view the current branches on a git repository either just name or in detail with -v flag, it can create a branch, it rename existing branchs (_granted you on the branch_), it delete and force delete branches as well.|
|git switch < branch-name > <br> git switch -c < new-branch > |git switch is used to switch between branches on a git repository, however it can also create a branch with the correct flag.|
|git checkout <br> git checkout -b < new-branch >|git checkout is an older command than git switch, however it do many things. The 2 higlighted here are examples of switching branches and creating a branch.
|git merge < branch-name  >|This command merges branches together|