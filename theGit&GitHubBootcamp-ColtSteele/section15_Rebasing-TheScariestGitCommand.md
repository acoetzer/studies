###### -section15_Rebasing:TheScariestGitCommand

<br>

<!-- Section Header -->

![section15Header](./src/doc/section15Header.png 'Section 15 Header')

<!-- Table of Contents -->

### Table of Contents

+ [Why is Rebasing Scary? is it?](#why-is-rebasing-scary-is-it)
    - [Comparing merging and rebasing](#comparing-merging-and-rebasing)
+ [The Golden Rule: When NOT torebase](#the-golden-rule-when-not-to-rebase)

![divider](./src/doc/divider.png 'Divider')

<!-- Start of Document -->

## Why is Rebasing Scary? is it?

<br>
<br>

![](./src/gitRebasingOverview.png 'An illustration showing the ')

<br>
<br>

* git rebase < branch >
Rebasing has it's divded userbase, its scary as it can be quiet damaging to projects as it rewrites history. Rebasing is used as an alternative to merging for some people. The history it re-writes, ranges from placement of commit, to completely new commit hashes. 

You can see in the hands of a beginner, this can cause a lot of headaches. Therefor it is scary if you dont know how to use it. Though if a person knows how to use it, it can be quiet useful.

<br>
<br>

### Comparing merging and rebasing

Although rebasing is seen an alternative to merging it is also quiet different as it reorganises the entire branch history, pushing your branches commits to the tip of whatever branch, typically master, While master is behind as seen in the above illustration. 

So although it merging in a branch, it will also re-write history and re-arrange commits in this fashion.

<br>
<br>

## The Golden Rule: When NOT to rebase

The single most important rule when it comes to rebasing is that **NEVER** rebase a commits that others have as it will result in team members not having the same commits as you, and this can cause a lot of issues.

<br>
<br>

## Handling Conflicts & Rebasing

So when it comes to rebase conflicts, it sort of the same as merging however as rebasing re-arranges the commits and history, as we mentioned, the branch being merged in get placed at the back while your branch gets placed on the tip of that branch. If there is a conflict it will postpone the rebasing and prompt you to fix the conflicts.

You will the add the modified changes to the staging area, but the key destinction between merging and rebasing is that you do not do a normal commit, but you are given 3 options, as follows:
* git rebase --continue
* git rebase --skip
* git rebase --abort

Though self explanatory, this is the step that needs to be followed.

<br>
<br>

<!-- End of Document -->

![endDivider](./src/doc/endDivider.png 'End of Document')