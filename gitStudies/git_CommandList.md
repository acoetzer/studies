###### ____.git_CommandList

<br>
<!-- Table of Contents -->

### Table of Contents
- [Git Configuration Command Table](#git-configuration-command-table)
- [Setting up ssh keys for git](#setting-up-ssh-keys-for-git)
- [Git basic Command Table](#git-basic-command-table)

<br>
<br>

### **Git Configuration Command Table**
|Command|Description|
|:---|:---|
|a) git config --global user.name 'Username' <br> b) git config user.name|This sets the global username for git <br> This calls upon the config file, to view the current username.|
|git config --global user.email 'Email Address' <br> git config user.email|This sets the global email for git <br> This calls upon the config file, to view the current user email.|
|git config --global core.editor 'User preferred Editor' <br> git config core.editor|This sets the default editor for the use with git <br> This calls upon the config file, to view the current default editor.|
|git config --list <br> cat ~/.gitconfig|To list all values in the config file|

### **Setting up ssh keys for git**
|ssh steps|Description|
|:---|:---|
| ssh-keygen -t ed25519 -C 'your@email.here' <br> exec ssh-agent <br> ssh-add < private key/ ~/.ssh/id_ed25519 > <br> cat ~/.ssh/id_ed25519 & copy this to github | ez|

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
|git switch < branch-name > <br> git switch -c < new-branch > <br> git switch - |git switch is used to switch between branches on a git repository, however it can also create a branch with the correct flag.|
|git checkout <br> git checkout -b < new-branch > <br> git checkout < commit-hash/HEAD~1 > <br> git checkout --/HEAD < filename > |git checkout is an older command than git switch, however it do many things. It can time travel to other commits as well as restore previous commits|
|git merge < branch-name  >|This command merges branches together|
|git diff <br> git diff HEAD or git diff HEAD < filename  > <br> git diff --staged or git diff --staged < filename  > <br> git diff --cached <br> git diff branch1..branch2 <br> git diff commit1..commit2|The git diff command shows comparisons between files|
|git stash or git stash save <br> git stash pop <br> git stash apply <br> git stash list <br> git stash drop <br> git stash clear |git stash, allows you to stash files without having to commit, allowing you to move freely among branches|
|git restore < filename > <br> git restore --staged < filename >|git restore, the same as git checkout HEAD < filename >, it basically restores a file to the latest commit|
|git reset < commit-hash ><br> git reset --hard < commit-hash>|git reset, resets you to a previous commit, however deletes said commits from your history|
|git revert < Commit-hash >|git revert is the same as git reset, however it doesn't remove your commits, it goes forward by creating what is know as a revert commit|