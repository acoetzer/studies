#### level5-6_Objective

* The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
    * human-readable
    * 1033 bytes in size
    * not executable


#### Result

|**_Type_**|**_Goal_**|
|:--:|:--:|
|Password|DXjZPULLxYr17uwoI01bNLQbtFemEgo7|

#### Explanation & Conclusion

* We ran the ls command to find the inhere folder
* We then cd'd into the inhere folder
* When using ls -laR you see an array of multiple folders and files.
* Based on the clue and using the find command with the option -size n and c for bytes, we searched for a file as follows : find -size 1033c
* This resulting in one hidden file being showed
* we then used the cat command as follows : cat ./maybehere07/.file2