#### level1-2_Objective

* The password for the next level is stored in a file called - located in the home directory

#### Result

|**_Type_**|**_Goal_**|
|:--:|:--:|
|Password|CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9|

#### Explanation & Conclusion

* We ran the ls command to find a "-" dashed file, we couldnt cat the dashed file as a dash at the end of a command is considered a popular convention for stdin or stdout, which means when trying to cat - we essentially saying cat stdin/stdout.
* In order to correct this, we need to input the file path as an argument to the cat command as follows : cat ./-