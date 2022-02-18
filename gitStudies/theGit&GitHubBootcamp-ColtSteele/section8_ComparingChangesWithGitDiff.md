###### ____section8_ComparingChangesWithGitDiff

<br>

<!-- Table of Contents  -->

### Table of Contents
- [Introducing the git diff command](#introducing-the-git-diff-command)
- [A guide to reading git diff's](#a-guide-to-reading-git-diffs)
    - [Breaking it down](#breaking-it-down)
    - [Chunk header breakdown](#chunk-header-breakdown)
    - [General illustration of how git diff works](#general-illustration-of-how-git-diff-works)
- [Viewing unstaged changes](#viewing-unstaged-changes)
- [Viewing Working directory changes](#viewing-working-directory-changes)
- [Viewing staged changes](#viewing-staged-changes)
- [Diffing specific files](#diffing-specific-files)
- [Comparing changes across branches](#comparing-changes-across-branches)
- [Comparing changes across commits](#comparing-changes-across-commits)

<br>
<br>

# **Introducing the git diff command**
* The **git diff** command is all about showing changes within git.
    * These changes can range from branches, files, the working directory, to HEAD, staged, cached to even commits.
    * You can go as far as comparing specific files, branches and even commits against one another, instead of viewing all changes.
* You get different variations of the git diff command
    * **git diff** 
        > Viewing the working directory and files that have not been staged.
    * **git diff HEAD | git dif HEAD < fileame  >**
        > This views everything on that HEAD, Whether it be working directory, staged or unstaged. It shows all files, including multiple files.
    * **git diff --staged | git diff --staged < filename  >**
        > This only views staged files, all or specific.
    * **git diff --cached**
        > This only views cached files
    * **git diff branch1..branch2**
        > You can compare 2 branch's with one another.
    * **git diff commit1..commit2**
        > The same for 2 different commit (hash values)

<br>

# **A guide to reading git diff's**
### **Breaking it down**
<br>

![gitDiffChunkBreakdown](./src/gitDiffChunkBreakdown.png 'An illustration of how to read a giff chunk')

* Taking a look at the above illustration, this is what one could see when looking at the git diff command
* Breaking it down from top to bottom we have
    * **Compared files**, This tells you which files are being compared, though usually its the same files. 
            * You can also tell the same file apart and there is a letter beside it, in this case (**a**/_example.txt_) & (**b**/_example.txt_).
    * **File Metadata**, This shows you the hash of each file, hece how its able to show 2 version of the same file.
        * _Not that you will really every use it, but it is there_.
    * **Markers**, Indicate by the symbols **---** **+++** which document is old and newer. 
        * Although older and newer is not always the case, but in general it shows what was and will be.
    * **Chunk Header**, This shows a wide array of information which can be seen [here](#chunk-header-breakdown 'An illustration of the chunk header'), however in short it shows the file, line number, and changed line.
    * **Chunk**, This section is considered the Chunk, and holds the all the information such as chunk header, leading and trailing lines, including the said alteration between files.

<br>

### **Chunk header breakdown**

<br>

![gitDiffChunkHeaderBreakdown](./src/gitDiffChunkHeaderBreakdown.png 'A breakdown of the chunk header')

<br>

### **General illustration of how git diff works**

<br>

![gitDiffOverall](./src/gitDiffOverall.png 'An overall illustration of how git diff works')

* Above, you can see depending  where you are in your document, your results can output differently, so its important to remember there are always 3 trailing and leading lines.

<br>

# **Viewing unstaged changes**
* **git diff**
    * With only **git diff** you can view your working directory and staging files, though not the staged files

<br>

# **Viewing Working directory changes**
* **git diff HEAD**
    * **git diff HEAD** shows all files including staged, unstaged, working directory.
        * This includes multiple files
    * You can also use **git diff HEAD < filename  >** to view specific files.

<br>

# **Viewing staged changes**
* **git diff --staged**
    * **git diff --staged**, views all staged files.
* **git diff --staged < filename  >**, you can also view specific files.

<br>

# **Diffing specific files**
* **git diff HEAD < filename  >**
*  **git diff --staged < filename  >**

<br>

# **Comparing changes across branches**
* **git diff branch1..branch2** or **git diff branch1 branch2**
    * Note you separate the branch-names with 2 .. or just a space 

<br>

# **Comparing changes across commits**
* **git diff commit1..commit2** or **git diff commit1 commit2**
    * note, once again you can separate the commits by 2 .. or a space
