import time
import json
import random

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

#inside of practicce
questionsCorrect = 1
questionsWrong = 1
questionNum = 3



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

    selUser = input("Username: ").strip()

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
    skipLinez(10)
    print("Welcome to the hub!")
    print("1. Start Practice")
    print("2. Source the Code")
    print("3. View Stats")
    print("4. Exit")




def questionGiver():
    global questionsCorrect
    global questionsWrong
    global currentquestion
    global questionNum
    skipLinez(2)
    time.sleep(1)
    print(f"Question {currentquestion} / {amountQuestions}")
    print(questions[questionNum]["questionDesc"])
    print(questions[questionNum]["QuestionOPT"])
    usrInput = input("Answer: ").strip().upper()

    if usrInput == questions[questionNum]["correctAns"]:
        print("Answer correct!")
        questionsCorrect += 1
        currentquestion += 1
    else:
        print("Answer incorrect!!")
        questionsWrong += 1



def menuLogic():
    global userChoice
    global quitPractice
    global amountQuestions
    global questionsCorrect
    global questionsWrong
    global currentquestion
    global database
    global questionNum
    skipLinez(1)
    userChoice = int(input(":"))
    #setting the questions enviromentS
    if userChoice == 1:
        skipLinez(5)
        amountQuestions = int(input("How many questions would you like (1 - 20): "))
        print("Starting practice. Get ready")
        for i in range(0, 3):
            print(".")
            time.sleep(1)
        skipLinez(5)
        questionsCorrect = 0
        questionsWrong = 0
        currentquestion = 1

        questionNum
        for i in range (0, amountQuestions):
            questionNum = random.randint(1, 20)
            questionGiver()
        print("Thats it!")
        print(f"Correct: {questionsCorrect}")
        print(f"Wrong: {questionsWrong}")

        percentageRight = (questionsCorrect / amountQuestions) * 100
        print(f"Your final score is: {percentageRight:.1f}%")


        database["People"][loggedinas]["stats"]["ExamsCompleted"] += 1
        if percentageRight >= 74:
            print("You passed")
            database["People"][loggedinas]["stats"]["CorrectStreak"] += 1
            database["People"][loggedinas]["stats"]["ExamsCorrect"] += 1
            
        else:
            print("You've failed")
            database["People"][loggedinas]["stats"]["CorrectStreak"] = 0
            database["People"][loggedinas]["stats"]["ExamsFailed"] += 1
            
        
        with open("database/userdatabase.json", "w") as f:
            json.dump(database, f, indent=2)
        pass
    elif userChoice == 2:
        print("https://github.com/denyakushnirchuk-glitch/AviationReadbackPractice")
        pass
    elif userChoice == 3:
        skipLinez(5)
        print(f"Printing {loggedinas}'s stats")
        print(f"Tests passed: {database["People"][loggedinas]["stats"]["ExamsCorrect"]}")
        print(f"Tests failed: {database["People"][loggedinas]["stats"]["ExamsFailed"]}")
        print(f"Correct streak: {database["People"][loggedinas]["stats"]["CorrectStreak"]}")
        pass
    elif userChoice == 4:
        quitPractice = True
        print("See you later!!")
        pass
    else:
        print("Please enter a valid choice!")








                
#The loop that triggers if user not logged in.
while not loggedin:
    appendDatabase()


while not quitPractice:
    menu()
    menuLogic()

#print(loggedinas) #debug function, keep commented unless you know what you are doing













