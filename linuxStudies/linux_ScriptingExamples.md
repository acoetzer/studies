###### - linux_ScriptingExample

## Simple Backup Program

<br>


    #!/bin/bash     --> Shebang telling your shell how to read the script

    #### Setting up Variables
    DATE=$(date +%d-%m-%Y)     --> You can make variables using command substitution
    BACKUP_STORAGE="/home/user/myBackups"     --> You can also provide a path to a variable

    #### Now writing the script or program you wish to run
    tar -cvzf $BACKUP_STORAGE/system-backup-$DATE.tar.gz /home/aspacebar/

