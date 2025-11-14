import time
import json

#importing questions
from questions import questions


#setting variables for the functions to function nicely
loggedin = False
selUser = ""
loggedinas = ""
userChoice = ""
quitPractice = False
amountQuestions = 1
currentquestion = 1

with open("database/userdatabase.json", "r") as file:
    database = json.load(file)

#global function for spacings
def skipLinez(amount):
    for _ in range(amount):
        print("\n")


#If the mainloop fails to find a login info for a given user, it transfers it into this registerring portal where you are able to add a user.
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
    global loggedinas
    print("Please log in as one of the users in database:")

    x = 1
    for i in database["People"]:
      print(f"{x}. {i}")
      x += 1

    selUser = input("Username: ")

    if selUser in database["People"]:
        password = str(input("Password: "))
        if password == database["People"][selUser]["password"]:
            print(f"Login successful! Welcome back, {selUser}. Transferring to student portal now.")
            loggedin = True
            loggedinas = selUser
        else:
            print("Incorrect password. Access denied, please try again")
            time.sleep(2)
            skipLinez(3)
    elif selUser not in database["People"]:
        print("Transferring to registration portal...")
        registerUser()
        with open("database/userdatabase.json", "w") as file:
            json.dump(database, file, indent=2)


#INSIDE OF THE HUB--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def menu():
    time.sleep(2)
    skipLinez(10)
    print("Welcome to the hub!")
    print("1. Start Practice")
    print("2. Source the Code")
    print("3. Exit")

def questionGiver():
    global currentquestion
    global amountQuestions

    currentquestion = amountQuestions - amountQuestions + 1

    print(f"Question {currentquestion} of {amountQuestions}")

def menuLogic():
    global userChoice
    global quitPractice
    global amountQuestions
    skipLinez(1)
    userChoice = input(":")
    #setting the questions enviromentS
    if input == "1":
        skipLinez(5)
        amountQuestions = input("How many questions would you like (1 - 20): ")
        print("Starting practice. Get ready")
        for i in range(0, 3):
            print(".")
            time.sleep(1)
        skipLinez(5)




                
#The loop that triggers if user not logged in.
while not loggedin:
    appendDatabase()

menu()
menuLogic()

time.sleep(2)
#print(loggedinas) #debug function, keep commented unless you know what you are doing













