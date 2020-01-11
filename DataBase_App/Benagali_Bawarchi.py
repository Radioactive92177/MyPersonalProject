from tkinter import *
import psycopg2


def login(registration_id, password):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="6502", host="localhost")
    cur = conn.cursor()
    query = '''select EXISTS (SELECT "reg","pass" FROM MEMBERS WHERE "reg"= {0} and "pass" = '{1}');'''.format(
        registration_id, password)
    cur.execute(query, (registration_id, password))
    row = cur.fetchone()
    if row == "(True,)":
        print("LOGIN SUCCESSFUL")
    else:
        print("User not found")
    conn.commit()
    conn.close()


def get_data(First_Name, Last_Name, order, quantity):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="6502", host="localhost")
    cur = conn.cursor()
    query = '''INSERT INTO bengali_bawarchi("First Name", "Last Name", "Order", quantity) VALUES (%s,%s,%s,%s);'''
    cur.execute(query, (First_Name, Last_Name, order, quantity))
    print("Data Inserted")
    conn.commit()
    conn.close()
    display_all()


def search_data(First_Name):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="6502", host="localhost")
    cur = conn.cursor()
    query = '''SELECT *FROM bengali_bawarchi where "First Name"='%s';''' % First_Name
    cur.execute(query, First_Name)
    row = cur.fetchall()
    for x in row:
        display_search(row)
    conn.commit()
    conn.close()


def display_search(row):
    listbox = Listbox(search_frame, width=42)
    listbox.grid(row=2, column=1)
    listbox.insert(END, row)


def display_all():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="6502", host="localhost")
    cur = conn.cursor()
    query = '''SELECT *FROM bengali_bawarchi'''
    cur.execute(query)
    row = cur.fetchall()
    listbox = Listbox(list_frame, width=42, height=3)
    listbox.grid(row=0, column=1)
    for x in row:
        listbox.insert(END, x)


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
                           font=("Times", 15, "bold"), command=lambda: search_data(search_entry.get()))
    search_button.grid(row=1, column=1)

    global list_frame
    list_frame = Frame(canvas, bg="brown1")
    list_frame.place(relx=0.1, rely=0.63, relwidth=0.8, relheight=0.2)

    order_list = Label(list_frame, text="   ORDERS : ", fg="light yellow", bg="brown1", font=("Times", 18, "bold"))
    order_list.grid(row=0, column=0)

    display_all()
    member_window.mainloop()


root = Tk()
root.title("Bengali Bawarchi")
canvas = Canvas(root, height=600, width=600, bg="firebrick2")
canvas.pack()

frame = Frame(canvas, bg="brown1")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

Label(frame, text="Bengali Bawarchi", fg="light yellow", bg="black", font=("Times", 30, "bold")).pack(fill=X)
Label(frame, text="Welcome to Bengali Bawarchi"
                  "\nPlease Enter your details as"
                  "\Mentioned below", fg="light yellow", bg="brown1", font=("Times", 15, "bold")).pack()

frame2 = Frame(canvas, bg="brown1")
frame2.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

registration_id = Label(frame2, text=" REGISTRATION ID : ", fg="light yellow", bg="brown1", font=("Times", 18, "bold"))
password = Label(frame2, text="        PASSWORD       : ", fg="light yellow", bg="brown1", font=("Times", 18, "bold"))

registration_id.grid(row=0, column=0)
password.grid(row=1, column=0)

registration_id_entry = Entry(frame2, width=38)
password_entry = Entry(frame2, width=38)

registration_id_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

login_button = Button(frame2, text="               LOGIN               ", activeforeground="white",
                      activebackground="black",
                      fg="firebrick2", bg="light yellow", font=("Times", 15, "bold"), relief="raised",
                      command=lambda: login(registration_id_entry.get(), password_entry.get()))
login_button.grid(row=2, column=1)

root.mainloop()
