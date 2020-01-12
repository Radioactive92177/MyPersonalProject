from tkinter import *
from psycopg2 import *

label_fg = "light yellow"
label_bg = "black"
text_fg = "white"
text_bg = "black"
button_fg = "red"
button_bg = "white"
frame_bg = "black"
canvas_bg = "black"


def login_fun(id, password):
    conn = connect(dbname="postgres", user="postgres", password="6502", host="localhost")
    cur = conn.cursor()
    query = '''select EXISTS (SELECT "id","pass" FROM staffs WHERE "id"= {0} and "pass" = '{1}');'''.format(id,
                                                                                                            password)
    cur.execute(query)
    result = cur.fetchone()
    if result == (True,):
        print("Login SuccessFul")
        FirstScreen.destroy()
        Title2Frame.destroy()

    else:
        print("Access Denied")
        register()


def register_function(id, password, name, phone, address):
    conn = connect(dbname="postgres", user="postgres", password="6502", host="localhost")
    cur = conn.cursor()
    query = '''insert into staffs (id, pass, name, phone, address) VALUES ({0},{1},'{2}',{3},'{4}');'''.format(id,
                                                                                                               password,
                                                                                                               name,
                                                                                                               phone,
                                                                                                               address)
    cur.execute(query)
    print(f"{name} is a registered in staffs")
    conn.commit()
    conn.close()


def register():
    Title3Frame = Frame(MainScreen, bg=frame_bg)
    Title3Frame.place(relx=0.06, rely=0.58, relwidth=0.88, relheight=0.07)

    Title = Label(Title3Frame, text="Register", fg=text_fg, bg=label_bg, font=("Times", 30, "bold"))
    Title.pack(fill=X)
    # Adding the register frame for new staffs
    Register_Frame = Frame(FirstScreen, bg=frame_bg)
    Register_Frame.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.34)

    Label(Register_Frame, text="                          ID :", fg=label_fg, bg=label_bg,
          font=("Helvetica", 18, "bold")).grid(row=0, column=0)
    Label(Register_Frame, text="          PASSWORD :", fg=label_fg, bg=label_bg, font=("Helvetica", 18, "bold")).grid(
        row=1,
        column=0)
    Label(Register_Frame, text="                   NAME :", fg=label_fg, bg=label_bg,
          font=("Helvetica", 18, "bold")).grid(
        row=2, column=0)
    Label(Register_Frame, text="                 PHONE :", fg=label_fg, bg=label_bg,
          font=("Helvetica", 18, "bold")).grid(
        row=3, column=0)
    Label(Register_Frame, text="            ADDRESS :", fg=label_fg, bg=label_bg, font=("Helvetica", 18, "bold")).grid(
        row=4,
        column=0)

    reg_ID_Entry = Entry(Register_Frame, width=40)
    password_Entry = Entry(Register_Frame, width=40)
    name_Entry = Entry(Register_Frame, width=40)
    phone_Entry = Entry(Register_Frame, width=40)
    address_Entry = Entry(Register_Frame, width=40)

    reg_ID_Entry.grid(row=0, column=1)
    password_Entry.grid(row=1, column=1)
    name_Entry.grid(row=2, column=1)
    phone_Entry.grid(row=3, column=1)
    address_Entry.grid(row=4, column=1)

    register_button = Button(Register_Frame, text="            REGISTER             ", activeforeground="white",
                             activebackground="black",
                             fg=button_fg, bg=button_bg, font=("Times", 15, "bold"), relief="raised",
                             command=lambda: register_function(reg_ID_Entry.get(), password_Entry.get(),
                                                               name_Entry.get(), phone_Entry.get(),
                                                               address_Entry.get()))
    register_button.grid(row=5, column=1)


root = Tk()
root.title("Restaurant")

# creating Main Screen here
MainScreen = Canvas(root, height=768, width=600, bg=canvas_bg)
MainScreen.pack()

# creating Title Frame here
TitleFrame = Frame(MainScreen, bg=frame_bg)
TitleFrame.place(relx=0.06, rely=0.02, relwidth=0.88, relheight=0.07)

# Adding Title here
Title = Label(TitleFrame, text="Restaurant", fg=text_fg, bg=label_bg, font=("Times", 30, "bold"))
Title.pack(fill=X)

# This is the first screen
FirstScreen = Frame(MainScreen, bg=frame_bg)
FirstScreen.place(relx=0.06, rely=0.1, relwidth=0.88, relheight=0.88)

textFrame = Frame(FirstScreen, bg=frame_bg)
textFrame.place(relx=0.05, rely=0.005, relwidth=0.9, relheight=0.15)

text = Label(textFrame, text="Welcome to our Restaurant"
                             "\n Please enter details"
                             "\n As mentioned below", fg=text_fg, bg=label_bg, font=("Times", 18, "bold"))
text.pack()

Title2Frame = Frame(MainScreen, bg=frame_bg)
Title2Frame.place(relx=0.06, rely=0.28, relwidth=0.88, relheight=0.07)

Title = Label(Title2Frame, text="Login", fg=label_fg, bg=label_bg, font=("Times", 30, "bold"))
Title.pack(fill=X)

LoginFrame = Frame(FirstScreen, bg=frame_bg)
LoginFrame.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.18)

ID = Label(LoginFrame, text="                          ID :", fg=label_fg, bg=label_bg, font=("Helvetica", 18, "bold"))
PASS = Label(LoginFrame, text="          PASSWORD :", fg=label_fg, bg=label_bg, font=("Helvetica", 18, "bold"))

ID.grid(row=0, column=0)
PASS.grid(row=1, column=0)

ID_entry = Entry(LoginFrame, width=40)
PASS_entry = Entry(LoginFrame, width=40)

ID_entry.grid(row=0, column=1)
PASS_entry.grid(row=1, column=1)

login_button = Button(LoginFrame, text="                LOGIN                ", activeforeground="white",
                      activebackground="black",
                      fg=button_fg, bg=button_bg, font=("Times", 15, "bold"), relief="raised",
                      command=lambda: login_fun(ID_entry.get(), PASS_entry.get()))
login_button.grid(row=2, column=1)

Title3Frame = Frame(MainScreen, bg=frame_bg)
Title3Frame.place(relx=0.06, rely=0.58, relwidth=0.88, relheight=0.07)

root.mainloop()
