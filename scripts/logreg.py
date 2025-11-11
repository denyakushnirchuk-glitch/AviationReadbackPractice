import time
import json

loggedin = False
selUser = ""

with open("database/userdatabase.json", "r") as file:
    database = json.load(file)

#just a function to help with uhh spacing and code decluttering
def skipLinez(amount):
    for _ in range(amount):
        print("\n")


def registerUser():
    print(f"Hello Newbie, welcome to the registration portal!")
    username = input("Enter your login: (email if possible):  ")
    password = input("Enter your password: ")
    database["People"][username] = {
        "password": password,
        "stats": {
            "ExamsCompleted": 0,
            "ExamsCorrect": 0,
            "ExamsFailed": 0,
            "CorrectStreak": 0,
            "DateJoined": time.strftime("%m/%d/%y")
        }
    }
    
# main loop function, basically handles the login and registering system. 
def appendDatabase():
    global loggedin
    print("Please log in as one of the users in database:")


    for i in database["People"]:
      x = 1
      print(f"{x}. {i}")
      x += 1

    selUser = input("Username: ")

    if selUser in database["People"]:
        password = str(input("Password: "))
        if password == database["People"][selUser]["password"]:
            print(f"Login successful! Welcome back, {selUser}. Transferring to student portal now.")
            loggedin = True
        else:
            print("Incorrect password. Access denied, please try again")
            time.sleep(2)
            skipLinez(3)
    elif selUser not in database["People"]:
        print("Transferring to registration portal...")
        registerUser()
        with open("database/userdatabase.json", "w") as file:
            json.dump(database, file, indent=2)
                    


while not loggedin:
    appendDatabase()









