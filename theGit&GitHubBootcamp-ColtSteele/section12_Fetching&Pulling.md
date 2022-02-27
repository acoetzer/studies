###### - section12_Fetching&Pulling

<br>

<!-- Section Header-->

![section12Header](./src/doc/section12Header.png 'Section 12 Header')

<!-- Table of Contents -->

### **Table of Contents**

+ [Remote Tracking Branches: WTF are they?](#remote-tracking-branches-wtf-are-they)
+ [Checking out remote tracking branches](#checking-out-remote-tracking-branches)
+ [Working with remote branches](#working-with-remote-branches)
+ [Git Fetch: The Basics](#git-fetch-the-basics)
+ [Git Pull: The Basics](#git-pull-the-basics)
    - [Git Pull & Merge conflicts](#git-pull--merge-conflicts)
    - [A shorter syntax for Git Pull](#a-shorter-syntax-for-git-pull)
+ [git fetch vs git pull](#git-fetch-vs-git-pull)

![divider](./src/doc/divider.png 'Divider')

<!-- Start of Document -->

## **Remote Tracking Branches: WTF are they?**

<br>
<br>

![remoteTrackingBrancha](./src/remoteTrackingBrancha.png 'illustration of a remote tracking branch')

<br>
<br>

Remote tracking branches, are branches located on your remote repo as well as locally, however slightly different. When cloning a repo from a remote repository, you will see something along the line origin/master when running **git status** command.

This is referred to as a _remote tracking branch_, it is essentially referencing the most recent state of whatever branch on the remote. Looking at the illustration above you can see the local repo has the master, while there is another called origin/master.

<br>
<br>

![remoteTrackingBranchb](./src/remoteTrackingBranchb.png 'Illustration demonstrating the local does not affect the remote branch unless pushed')

<br>
<br>

Taking a look at the above image, you can see that even when you commit work on your local repo the remote tracking branch or _origin/master_ will continue to reference what it believes to be latest commit to the remote However once you push the changes to the remote repo, _origin/master_ will be at the current state as your local repo.

_side note: git does not send requests periodically to see if the remote repo's are up to date, this has to be done manually with a command called [git fetch or git fetch < remote > < branch >](#git-fetch-the-basics)_

<br>
<br>

## **Checking out remote tracking branches**

As the _remote tracking branch_ or _origin/main_ or _< remote >/< branch >_ tracks the last known remote commit, when making commits locally it will not affect the remote reference, unless pushed. This means, You can checkout the _< remote >/< branch >_ or _origin/main_ (as an example), as it hasn't moved since being cloned to the local machine, so that one can see what changes were like before moving forward.

The way you do is this with **git checkout origin/main**, this ofcourse will place you in de-tached HEAD state and time travel you back to where _origin/master_

<br>
<br>

## **Working with remote branches**

<br>
<br>

![remoteTrackingBranchConnection](./src/remoteTrackingBranchConnection.png 'Illustration showing remote tracking branch connection after cloning')

<br>
<br>

After cloning a repo, you will notice only one 1 branch shows up. Typically the _master or main_, though the repo shows no other branches, this could be if there were no other branches, however if you know there are multiple branches, you still would not see them. Why? If you run **git branch**, there will only be the repo's default branch, commonly main or master as mentioned before.

_Side note: If you run **git branch -r** or **git branch -a** you should be able to see the remotes as well._

 Why does this happen?, well by default when cloning a branch from a remote such as github, it automatically configures the local branch whether it be master or main to track the remote equivalent branch. However the other branches that are remote, need to be set up where there is a local branch and it needs to be tracked.

Thankfully **git switch < remote-branch-name >** will automatically create that branch locally and set it up to track with its remote branch-name. _That is if git detects the same name between them._ However you can do this manually with **git checkout --track < remote >/< branch >** or as an example **_git checkout --track origin/master_**

<br>
<br>

## **Git Fetch & Pull Diagram**

<br>
<br>

![gitFetch&PullDiagram](./src/gitFetch&PullDiagram.png 'Diagram showing the difference between Fetch and Pull')

<br>
<br>

## **Git Fetch: The Basics**

git fetch is a way for a user to _check or collect or in other words fetch_ newer work from a remote location

* **git fetch < remote >** or **git fetch** fetches the entire repo
    * **git fetch < remote > < branch >** fetches only a spcific branch
Taking a look at the diagram above, you see **git fetch** only fetches work from the remote repo and places it into the local repo, without merging or destroying workspace files. From there you can checkout what changes have been made and then decide to merge or pull.

<br>
<br>

## **Git Pull: The Basics**

**git pull** is like **git fetch**, however instead of it just going into the local repo, it will merge into your workspace as well. 
* git pull < remote > < branch > 
    * _git pull = git fetch + git merge_
git pull can result in merge conflicts

<br>
<br>

### Git Pull & Merge conflicts

Most times pulling can result in merge conflicts when others are working on the same file. Therefor in best practice its best to git fetch than to git pull.Fixing conflicts that arise from git pull, is the same way as fixing issues, when merging.

<br>
<br>

### **A shorter syntax for Git Pull**

A shorter syntax is **git pull**, git pull will default to the default origin, as well as the default branch to whatever tracking connection is configured for the current branch.

<br>
<br>

## **git fetch vs git pull**

|**git fetch**|git pull|
|:---|:---|
|Gets changes from remote branch(es) <br> Updates the remote-tracking branches with the new changes <br> Does not merge changes onto your current head branch <br> Safe to do at anytime|Gets changes from remote branch(es) <br> Updates the current branch with the new changes, merging them in <br> Can result in merge conflicts <br> Not recommended if you have uncommitted changes!|

<br>
<br>

<!-- End of Document -->

![endDivider](./src/doc/endDivider.png 'End of Document')