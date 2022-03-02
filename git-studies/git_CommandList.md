###### - git_CommandList

<br>

<!--
Section Header
-->

![gitCommandList](../src/git/doc/gitCommandListHeader.png 'Git Command List')

<!-- 
Table of Contents
-->

### Table of Contents 

+ [Git Configuration Command Table](#git-configuration-command-table)
+ [Setting up ssh keys for git](#setting-up-ssh-keys-for-git)
+ [Git Command List](#git-command-list)
    - [Git Configuration Command Table](#)
    - [Setting up ssh keys for git](#)
   
|Git|Command|List|
|:---|:---|:---|
|[git init](#git-init)|[git stash](#git-stash)|[git show](#git-show)|
|[git status](#git-status)|[git restore](#git-restore)|[git reflog show](#git-reflog-show)|
|[git add](#git-add)|[git reset](#git-reset)||
|[git commit](#git-commit)|[git revert](#git-revert)||
|[git log](#git-log)|[git remote](#git-remote)||
|[git branch](#git-branch)|[git push](#git-push)||
|[git switch](#git-switch)|[git fetch](#git-fetch)||
|[git checkout](#git-checkout)|[git pull](#git-pull)||
|[git merge](#git-merge)|[git rebase](#git-rebase)||
|[git diff](#git-diff)|[git tag](#git-tag)||

<br>
<br>

<!-- 
Start of Document
-->

## **Git Command List**

<br>
<br>

### **Git Configuration Command Table** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|a) git config --global user.name 'Username' <br> b) git config user.name|This sets the global username for git <br> This calls upon the config file, to view the current username.|
|git config --global user.email 'Email Address' <br> git config user.email|This sets the global email for git <br> This calls upon the config file, to view the current user email.|
|git config --global core.editor 'User preferred Editor' <br> git config core.editor|This sets the default editor for the use with git <br> This calls upon the config file, to view the current default editor.|
|git config --list <br> cat ~/.gitconfig|To list all values in the config file|

<br>
<br>

### **Setting up ssh keys for git**
##### [go back](#table-of-contents 'Go back to Table of Contents')

|ssh steps|Description|
|:---|:---|
| ssh-keygen -t ed25519 -C 'your@email.here' <br> exec ssh-agent <br> ssh-add < private key/ ~/.ssh/id_ed25519 > <br> cat ~/.ssh/id_ed25519 & copy this to github | ez|

<br>
<br>

### **git init** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git init|Initialize a git repository.|

<br>
<br>

### **git status** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git status|Checks the status of said repository, indicating whether or not.|

<br>
<br>

### **git add** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git add < filename >|This adds any unstaged or untracked files to the staging area of git for preperation of the git command.|

<br>
<br>

### **git commit** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git commit <br> git commit -m '_Commit Message_' <br> git commit -a -m '_Commit Message_' <br> git commit --amend|git commit will commit any files that were added to the staging area with the git add command. You can also amend a previous commit with the --amend flag (However this only works with one commit behind)|

<br>
<br>

### **git log** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git log <br> git log --oneline|git log will show the history of commits made in a repository.|

<br>
<br>

### **git branch** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git branch <br> git branch -v  <br> git branch -a  <br> git branch -r <br> git branch < new-branch > <br> git branch -m < renamed-branch > -M (_to force_) <br> git branch -d < branch-name > <br> git branch -D < branch-name >|git branch can be used to view the current branches on a git repository either just name or in detail with -v flag, it can create a branch, it rename existing branchs (_granted you on the branch_), it delete and force delete branches as well.|

<br>
<br>

### **git switch** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git switch < branch-name > <br> git switch -c < new-branch > <br> git switch - |git switch is used to switch between branches on a git repository, however it can also create a branch with the correct flag.|

<br>
<br>

### **git checkout** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git checkout <br> git checkout -b < new-branch > <br> git checkout < commit-hash/HEAD~1 > <br> git checkout --/HEAD < filename > <br> git checkout origin/master <br> git checkout --track origin/main |git checkout is an older command than git switch, however it do many things. It can time travel to other commits as well as restore previous commits|

<br>
<br>

### **git merge** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git merge < branch-name  > <br> git merge --no-ff < branch-name >|This command merges branches together and second to stop a fast forward merge and do a force commit|

<br>
<br>

### **git diff** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git diff <br> git diff HEAD or git diff HEAD < filename  > <br> git diff --staged or git diff --staged < filename  > <br> git diff --cached <br> git diff branch1..branch2 <br> git diff commit1..commit2 <br> git diff < tag-name1> < tag-name2 >|The git diff command shows comparisons between files|

<br>
<br>

### **git stash** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git stash or git stash save <br> git stash pop <br> git stash apply <br> git stash list <br> git stash drop <br> git stash clear |git stash, allows you to stash files without having to commit, allowing you to move freely among branches|

<br>
<br>

### **git restore** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git restore < filename > <br> git restore --staged < filename >|git restore, the same as git checkout HEAD < filename >, it basically restores a file to the latest commit|

<br>
<br>

### **git reset** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git reset < commit-hash > <br> git reset --hard < commit-hash>|git reset, resets you to a previous commit, however deletes said commits from your history|

<br>
<br>

### **git revert** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git revert < Commit-hash >|git revert is the same as git reset, however it doesn't remove your commits, it goes forward by creating what is know as a revert commit|

<br>
<br>

### **git remote** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git remote <br> git remote -v <br> git remote add < remote-name > < url > <br> git remote show origin|You can use this command to view, either your remote name _(origin)_ or remotes, you can add remotes to repo's that were original initialized locally|

<br>
<br>

### **git push** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git push <br> git push < remote-name > < branch-name > <br> git push -u < remote-name > < branch-name > or git push --set-upstream < remote-name > < branch-name > <br> git push --delete < remote-name > < branch-name > <br> git push < tag-name> or git push --tags|You can use this command to push files to a git repo in the cloud, as well as deleting remote repo's and managing repo's in general and pushing tags|

<br>
<br>

### **git fetch** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git fetch or git fetch remote <br> git fetch < remote/_origin_> < branch/_main_>|This fetches whatever new files are on the remote, or remote branch and places it in the local repo|

<br>
<br>

### **git pull** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git pull <br> git pull < remote/_origin_> < branch/_main_>|This will pull any latest work or files directly to the workspace which can result in a merge conflict|

<br>
<br>

### **git rebase** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git rebase < branch > <br> git rebase -i HEAD~1 <br> git rebase --continue <br> git rebase --skip <br> git rebase --abort|Rebase is similair to merge but instead of creating merge commits it changes all history but organizes a particular branch in a more readable fashion. <br> Interactive Rebasing also allows for correcting commit messages, dropping commits, squashing commits or fixup commit, great for before pushing your branch for review to clean it up. <br> git Rebase is seen as an alternative to merging as well as a clean up tool|

<br>
<br>

### **git tag** 
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git tag or git tag -l <br> git tag -l '* name *' <br> git tag < tag-name > or git tag -a < tag-name > <br> git tag < tag-name > < Commit-hash > or git tag -a < tag-name > < commit-hash > <br> git tag -f < tag-name > <br> git tag -d < tag-name > | git tag is used to create tags for specific moments within your repository history|

<br>
<br>

### **git show**
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git show < tag-name > <br> git show < commit-hash > or git show HEAD/~1|This shows indepth infomation on git tags and commits|

<br>
<br>

### **git reflog show**
##### [go back](#table-of-contents 'Go back to Table of Contents')

|Command|Description|
|:---|:---|
|git reflog show||

<br>
<br>

<!--
End of Document
-->