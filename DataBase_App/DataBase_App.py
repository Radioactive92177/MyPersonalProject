from tkinter import *
import tkinter as tk

root = Tk()
canvas = Canvas(root,height=480,width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8)

label = Label(frame,text="Add Data")
label.grid(row=0,column=1)

name = Label(frame,text="Name")
age = Label(frame,text="Age")
address = Label(frame,text="Address")

name.grid(row=1,column=0)
age.grid(row=2,column=0)
address.grid(row=3,column=0)

entry_name = Entry(frame)
entry_age = Entry(frame)
entry_address = Entry(frame)

entry_name.grid(row=1,column=1)
entry_age.grid(row=2,column=1)
entry_address.grid(row=3,column=1)

button = Button(frame,text="Add")
button.grid(row=4,column=1)

root.mainloop()