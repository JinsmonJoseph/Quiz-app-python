import Main
import Quiz
from tkinter import*
def score_screen(score):
    uid=int(Main.loggedInUser)
    scoreInfo=[(uid,score)]
    Quiz.save_score(scoreInfo)
    global root 
    for wid in root.winfo_children():
        wid.destroy()
    var1=StringVar()
    label_1 = Label( root, textvariable=var1, relief=RAISED )
    label_1.grid(row=1, column=0,padx=20,pady=15)
    if(score<=40):
        var1.set("SCORE : "+score+"%\n\nPLEASE TRY AGAIN")
        nextButton=Button(root,text="TRY NOW",bg="green",fg="white",width="35",command=Main.start_quiz)
        nextButton.grid(row=5,column=0,padx=70,pady=15)
    elif(score==60):
        var1.set("SCORE : "+score+"%\n\nGOOD JOB")
    elif(score==80):
        var1.set("SCORE : "+score+"%\n\nEXCELLENT WORK")
    else:
        var1.set("SCORE : "+score+"%\n\nYOU ARE GENIUS")
    backButton=Button(root,text="BACK BUTTON",bg="green",fg="white",width="35",command=Main.get_welcome_page)
    backButton.grid(row=5,column=0,padx=70,pady=15)