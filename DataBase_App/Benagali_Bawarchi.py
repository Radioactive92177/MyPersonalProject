from tkinter import *
import psycopg2


def get_data(First_Name, Last_Name, order, quantity):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="6502", host="localhost")
    cur = conn.cursor()
    query = '''INSERT INTO benagali_bawarchi("First Name", "Last Name", "Order", quantity) VALUES (%s,%s,%s,%s);'''
    cur.execute(query, (First_Name, Last_Name, order, quantity))
    print("Data Inserted")
    conn.commit()
    conn.close()


def search_data(First_Name):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="6502", host="localhost")
    cur = conn.cursor()
    query = '''SELECT *FROM bengali_bawarchi where First Name='%s';''' % First_Name
    cur.execute(query, First_Name)
    row = cur.fetchone()
    display_search(row)
    conn.commit()
    conn.close()


def display_search(row):
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=9, column=1)
    listbox.insert(END, row)


def members():
    root.destroy()
    member_window = Tk()
    member_window.title("Bengali Bawarchi")
    canvas = Canvas(member_window, height=600, width=600, bg="firebrick2")
    canvas.pack()

    frame = Frame(canvas, bg="brown1")
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    Label(frame, text="Bengali Bawarchi", fg="light yellow", bg="black", font=("Times", 30, "bold")).pack(fill=X)

    frame1 = Frame(canvas, bg="brown1")
    frame1.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.7)

    name = Label(frame1, text="        NAME : ", fg="light yellow", bg="brown1", font=("Times", 18, "bold"))
    order = Label(frame1, text="      ORDER : ", fg="light yellow", bg="brown1", font=("Times", 18, "bold"))

    name.grid(row=0, column=0)
    order.grid(row=1, column=0)

    First_name_entry = Entry(frame1)
    Last_name_entry = Entry(frame1)
    order_entry = Entry(frame1)
    quantity_entry = Entry(frame1)

    First_name_entry.grid(row=0, column=1)
    Last_name_entry.grid(row=0, column=2)
    order_entry.grid(row=1, column=1)
    quantity_entry.grid(row=1, column=2)

    Button(frame1, text=" CONFIRM  ", fg="firebrick2", bg="light yellow", font=("Times", 15, "bold"),
           command=lambda: get_data(First_name_entry.get(), Last_name_entry.get(), order_entry.get(),
                                    quantity_entry.get())).grid(row=2,
                                                                column=2)
    global search_frame
    search_frame = Frame(canvas, bg="brown1")
    search_frame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.2)

    search = Label(search_frame, text="   SEARCH : ", fg="light yellow", bg="brown1", font=("Times", 18, "bold"))
    search_entry = Entry(search_frame, width=42)

    search.grid(row=0, column=0)
    search_entry.grid(row=0, column=1)

    search_button = Button(search_frame, text="               SEARCH                 ", fg="firebrick2", bg="light "
                                                                                                            "yellow",
                           font=("Times", 15, "bold"))
    search_button.grid(row=1, column=1)

    listbox = Listbox(search_frame, width=42)
    listbox.grid(row=2, column=1)

    member_window.mainloop()


root = Tk()
root.title("Bengali Bawarchi")
canvas = Canvas(root, height=600, width=600, bg="firebrick2")
canvas.pack()

frame = Frame(canvas, bg="brown1")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

Label(frame, text="Bengali Bawarchi", fg="light yellow", bg="black", font=("Times", 30, "bold")).pack(fill=X)
Label(frame, text="Welcome to Bengali Bawarchi"
                  " \nPlease stay quiet"
                  "\nThe only place in LPU"
                  "\nWhere food feels like home", fg="light yellow", bg="brown1", font=("Times", 15, "bold")).pack()
Button(frame, text="MEMBERS", command=members).pack()
Button(frame, text="CUSTOMERS").pack(side=BOTTOM)

root.mainloop()
