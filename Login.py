import sqlite3
import pandas as pd
#This file returns an dataframe with all the input credentials stored in the database
def read_credentials():
    con = sqlite3.connect('UserInfo.db')
    loginDf = pd.read_sql('SELECT * FROM Login', con)
    con.commit()
    con.close()
    return loginDf
#This function will add a new user name and password to the database
def register_user(login_info):
    con = sqlite3.connect("UserInfo.db")
    cur=con.cursor()
    try:
        cur.execute("create table Login (userID,password)")
        cur.executemany("insert into Login values (?,?)" ,login_info)
    except:
        cur.executemany("insert into Login values (?,?)" ,login_info)
    print("User created succesfully")
    con.commit()
    con.close()

#This function returns boolean list of 2 elements 
# if the user name exists validation[0] is True
#if password is correct validation[1] is also True
def login(loginInfo):
    validation=False
    loginDf=read_credentials()
    userIDList=loginDf["userID"].tolist()
    passWordList=loginDf["password"].tolist()
    if(loginInfo[0] in userIDList):
        loginDatabase=dict(zip(userIDList,passWordList))
        if(loginInfo[1]==loginDatabase[loginInfo[0]]):
            validation=True
    return validation


