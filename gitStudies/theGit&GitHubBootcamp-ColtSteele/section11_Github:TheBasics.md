###### - section11_Github:TheBasics

<br>

<!-- Table of Contents -->

### Table of Contents
- [What does github do for us?](#what-does-github-do-for-us)
    - [Why you should use Github](#why-you-should-use-github)
- [Cloning Github repos with git clone](#cloning-github-repos-with-git-clone)
    - [Cloning non-github repos](#cloning-non-github-repos)
- [Github Setup: SSH Config](#github-setup-ssh-config)
- [Creating our first Github repo](#creating-our-first-github-repo)
- [A crash course in git remotes](#a-crash-course-in-git-remotes)
    - [git remote commands](#git-remote-commands)
    - [Adding remotes to your local repo](#adding-remotes-to-your-local-repo)
- [Introducing git push](#introducing-git-push)
    - [git push command](#git-push-command)
    - [A closer look at git push](#a-closer-look-at-git-push)
    - [What does git push -u mean?](#what-does-git-push--u-mean)
    - [Deleting a remote branch](#deleting-a-remote-branch)
- [Another github Workflow: Cloning First](#another-github-workflow-cloning-first)
- [Main & Master: Github Default Branches](#main--master-github-default-branches)    

<br>
<br>

# What does github do for us?
* Github allows us to not only collaborate, even though that is a big part of it, it gives you exposure to other developers.
    * When looking for a job, potential bosses, could look at your github page to see your work, or collaborations.
    * Also a great way to back up your work, so you can work from multiple devices.

### Why you should use Github
* This, again, github gives you exposure, gives you insight as to how projects are made and allows you to collaborate with other developers 
    * Not to mention a way to backup your work and Work from multiple different devices.
* It can potentially land you a job.

<br>

# Cloning Github repos with git clone
* When it comes to cloning repositories found in the cloud such as [github.com](https://github.com), You can use the **git clone < url >** command.
    * You are allowed to clone anything you can see, generally private repo's are not visible to the public. Again anything visible to 'clonable'
    * What **git clone** does is essentially copy the repo that is in the cloud to your computer. 
    * You can then make changes how you want, as it only affect your local version.
        * Just a side note, no one can clone your work, delete its contents and push it back to your repository, without your permission to do so.

### Cloning non-github repos
* Yes it is possible to clone from non-github repositories, however, github is the most popular.

<br>

# Github Setup: SSH Config
* To setup a secure shell, have a look at [git commands](../git_CommandList.md#setting-up-ssh-keys-for-git)

<br>

# Creating our first Github repo
* When it comes to creating repo's, there are 2 workflows one can follow
    * Connecting an existing **local** repo to github [adding remotes](#a-crash-course-in-git-remotes)
        * _Side note: when connecting a local repo to github, make sure to make an empty repo on github first and then add the remote to your local repo_
    * Starting a new repo on gitgub first or otherwise known as [cloning first](#another-github-workflow-cloning-first)

<br>

# A crash course in git remotes
### git remote commands
* **git remote** 
    * This should display the remote name, which should be origin, unless changed
* **git remote -v**
    * This should display the url connected with the repo as well as the name.
        * an example of this should look like this
            * origin	https://github.co/acoetzer/some-repo.git (fetch)
            * origin	https://github.co/acoetzer/some-repo.git (push)

### Adding remotes to your local repo
* When it comes to adding your local repo to github, use
    * **git remote add < name > < url >**
        * **git remote add origin https://github.co/acoetzer/some-repo.git** _as an example_.
    * You will notice the name origin, you can name it whatever you want, but standard and best practice is to leave it as origin.
        * Again, this is just naming the remote.
* after doing so, you can check the remote with **git remote -v** and you should see 2 enteries for pull and fetch
* Side note, make sure to [push](#introducing-git-push) any changes.

<br>

# Introducing git push
* git push is used to push work from your local repository to your remote repository such as Github.
    * However, one needs to specify certain details before it works.
### git push command
* **git push**
    * **git push** is a shortcut for **git push < remote-name > < branch-name >**
        * As an example: **_git push origin master/main_**
        * _However to be able to use the git push shortcut command, you will need to set an upstream for where the local branch will push to._
* **git push < remote-name > < branch-name >**
    * An example: git push origin master/main
* **git push -u < remote-name > < branch-name >** or **git push --set-upstream < remote-name > < branch-name >**
    * An example: **git push -u origin master/main** or **git push --set-upstream origin master/main**
    * After this command you should be able to use **git push** by itself


### A closer look at git push
* Taking a closer look at **git push**, you can push another branch to master/main by separating both branch names with a **:/colon**. As an example if you had a branch named cat, you could push the cat brach to origin/master branch. 
    * An exmaple: **git push origin cat:master**
        * You can go as far as linking or upstreaming the cat branch to master as well, using **git push -u origin cat:master**

### What does git push -u mean?
* **git push -u** or more specifically the **-u** stands for upstream.
* An upstream just connects your local branch to a remote origin/branch, so you dont always need to specify where to push to, ie **git push origin master**
* **git push -u < remote-name > < branch-name >** or **git push --set-upstream < remote-name > < branch-name >**
    * An example: **git push -u origin master/main** or **git push --set-upstream origin master/main**
    * After this command you should be able to use **git push** shortcut.

### Deleting a remote branch
* To delete a remote branch use git push --delete < remote > < branch-name for deletion >
    * As an example: **git push --delete origin master**
* we will discuss why you would want to delete your remote from terminal rather than github [here](#main--master-github-default-branches)

<br>

# Another github Workflow: Cloning First
* Another method for a repo workflow, is to just make the repo on github first and then clone it to your machine
    * github gives instructions to follow, though it does come with remotes already included.

<br>

# Main & Master: Github Default Branches
* When it comes to main or master, Github is pushes for main, more and more people are using main due to trying to avoid offensive language apparently. 
    * However Git still uses master as its default. 
* So because main is becoming more and more popular, you are able to rename your branch and these are the steps to follow:
    1. Rename your local branch, using the **git branch -m/M < new-name >** _(capital M is just to force the rename, incase another branch already has that name also remember to be on the branch to rename it)_
    2. You can either set a upstream immediately, or can **git push origin < new-branch >** and set it later after deleting the previous branch.
    3. Head over to github and then make the new **main** branch as example the default instead of master.
    4. Then back on your terminal you can run **git branch -a** to list all branches locally and remote
    5. You will see **remotes/origin/master** 
    6. Now delete origin/master using **git push --delete origin master** command
    7. It will prompt for login details, and once done, it should be deleted both on github and locally.
* I would recommend this, as deleting from github before local, can result in **git push --delete origin master** error.
    * If this is the case, you can run another command **git remote show origin**
    * Somewhere in there, you will notice origin/master has gone stale and use git remote prune to remove it.

