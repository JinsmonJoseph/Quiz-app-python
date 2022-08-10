
from tkinter import*
import Login
import Quiz
import random
import Score
#Database.create_quizApp_database()
root=Tk()
root.title("QUIZ APP")
root.geometry("700x700")
loggedInUser=""
def createNewUserScreen():
    global root
    for wid in root.winfo_children():
        wid.destroy()
    usernameLabel = Label(root, text="User Name")
    usernameLabel.grid(row=0, column=0,padx=20,pady=15)
    userName=StringVar()
    usernameEntry = Entry(root, textvariable=userName)
    usernameEntry.grid(row=0, column=1,padx=20,pady=15)  
 
    passwordLabel = Label(root,text="Password")
    passwordLabel.grid(row=1, column=0,padx=20,pady=15)  
    password = StringVar()
    passwordEntry = Entry(root, textvariable=password)
    passwordEntry.grid(row=1, column=1,padx=20,pady=15)
    def create_login_info():
        u=userName.get()
        loginDf=Login.read_credentials()
        userIDList=loginDf["userID"].tolist()
        p=password.get()
        loginInfo=[(u,p)]
        if(loginInfo[0][0] in userIDList):
            usernamealreadyexistLabel = Label(root,text="User name already exists")
            usernamealreadyexistLabel.grid(row=3, column=0,padx=20,pady=15)
            submitButton.configure(text="RETRY")
            submitButton.configure(command=createNewUserScreen)
        else:
            Login.register_user(loginInfo)
            get_welcome_page()
    submitButton=Button(root,text="SUBMIT" ,bg="red",fg="white",width="35",command=create_login_info)
    submitButton.grid(row=2,column=0,padx=20,pady=15)
def viewScores():
    global root 
    for wid in root.winfo_children():
        wid.destroy()
    uid=int(loggedInUser)
    scores=Quiz.get_scores(uid)
    for i in range(len(scores)):
        scoreLabel = Label( root, text="Attempt "+i+" : "+scores[0][i])
        scoreLabel.grid(row=i, column=0,padx=20,pady=15)

def Create_home_screen():
    global root 
    for wid in root.winfo_children():
        wid.destroy()
    startQuizButton=Button(root,text="START QUIZ",bg="green",fg="white",width="35",command=start_quiz)
    startQuizButton.grid(row=0,column=1,padx=70,pady=15)
    viewScoreButton=Button(root,text="VIEW MY SCORES",bg="blue",fg="white",width="35",command=viewScores)
    viewScoreButton.grid(row=1,column=1,padx=70,pady=15)
    
def createExistingUserScreen():
    global root 
    for wid in root.winfo_children():
        wid.destroy()
    usernameLabel = Label(root, text="User Name")
    usernameLabel.grid(row=0, column=0,padx=20,pady=15)
    userName=StringVar()
    usernameEntry = Entry(root, textvariable=userName)
    usernameEntry.grid(row=0, column=1,padx=20,pady=15)  
    passwordLabel = Label(root,text="Password")
    passwordLabel.grid(row=1, column=0,padx=20,pady=15)  
    password = StringVar()
    passwordEntry = Entry(root, textvariable=password)
    passwordEntry.grid(row=1, column=1,padx=20,pady=15)
    def create_login_info():
        u=userName.get()
        p=password.get()
        loginInfo=[u,p]
        x=Login.login(loginInfo)
        if(x==False):
            usernamealreadyexistLabel = Label(root,text="Wrong password")
            usernamealreadyexistLabel.grid(row=3, column=0,padx=20,pady=15)
            submitButton.configure(text="RETRY")
            submitButton.configure(command=createNewUserScreen)
        else:
            global loggedInUser
            loggedInUser=str(u)
            Create_home_screen()
    submitButton=Button(root,text="SUBMIT",bg="red",fg="white",width="35",command=create_login_info)
    submitButton.grid(row=2,column=0,padx=20,pady=15)
def start_quiz():
    quid_list=random.sample(range(1,10),5)
    i=0
    score=0
    def question_screen():
        global root
        for wid in root.winfo_children():
            wid.destroy()
        nonlocal i
        ques=Quiz.get_question(quid_list[i])
        print(ques)
        question=ques[0][1]
        answers=Quiz.get_answers(quid_list[i])
        var1=StringVar()
        Question_label = Label( root, textvariable=var1, relief=RAISED )
        var1.set(question)
        var=IntVar()
        Question_label.grid(row=0, column=0,padx=20,pady=15)
        def selection():
            global selected
            selected=var.get()
        def score_update():
            if(selected==Quiz.get_right_answer(ques[0][0])):
                nonlocal score
                score=score+20
            print(score)
            if(i<5):
                question_screen()
            else:
                Score.score_screen(score)
        r1= Radiobutton(root, text=answers[0][1], variable=var, value=answers[0][0],command=selection)
        r1.grid(row=1, column=0,padx=20,pady=15)
        r2= Radiobutton(root, text=answers[1][1], variable=var, value=answers[1][0],command=selection)
        r2.grid(row=2, column=0,padx=20,pady=15)
        r3= Radiobutton(root, text=answers[2][1], variable=var, value=answers[2][0],command=selection)
        r3.grid(row=3, column=0,padx=20,pady=15)
        r4= Radiobutton(root, text=answers[3][1], variable=var, value=answers[3][0],command=selection)
        r4.grid(row=4, column=0,padx=20,pady=15)
        nextButton=Button(root,text="NEXT",bg="green",fg="white",width="35",command=score_update)
        nextButton.grid(row=5,column=0,padx=70,pady=15)
        i=i+1
    question_screen()


def get_welcome_page():
    global root 
    for wid in root.winfo_children():
        wid.destroy()
    newUserButton=Button(root,text="REGISTER NEW USER",bg="green",fg="white",width="35",command=createNewUserScreen)
    newUserButton.grid(row=0,column=1,padx=70,pady=15)
    existingUserButton=Button(root,text="LOG IN AS EXISTING USER",bg="blue",fg="white",width="35",command=createExistingUserScreen)
    existingUserButton.grid(row=1,column=1,padx=70,pady=15)
    exitButton=Button(root,text="EXIT",bg="red",fg="white",width="35",command=exit)
    exitButton.grid(row=2,column=1,padx=70,pady=15)
    root.mainloop()
get_welcome_page()





        
    
    



