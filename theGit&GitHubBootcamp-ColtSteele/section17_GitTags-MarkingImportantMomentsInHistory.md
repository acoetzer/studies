###### - section17_GitTags:MarkingImportantMomentsInHistory

<br>

<!--
Section Header
-->

![section17Header](../src/doc/section17Header.png 'Section 17 Header')

<!--
Table of Contents 
-->

### Table of Contents

+ [The idea behind git tags](#the-idea-behind-git-tags)
    - [side note onsemantic versioning](#side-note-onsemantic-versioning)
+ [Viewing and Searching tags](#viewing-and-searching-tags)
+ [Comparing tags with git diff](#comparing-tags-with-git-diff)
+ [Creating lightweight tags](#creating-lightweight-tags)
+ [Creating Annotated tags](#creating-annotated-tags)
+ [Tagging previous commits](#tagging-previous-commits)
+ [Replacing tags with force](#replacing-tags-with-force)
+ [Deleting tags](#deleting-tags)
+ [IMPORTANT: Pushing tags](#important-pushing-tags)

<br>
<br>

<!--
Start of Document
-->

## The idea behind git tags

* **git tag** or **git tag -l**
The idea behind git tags is to mark important moments in history so if you wan to go back and look at how a particular piece of software was back then, you could do it. Although you can de-tach HEAD and go back. This is just another way by using marks of specific importance, usually version releases.

There are also 2 different types of git tags, this being lightweight tags and annotated tags.

* **git tag < tag-name >**
Lightweight tags are simply just a tag name and label.

* **git tag -a < tag-name >**
Annotated tags on the other hand, allows one to put meta data, name of author and many more things. This is usually the preferred way of tagging, while lightweightis generally frowned upon.

_Side Note_: Tags are placed based on current HEAD.

<br>
<br>

### side note on semantic versioning

Semantic versioning is a system that gives meaning to versioning software. In short there are 3 sets of digits seprated by a period (.). An example of this would be 2.4.1. Each set has meaning, it represents what type of work is done on said project.

* Major -- 2
* Minor -- 4
* Patch -- 1

The above mentioned, shows how each number falls under a specific catagory. From left to right you have what is known as a major update, this is when you completely overhual your product, and or make any big changes.

Minor, is for things like feature being added to the software, while patch are small fixes here and there.


<br>
<br>

## Viewing and Searching tags

* **git tag* or *git tag -l**
This is how you view git tags

* **git tag -l '* db4fdaaBeta *'**
This is how you search for specific tags

* **git show < tag-name >**
This shows you more indepth informationabout a specific tags, as some tags include meta data, author and other various things.

<br>
<br>

## Comparing tags with git diff

* **git diff < tag-name > < tag-name >**
You can also compare tag using *git diff*

<br>
<br>

## Creating lightweight tags

To create a lightweight tag, its as simple as **git tag < tag-name >**

<br>
<br>

## Creating Annotated tags

To create an annotated tag, you will type git tag -a < tag-name > and then be prompted in your editor with a place to input information, almost like git merge.

<br>
<br>

## Tagging previous commits

* **git tag < tag-name > < commit-hash >** or for annotated  **git tag -a < tag-name > < commit-hash >**
To tag a previous commit, one need to not only provide a tag-name but also the commit hash you wish to tag.

<br>
<br>

## Replacing tags with force

* **git tag -f < tag-name >**
This is a tricky one, as although this one forces a tag creation no matter if its already created before, it also kinda moves tags. So by forcing a tag that already exists, you will essentially remove the tag from the commit it was on and place it on the commit you on.

<br>
<br>

## Deleting tags

* **git tag -d < tag-name >**
To delete a tag is the same way you delete a branch with the '-d' flag.

<br>
<br>

## IMPORTANT: Pushing tags

* **git push < tag-name >** or for all **git push --tags**
The most important thing to remember is to push your tags, when pushing your commits, it does not include your tags, so make  sure to push tags as well.

<br>
<br>

<!--
End of Document
-->