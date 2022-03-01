###### -section16_CleaningUpHistoryWithInteractiveRebase

<br>

<!--
Section Header
-->

![section16Header](../src/doc/section16Header.png 'Section 16 Header')

<!--
Table of Contents 
-->

### Table of Contents

+ [Introducing Interactive Rebase](#introducing-interactive-rebase)

<br>
<br>

<!--
Start of Document
-->

## Introducing Interactive Rebase

* **git rebase -i HEAD~1** 
    * _Side Note_: It's important to note, while **git checkout HEAD~1** ref the HEAD Commit and Whatever commit after that. In interactinve rebasing, it references from HEAD to said number.

Interactive rebasing is used as a tool to clean up branch history. There are some options to take note of:

1. Pick
    * Use current commit
2. Reword
    * use commit, but edit only commit message
3. Fixup
    * fixup is like squash but instead of keeping the commit as history, it removes it, therefor fixup combines commits to previous commits. Almost like **git commit --amend**
4. Drop
    * Removes commits and its contents.

Its important to note that it will subsequently redo history as well.

<br>
<br>

<!--
End of Document
-->