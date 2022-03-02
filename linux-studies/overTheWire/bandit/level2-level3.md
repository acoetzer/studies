#### level2-3_Objective

* The password for the next level is stored in a file called spaces in this filename located in the home directory.

#### Result

|**_Type_**|**_Goal_**|
|:--:|:--:|
|Password|UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK|

#### Explanation & Conclusion

* we ran the ls command and found a file (spaces in this filename)which has spaces between its name, when trying to cat spaces in this filename, its essentially looking for 4 files : 
    * spaces
    * in
    * this
    * filename
* This resulting in a error.
* However if you use quotation marks as follows : cat "space in this filename" it treats it as one single string/name.