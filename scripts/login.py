database = {
  "People": {
    "Denya": {
      "password": "123456",
      "stats": {
        "ExamsCompleted": 1200,
        "ExamsCorrect": 1100,
        "ExamsFailed": 100,
        "CorrectStreak": 80,
        "DateJoined": "09/11/25"
      }
    },

    "Alex": {
        "password": "NoobPlenz",
        "stats": {
            "ExamesCompleted": 100000,
            "ExamsCorect": 1,
            "ExamsFailed": 99999,
            "CorrectStreak": 1,
            "DateJoined": "01/01/0001"
        }
    }
  }
}

print("Users in database:")

for i in database["People"]:
    x = 1
    print(f"{x}. {i}")
    x += 1


print("Please select a user to login as:")

selUser = input("Username: ")

if selUser in database["People"]:
    password = input("Password: ")
    if password == database["People"][selUser]["password"]:
        print(f"Login successful! Welcome back, {selUser}.")
    else:
        print("Incorrect password. Access denied.")



