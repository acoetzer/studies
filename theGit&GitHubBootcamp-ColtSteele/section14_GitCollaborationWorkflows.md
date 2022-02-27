###### - section14_GitCollaborationWorkflows

<br>

<!-- Section Header -->

![seciotn14Header](../src/doc/section14Header.png 'Section 14 Header')

<!-- Table of Contents -->

###  **Table of Contents**

+ [The pitfalls of a centralized workflow](#the-pitfalls-of-a-centralized-workflow)
+ [The all-important feature brnach workflow](#the-all-important-feature-brnach-workflow)
    - [Merging feature branches](#merging-feature-branches)
+ [Introducing pull requests or PR](#introducing-pull-requests-or-pr)
    - [Merging pull requests with conflicts](#merging-pull-requests-with-conflicts)
+ [Branch protection rules](#branch-protection-rules)
+ [The fork & clone workflow](#the-fork--clone-workflow)

![divider](../src/doc/divider.png 'Divider')

<!-- Start of Document -->

## **The pitfalls of a centralized workflow**

<br>
<br>

* ![centralizedWorkflow](../src/centralizedWorkflow.png 'Illustation showcasing a centralized workflow')

<br>
<br>

The idea of multiple developers working on the same branch is known as a centralized workflow. 

Here multiple developers work on the same branch and this can bring along some issues. Taking a look at the above diagram one can illustrate a particular scenario. Lets say Dev 1 was the first to push to the master/main branch, Dev 2 and Dev 3 will need to pull or fetch those changes before pushing theres. They will have to resolve conflicts, merge and push again.

This is relatively small scale, though one can imagine 20 to 30 developers constantly fetching and pulling work. This will just be unproductive alongside other issues. If one developer had to ask another developer to check broken code, they will first need to push that broken code into the main branch causing issues for multiple other developers.

This is not a desired workflow.

<br>
<br>

## **The all-important feature branch workflow**

<br>
<br>

* ![featureBranchWorkflow](../src/featureBranchWorkflow.png 'Illustration showcasing a feature branch workflow')

<br>
<br>

The feature branch is a more desirable workflow, as this allows for a more controlled and organized output. Developers are not restricted by one another and can work at a more consistant pace, not to mention they can save their work separately if they ever need to help some other dev. 

There are no constrictions and worry of broken code being pushed into the main or original branch.

<br>
<br>

### **Merging feature branches**

When it comes to merging and workflows, there are a few options at hand.
* You can merge at your own free will whenever something get done, no sort of communication between members of the project.
    * _Not something you want_.
* You can have some for of communication, whether it be via email, chat or even github.
* Pull Requests

<br>
<br>

## **Introducing pull requests or PR**

Pull requests are setup so that there is a mechanism to approve or reject changes within a project. They also help facilitate discussion and feedback. Pull Requests are not found on git, this is a feature found on products such as github and bitbucket.

The way pull requests work, is that when a developer wants to merge their work into a branch typically main/master they cannot just push the work onto the main or master branch. 

They will have to push to their branch, go on github and submmit a pull request or otherwise known as a (PR) and then wait for someone to review their work and make a decision. This allows for more control and organization over projects, especially when working alongside 50 other developers.

<br>
<br>

### **Merging pull requests with conflicts**

Generally the person overseeing the pull requests would have to merge in code, and before so, they can always ask for things to be fixed before doing so.

However, the process that one takes to merge feature branch in main for example, is they would follow some steps like this.
* They would typically fetch from the repo, to make sure their files are up to date
* They would switch over to the feature branch and merge the main branch into that
    * Resolve any conflicts that may arise
* Once they happy with the outcome, they would switch over to main, and merge that branch into main.
* Commit and push changes to origin

_Side Note_: another good habbit is to not always allow a fast forward merge as sometime people want to see the history of merge commits that may have happened. 
* So a good way to avoid that is to **git merge --no-ff < branch-name >** 

<br>
<br>

## **Branch protection rules**

On github, in settings you can setup branch protection rules, so as an exmaple, no one can directly push to master or merge with master and they will need to do a PR instead. There are various rules one can go through, but that option does exist.

<br>
<br>

## **The fork & clone workflow**

<br>
<br>

* ![fork&CloneWorkflow](../src/fork&CloneWorkflow.png 'Illustration of a fork and clone workflow')

<br>
<br>

The fork and clone workflow really just involves those that want to partake in open source contributions. As one is not a collaborator  you can still be a contributor through the process of forking. Due to one not have access to the to the repo, there is no way you can push your changes or even PR without forking to the repo to your personal repository first.

The above diagram illustrates how one goes about contributing work to open source projects. That is done by forking the repo to your personl repo and then cloning the repo down to your local machine, an intersting dynamic arises when forking repos. 

Looking at the diagram you see that we cannot push to the original repo as we do not have permission to do so, however we can fetch from the repo granted we set up a different remote under the name typically upstream or original. This allows us to be up-to-date with the original repo while still be able to push to out personal repo.

Once you wish to contribute to to the original repo, you simply submit a PR on github.

<br>
<br>

<!-- End of Document -->

![endDivider](../src/doc/endDivider.png 'End of section 14')