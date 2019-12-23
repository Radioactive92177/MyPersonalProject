import parser
from tkinter import *

root = Tk()
root.title("CalC version 01")
root.configure(bg="LightBlue2")

# adding title frame
TitleFrame = Frame(root, bg="gray29")
TitleFrame.pack(fill=X)

# adding title
Title = Label(TitleFrame, text="CalSy", font=("Times", 16, "bold"), fg="Snow", bg="gray29")
Title.pack()

# adding display frame
DisplayFrame = Frame(root)
DisplayFrame.pack(fill=X)

# adding input field
Display = Entry(DisplayFrame)
# V.set("Enter Expression here")
Display.pack(fill=X)

i = 0


# getting variables in the input field
def get_variables(num):
    global i
    Display.insert(i, num)
    i += 1


# getting operators in the input field
def get_operation(operator):
    global i
    length = len(operator)
    Display.insert(i, operator)
    i += length


# getting functions
def clear_all():
    Display.delete(0, END)


def undo():
    entire_string = Display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        Display.insert(0, new_string)
    else:
        clear_all()
        Display.insert(0, "Error")


# calculating
def calculate():
    entire_string = Display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        Display.insert(0, result)
    except Exception:
        clear_all()
        Display.insert(0, "Error")


# adding buttons frame
ButtonsFrame = Frame(root)
ButtonsFrame.pack(anchor=W, fill=X)

# adding numeric buttons
Button(ButtonsFrame, text="7", fg="Snow", bg="gray40", font="bold", command=lambda: get_variables(7)).grid(row=1,
                                                                                                           column=0,
                                                                                                           padx=3,
                                                                                                           pady=3)
Button(ButtonsFrame, text="8", fg="Snow", bg="gray40", font="bold", command=lambda: get_variables(8)).grid(row=1,
                                                                                                           column=1,
                                                                                                           padx=3,
                                                                                                           pady=3)
Button(ButtonsFrame, text="9", fg="Snow", bg="gray40", font="bold", command=lambda: get_variables(9)).grid(row=1,
                                                                                                           column=2,
                                                                                                           padx=3,
                                                                                                           pady=3)
Button(ButtonsFrame, text="4", fg="Snow", bg="gray40", font="bold", command=lambda: get_variables(4)).grid(row=2,
                                                                                                           column=0,
                                                                                                           padx=3,
                                                                                                           pady=3)
Button(ButtonsFrame, text="5", fg="Snow", bg="gray40", font="bold", command=lambda: get_variables(5)).grid(row=2,
                                                                                                           column=1,
                                                                                                           padx=3,
                                                                                                           pady=3)
Button(ButtonsFrame, text="6", fg="Snow", bg="gray40", font="bold", command=lambda: get_variables(6)).grid(row=2,
                                                                                                           column=2,
                                                                                                           padx=3,
                                                                                                           pady=3)
Button(ButtonsFrame, text="1", fg="Snow", bg="gray40", font="bold", command=lambda: get_variables(1)).grid(row=3,
                                                                                                           column=0,
                                                                                                           padx=3,
                                                                                                           pady=3)
Button(ButtonsFrame, text="2", fg="Snow", bg="gray40", font="bold", command=lambda: get_variables(2)).grid(row=3,
                                                                                                           column=1,
                                                                                                           padx=3,
                                                                                                           pady=3)
Button(ButtonsFrame, text="3", fg="Snow", bg="gray40", font="bold", command=lambda: get_variables(3)).grid(row=3,
                                                                                                           column=2,
                                                                                                           padx=3,
                                                                                                           pady=3)
Button(ButtonsFrame, text="0", fg="Snow", bg="gray40", font="bold", command=lambda: get_variables(0)).grid(row=4,
                                                                                                           column=1,
                                                                                                           padx=3,
                                                                                                           pady=3)

# adding operator buttons
Button(ButtonsFrame, text=" / ", fg="Snow", bg="gray40", font="bold", command=lambda: get_operation("/")).grid(row=0,
                                                                                                               column=3,
                                                                                                               padx=3,
                                                                                                               pady=3)
Button(ButtonsFrame, text=" * ", fg="Snow", bg="gray40", font="bold", command=lambda: get_operation("*")).grid(row=1,
                                                                                                               column=3,
                                                                                                               padx=3,
                                                                                                               pady=3)
Button(ButtonsFrame, text=" - ", fg="Snow", bg="gray40", font="bold", command=lambda: get_operation("-")).grid(row=2,
                                                                                                               column=3,
                                                                                                               padx=3,
                                                                                                               pady=3)
Button(ButtonsFrame, text="+", fg="Snow", bg="gray40", font="bold", command=lambda: get_operation("+")).grid(row=3,
                                                                                                             column=3,
                                                                                                             padx=3,
                                                                                                             pady=3)

# adding functional buttons
Button(ButtonsFrame, text="  AC  ", fg="Snow", bg="gray40", font="bold", command=lambda: clear_all()).grid(row=0,
                                                                                                           columnspan=2,
                                                                                                           padx=3,
                                                                                                           pady=3)
Button(ButtonsFrame, text="C", fg="Snow", bg="gray40", font="bold", command=lambda: undo()).grid(row=0, column=2,
                                                                                                 padx=3, pady=3)
Button(ButtonsFrame, text=" . ", fg="Snow", bg="gray40", font="bold", command=lambda: get_variables(".")).grid(row=4,
                                                                                                               column=0,
                                                                                                               padx=3,
                                                                                                               pady=3)
Button(ButtonsFrame, text="    =    ", fg="Snow", bg="gray40", font="bold", command=lambda: calculate()).grid(row=4,
                                                                                                              column=2,
                                                                                                              columnspan=2,
                                                                                                              padx=3,
                                                                                                              pady=3)
root.mainloop()
