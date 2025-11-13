# 🗂️ App Planner

Hello and welcome to my apps planner file

---

## ⬇️ Progress ⬇️

- [ 🟩 ] --> **User log in section**  
- [ 🟩 ] --> **Question Database**  
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
 
Finished on 13/11/2025, pretty similar to what I've planned
--------------------------------end of section 1-------------------------------------

### Task 2: **Question Database**  
**Deadline:** **13/11/25**  

**Description:**  
*In this section, all i need to do is create a database which will follow a universal format in order to be able to provide questions on request on the later function that I will create *

**Limitations:**  
*For now the questionsa re only going to be in 1 difficulty, since I do not have time to organise them into difficulties, nor create a sccript that can fetch different question databases. *

**Example:**
```python

questions = {
    1 : {
        "questionDesc": "Can ATC Give you the following squawk code on inital clearence? 7700",
        "QuestionOPT": "(Y)es or (N)o",
        "correctAns": "N"
    },
    2 : {
      "questionDesc": "When recieving your clearence, if you are not given an initial altitude, does it mean you can climb unrestricted?"
      "QuestionOPT": "(Y)es or (N)o"
      "correctAns": "N"
    }
}


```
And finished on 13/11/25
--------------------------------end of section 2-------------------------------------

### Task 3 + 4: **Question Fetch  &  ask function**  
**Deadline:** **13/11/25**  

**Description:**  
*In this section I need to create a code that will be able to at RANDOM choose questions from the database, and give them to the user at their need. Also I need to make sure that you cannot get the same question in a row, because that makes the practice interesting *

**Limitations:**  
*For the app testing purposes, I only have 20 questions to work with. And, due to one specification requiring questions not to be repeated, I would limit the question amount to be up to 20. This is unfortunate *

**Example:**
```
-------------------------Question 1/20------------------------

When recieving your clearence, if you are not given an initial altitude, does it mean you can climb unrestricted?

(Y)es or (N)o

Answer: 


```
And finished on 13/11/25
--------------------------------end of section 2-------------------------------------