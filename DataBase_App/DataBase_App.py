from tkinter import *
import tkinter as tk

import psycopg2


def get_data(name, age, address):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="6502", host="localhost")
    cur = conn.cursor()
    query = '''INSERT INTO demo_table(name, age, address) VALUES (%s,%s,%s);'''
    cur.execute(query, (name, age, address))
    print("Data Inserted")
    conn.commit()
    conn.close()
    display_all()

def search_name(name):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="6502", host="localhost")
    cur = conn.cursor()
    query = '''SELECT *FROM demo_table where name='%s';''' % name
    cur.execute(query, (name))
    row = cur.fetchone()
    display_search(row)
    conn.commit()
    conn.close()


def display_search(row):
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=9, column=1)
    listbox.insert(END, row)


def display_all():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="6502", host="localhost")
    cur = conn.cursor()
    query = '''SELECT *FROM demo_table'''
    cur.execute(query)
    row = cur.fetchall()
    listbox = Listbox(frame, width=20, height=5)
    listbox.grid(row=10, column=1)
    for x in row:
        listbox.insert(END, x)


root = Tk()
canvas = Canvas(root, height=480, width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text="Add Data")
label.grid(row=0, column=1)

name = Label(frame, text="Name")
age = Label(frame, text="Age")
address = Label(frame, text="Address")

name.grid(row=1, column=0)
age.grid(row=2, column=0)
address.grid(row=3, column=0)

entry_name = Entry(frame)
entry_age = Entry(frame)
entry_address = Entry(frame)

entry_name.grid(row=1, column=1)
entry_age.grid(row=2, column=1)
entry_address.grid(row=3, column=1)

add_button = Button(frame, text="Add", command=lambda: get_data(entry_name.get(), entry_age.get(), entry_address.get()))
add_button.grid(row=4, column=1)

search = Label(frame, text="Search")
search.grid(row=5, column=1)

search = Label(frame, text="Search by Name")
search.grid(row=6, column=0)

search_entry = Entry(frame)
search_entry.grid(row=6, column=1)

search_button = Button(frame, text="Search", command=lambda: search_name(search_entry.get()))
search_button.grid(row=6, column=2)

display_all()
root.mainloop()
