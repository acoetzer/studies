#### level4-5_Objective

* The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

#### Result

|**_Type_**|**_Goal_**|
|:--:|:--:|
|Password|koReBOKuIDDepwhWk7jZC0RTdopnAYKh|

#### Explanation & Conclusion

* we used the cd command to change directories into the inhere folder.
* we then ran the ls command to see the contents of the folder and we saw a bunch of files starting with a dash.
* according to the clue, one of the files is human readable. 
* using the file command we then check all files within the directory but making sure to provide a path as the file names start with a dash as follows : find ./-file*
* we used the * wildcard to run this command on all files instead of going 1 by 1.