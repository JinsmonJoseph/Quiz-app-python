import sqlite3
import pandas as pd
#Creating a database for tables
def create_quizDB():
    con = sqlite3.connect("QuizInfo.db")
    cur=con.cursor()
    questions=[
    (1,"In the following options which are python libraries which are used for data analysis and scientific computations?"),
    (2,"Which can be an Identifier among them in Python?"),
    (3, "How can we run a Python script file named hello.py from the command line?"),
    (4, "Which of the following is TRUE about Python?"),
    (5, "A Python script file has ________ as its file extension."),
    (6, "What values do True and False represent?"),
    (7, "How can we convert the following string variable into an integer?"),
    (8, "Which of the following is FALSE about variables?"),
    (9, "What is the output of the following code? print (bool(1), bool(0))"),
    (10, "Which of the following is TRUE about variables in Python?"),
    ]

    answers=[
    (101, 1, "Numpy", 0),
    (102, 1, "Scipy", 0),
    (103, 1, "Pandas", 0),
    (104, 1, "All the above", 1),
    (105, 2, "1abc", 0),
    (106, 2, "$12a", 0),
    (107, 2, "_xy1", 1),
    (108, 2, "@python", 0),
    (109, 3, "python hello", 0),
    (110, 3, "python hello.py", 1),
    (111, 3, "hello.py", 0),
    (112, 3, "py hello", 0),
    (113, 4, "Python scripts only run on Windows Operating System.", 0),
    (114, 4, "Python scripts end with .python", 0),
    (115, 4, "None of these", 1),
    (116, 4, "In Python, the statements ends with a semi-colon.", 0),
    (117, 5, "pi", 0),
    (118, 5, "py", 1),
    (119, 5, "python", 0),
    (120, 5, "pyth", 0),
    (121, 6, "0 - True, 1 - False", 0),
    (122, 6, "1 - True, 0 - False", 1),
    (123, 6, "1 - True, -1 - False", 0),
    (124, 6, "None of these", 0),
    (125, 7, "By using the integer() function.", 0),
    (126, 7, "A string variable cannot be converted to an integer.", 0),
    (127, 7, "By using the float() function.", 0),
    (128, 7, "By using the int() function.", 1),
    (129, 8, "Variables must begin with a letter.", 0),
    (130, 8, "All of these are TRUE.", 0),
    (131, 8, "Variables can contain letters, numbers, and underscores.", 0),
    (132, 8, "Variables can be one of the reserved Python keywords like def, elif etc.", 1),
    (133, 9, "True False", 1),
    (134, 9, "1 0", 0),
    (135, 9, "False True", 0),
    (136, 9, "1,0", 0),
    (137, 10, "The kind of data pointed by the variable can be changed later.", 0),
    (138, 10, "Variables can change in value.", 0),
    (139, 10, "There is no need to declare the type of variable.", 0),
    (140, 10, "All of these are correct.", 1),
    (141, 11, "Answer1", 0),
    (142, 11, "Answer2", 0),
    (143, 11, "Answer3", 1),
    (144, 11, "Answer4", 0),
    ]
    try:
        cur.execute("create table Questions (qid,question)")
        cur.execute("create table Answers (aid,qid,answer,rightAns)")
        cur.executemany("insert into Questions values (?,?)" ,questions)
        cur.executemany("insert into Answers values (?,?,?,?)" ,answers)
    except:
        cur.executemany("insert into Questions values (?,?)" ,questions)
        cur.executemany("insert into Answers values (?,?,?,?)" ,answers)
    print("Database created succesfully")
    con.commit()
    con.close()
def get_question(question_id):
    question_id=str(question_id)
    con = sqlite3.connect('QuizInfo.db')
    cur=con.cursor()
    cur.execute('SELECT * FROM Questions WHERE qid='+question_id)
    question=cur.fetchall()
    return(question)
def get_answers(question_id):
    question_id=str(question_id)
    con = sqlite3.connect('QuizInfo.db')
    cur=con.cursor()
    cur.execute('SELECT aid,answer FROM Answers WHERE qid='+question_id)
    answers=cur.fetchall()
    return(answers)
def get_right_answer(question_id):
    question_id=str(question_id)
    con = sqlite3.connect('QuizInfo.db')
    cur=con.cursor()
    cur.execute('SELECT aid FROM Answers WHERE qid='+question_id+' AND rightAns=1')
    rightAnswer=cur.fetchone()
    return(rightAnswer[0])
def save_score(score_info):
    con = sqlite3.connect("QuizInfo.db")
    cur=con.cursor()
    try:
        cur.execute("create table Score (userID,score)")
        cur.executemany("insert into Score values (?,?)" ,score_info)
    except:
        cur.executemany("insert into Score values (?,?)" ,score_info)
    con.commit()
    con.close()
def get_scores(userId):
    question_id=str(userId)
    con = sqlite3.connect('QuizInfo.db')
    cur=con.cursor()
    cur.execute('SELECT * FROM Score WHERE qid='+userId)
    scoresdf=cur.fetchall()
    return(scoresdf)