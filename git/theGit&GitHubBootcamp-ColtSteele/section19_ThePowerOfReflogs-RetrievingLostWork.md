###### - section19_ThePowerOfReflogs-RetrievingLostWork

<br>

<!--
Section Header
-->

![section19header](../../src/git/doc/section19Header.png 'Section 19 Header')

<!--
Table of Contents
-->

### Table of Contents
+ [Introducing reflogs](#)
+ [The limitations of reflogs](#)
+ [Passing reflog references around](#)
+ [Time-based reflog qualifiers](#)
+ [Rescuing losts commits with reflog](#)
    - [Undoing a rebase with reflog](#)

<br>
<br>

<!--
Start of Document
-->

## Introducing reflogs

* **git reflog show** or **git reflog show HEAD**
Reflogs is basically a log the git keeps locally on your machine. You can find the logs file under the .git folder and then logs/heads/. It also house other branch's, however the command will refer to the current branch you are on. 

<br>
<br>

## The limitations of reflogs

The limitation of reflog is that it is local based. This meaning the logs do not upload to the repo and is only meant for your machine, so you will only see the changes made on your machine.

Also reflog or the logs, expire after 90 days so they dont last forever.

<br>
<br>

## Passing reflog references around

* name@{qualifier}
When referencing reflog we use **HEAD@{2}**, its not the same as **HEAD~2** (This referencing a commit and its parent commit). **HEAD@{2}** is referencing 2 entries ago in the log file. You can for example be on the same commit 2 entries ago.

<br>
<br>

## Time-based reflog qualifiers

* **git reflog main@{one.week.ago**
* **git checkout bugfix@{2.days.ago**
* **git diff main@{0} main@{yesterday}**
Every entry in reflog has a time stamp. So you can essentially place time in your reference for various commands.

<br>
<br>

## Rescuing losts commits with reflog

You can essentially use reflog to go back to commits that were deleted by git reset as an example. This happens because although the commits are deleted due to using something like git reset. 
* **Side Note**: It no longer shows up in your git log history as git log is a public log of commits, whereas git reflog is a private workspace log.

That being said, git reflog will still keep a history of that commit even though its supposed to be deleted. Better yet, you can still reset/restore and revert back to that commit.

<br>
<br>

### Undoing a rebase with reflog

Following what was said previously, you can restore from a rebase.

<!--
End of Document
-->