import os
#import pwd
#import crypt
#import getpass
import subprocess

while True:
    print(
        "Enter mode:\n"+
        "1) Create \"work user\" for current user\n"+
        "2) Initialize multiple users with work users (for loop)"
    )
    try:
        choice = int(input("? "))
        if choice >= 1 and choice <= 2:
            break
    except ValueError:
        pass
    print("Please enter a valid choice.")

subprocess.call(['sudo', 'fish'])