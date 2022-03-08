#### level6-7_Objective

* The password for the next level is stored somewhere on the server and has all of the following properties:
    * owned by user bandit7
    * owned by group bandit6
    * 33 bytes in size


#### Result

|**_Type_**|**_Goal_**|
|:--:|:--:|
|Password|HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs|

#### Explanation & Conclusion

* find / -user bandit7 -group bandit6 -size 33c -type f