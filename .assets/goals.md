# 🗂️ App Planner

Hello and welcome to my apps planner file

---

## ⬇️ Progress ⬇️

- [ 🟥 ] --> **User log in section**  
- [ 🟥 ] --> **Question Database**  
- [ 🟥 ] --> **Database Fetch function**  
- [ 🟥 ] --> **Question asking system**  
- [ 🟥 ] --> **Random Selection Code**  
- [ 🟥 ] --> **QOL Improvements**  
- [ 🟥 ] --> **TEMP files**  
- [ 🟥 ] --> **Rich UI**  
- [ 🟥 ] --> **Install script**

---

## ⌚ Timeline ⌚

### Task 1: **User Log In Section**  
**Deadline:** **09/11/25**  

**Description:**  
*In this section, we need to create a user log in system, which will allow different users on a single machine to use the app, without messing anyones scores. We will do this by making different entries into the main JSON Database, which will contain the userdata that is needed to upkeep the profile.*

**Limitations:**  
*For now, the database is going to be local and only accesible on the computer with the main JSON database. I will consider making it a server side thing. Also, since the lack of time, I will not make encrypted passwords. IT is in TODO list for later date though.*

**Example:**
```json
{
  "People": {
    "Denya": {
      "password": "ILikePlenz",
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

```

--------------------------------end of section 1-------------------------------------