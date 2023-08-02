from textblob import TextBlob
from tkinter import *

def spell_checker():
    get_data = enter1.get()
    corr = TextBlob(get_data)
    data= corr.correct()
    enter2.delete(0,END)
    enter2.insert(0,data)

def main_window():
    global enter1, enter2
    win = Tk()
    win.geometry("500x400")
    win.resizable(False,False)
    win.config(bg="SkyBlue")
    win.title("Spelling Checker")

    Text1= Label(win,text="Type Something",font=("calibri",30,"bold"),bg="white",fg="Black")
    Text1.place(x=100,y=20,height=50,width=300)

    enter1=Entry(win,font=("calibri",20))
    enter1.place(x=50,y=80,height=50,width=400)

    Text2 = Label(win, text="Correct Spelling", font=("calibri",30, "bold"), bg="white", fg="Black")
    Text2.place(x=100, y=140, height=50, width=300)

    enter2 = Entry(win, font=("calibri", 20))
    enter2.place(x=50, y=200, height=50, width=400)

    button = Button(win,text="Done",font=("calibri",25,"bold"),bg="pink",command=spell_checker)
    button.place(x= 150, y=280,height=50,width=200)
    win.mainloop()
main_window()

