import os
import pwd
#import crypt
#import getpass
import subprocess

def callExplicitly(command):
    print("Calling",end="")
    for i in command:
        print(" "+i,end="")
    print("...")

    subprocess.call(command)

#https://stackoverflow.com/questions/842059/is-there-a-portable-way-to-get-the-current-username-in-python
def getUsername():
    return pwd.getpwuid(os.getuid())[0]

def createUser(userName, inWheelGroup):
    print(" -= Here's the part where I'd make the user",userName,"=-")
    print(" -= In wheel group:",inWheelGroup,"=-")

def removeUserFromWheelGroup(userName):
    print(" -= Here's the part where I'd remove",userName,"from the wheel group =-")

def inputValidUser():
    print("Maybe I'll add opinions to this later. If I have to.")
    return input("Enter a valid username. I'll just trust you on it...\n(str)? ")

while True:
    print(
        "Enter mode:\n"+
        "1) Personal use. Create \"work user\" for current user\n"+
        "2) Workplace use. Initialize multiple users with work users"
    )
    try:
        choice = int(input("(int)? "))
        if choice >= 1 and choice <= 2:
            break
    except ValueError:
        pass
    print("Please enter a valid choice.")


if choice == 1:
    createUser(getUsername() + "-worker", False)

    while True:
        try:
            print("Do you wish to remove yourself from the wheel group?")
            choice = input("If yes, root or worker access would require su.\n(y/N)? ").lower()[0]
            
            if choice == 'y' or choice == 'n':
                break
            else: print("Please enter a valid choice.")
        except IndexError:
            choice = 'n'
            break
    if choice == 'y':
        removeUserFromWheelGroup(getUsername())

elif choice == 2:
    while True:
        try:
            amount = int(input("Enter number of users to make.\n(int)? "))
            break
        except ValueError:
            print("Please enter an integer.")
    
    newUsers = []
    for i in range(amount):
        newUsers.append(inputValidUser())
    
    while True:
        try:
            print("Should these users be in the wheel group?")
            choice = input("If no, root or worker access would require su.\n(y/N)? ").lower()[0]
            
            if choice == 'y' or choice == 'n':
                break
            else: print("Please enter a valid choice.")
        except IndexError:
            choice = 'n'
            break
    
    for user in newUsers:
        createUser(user, False)
        createUser(user + "-worker", False)


else:
    print("How'd you get here?")