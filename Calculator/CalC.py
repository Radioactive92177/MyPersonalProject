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

# adding display
V = StringVar()
Display = Entry(DisplayFrame)
# V.set("Enter Expression here")
Display.pack(fill=X)

# adding buttons frame
ButtonsFrame = Frame(root)
ButtonsFrame.pack(anchor=W, fill=X)

# adding numeric buttons
Button(ButtonsFrame, text="7", fg="Snow", bg="gray40", font="bold").grid(row=1, column=0, padx=3, pady=3)
Button(ButtonsFrame, text="8", fg="Snow", bg="gray40", font="bold").grid(row=1, column=1, padx=3, pady=3)
Button(ButtonsFrame, text="9", fg="Snow", bg="gray40", font="bold").grid(row=1, column=2, padx=3, pady=3)
Button(ButtonsFrame, text="4", fg="Snow", bg="gray40", font="bold").grid(row=2, column=0, padx=3, pady=3)
Button(ButtonsFrame, text="5", fg="Snow", bg="gray40", font="bold").grid(row=2, column=1, padx=3, pady=3)
Button(ButtonsFrame, text="6", fg="Snow", bg="gray40", font="bold").grid(row=2, column=2, padx=3, pady=3)
Button(ButtonsFrame, text="1", fg="Snow", bg="gray40", font="bold").grid(row=3, column=0, padx=3, pady=3)
Button(ButtonsFrame, text="2", fg="Snow", bg="gray40", font="bold").grid(row=3, column=1, padx=3, pady=3)
Button(ButtonsFrame, text="3", fg="Snow", bg="gray40", font="bold").grid(row=3, column=2, padx=3, pady=3)
Button(ButtonsFrame, text="0", fg="Snow", bg="gray40", font="bold").grid(row=4, column=1, padx=3, pady=3)

# adding operator buttons
Button(ButtonsFrame, text=" / ", fg="Snow", bg="gray40", font="bold").grid(row=0, column=3, padx=3, pady=3)
Button(ButtonsFrame, text=" * ", fg="Snow", bg="gray40", font="bold").grid(row=1, column=3, padx=3, pady=3)
Button(ButtonsFrame, text=" - ", fg="Snow", bg="gray40", font="bold").grid(row=2, column=3, padx=3, pady=3)
Button(ButtonsFrame, text="+", fg="Snow", bg="gray40", font="bold").grid(row=3, column=3, padx=3, pady=3)

# adding functional buttons
Button(ButtonsFrame, text="  AC  ", fg="Snow", bg="gray40", font="bold").grid(row=0, columnspan=2, padx=3, pady=3)
Button(ButtonsFrame, text="C", fg="Snow", bg="gray40", font="bold").grid(row=0, column=2, padx=3, pady=3)
Button(ButtonsFrame, text=" . ", fg="Snow", bg="gray40", font="bold").grid(row=4, column=0, padx=3, pady=3)
Button(ButtonsFrame, text="    =    ", fg="Snow", bg="gray40", font="bold").grid(row=4, column=2, columnspan=2, padx=3,pady=3)
root.mainloop()
