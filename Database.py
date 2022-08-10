import sqlite3
import Quiz
def create_user_info_database():
    try:
        con = sqlite3.connect("UserInfo.db")
        print("database created ")
        con.close()
    except Exception as e :print("---")
def create_quiz_info_database():
    try:
        con = sqlite3.connect("QuizInfo.db")
        print("database created ")
        con.close()
    except Exception as e :print("---")
Quiz.create_quizDB()