import tkinter as tk
from random import randint, choice
from tkinter import messagebox


def AddIdea():
    value = EnterText.get()
    if value != '':
        with open('ideas.txt', 'a+', encoding="utf-8") as file:
            file.write(value + '\n')
        EnterText.delete(0, 'end')
    else:
        tk.messagebox.showinfo(
            "The ERROR", ("An entry pole is empty! You are stupid f@cker!"))


def ShowIdea():
    with open('ideas.txt', 'r', encoding="utf-8") as file:
        lines = file.readlines()
        tk.messagebox.showinfo('An idea', (choice(lines)))


def EnterClick(e):
    AddIdea()


window = tk.Tk()

window.resizable(width=False, height=False)

window.title("Ideas Generation")

window.geometry('720x360')

window["bg"] = "black"


idea = tk.Label(window, text="Add a new idea",
                font=("Arial Bold", 14), fg="white", bg="black")
idea.place(x=290, y=25)

EnterText = tk.Entry(fg="black", width=47)
EnterText.place(x=220, y=65)

btn = tk.Button(window, text="Add", command=AddIdea, width=40,
                height=2, fg="black", bg="silver")
btn.place(x=220, y=100)

window.bind('<Return>, EnterClick')

GiveIdea = tk.Label(window, text="Generate an idea", font=(
    "Arial Bond", 14), fg="white", bg="black")
GiveIdea.place(x=290, y=170)

btn = tk.Button(window, text="Show an idea", command=ShowIdea, width=40,
                height=2, fg="black", bg="silver")
btn.place(x=220, y=210)

window.mainloop()
