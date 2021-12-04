import random
import string
import tkinter
from tkinter import *

root = Tk()
root.title("Password Generator")
root.geometry("400x90")

psswd = tkinter.StringVar()

class PswdGui:
    # creates the gui and adds widgets, but code for widgets repeats, dont know how to re-use
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.grid(row=0, column=0)

        self.lbl1 = Label(root, text="Password Length: ")
        self.lbl1.grid(row=0, column=0, padx=1, pady=1)

        self.txb1 = Entry(root, width=30)
        self.txb1.insert(0, 94)
        self.txb1.grid(row=0, column=1, padx=1, pady=1)

        self.lbl2 = Label(root, text="New Password: ")
        self.lbl2.grid(row=1, column=0, padx=1, pady=1)

        self.txb2 = Entry(root, width=30)
        self.txb2.insert(0, "--")
        self.txb2.grid(row=1, column=1, padx=1, pady=1)

        self.btn1 = Button(root, text="Generate & Copy New Password", command=lambda: self.psswdgen())
        self.btn1.grid(row=3, column=0, pady=2, padx=5)

        self.btn2 = Button(root, text="Clear New Password", command=lambda: self.clrpsswd())
        self.btn2.grid(row=3, column=1, pady=2, padx=5)

    def psswdgen(self):
        # Generate and Copy password to clipboard; replaces old password with new one every time it runs
        self.num = string.digits
        self.upper = string.ascii_uppercase
        self.lower = string.ascii_lowercase
        self.syms = string.punctuation
        self.all = self.lower + self.upper + self.num + self.syms
        self.tmp = random.sample(self.all, int(self.txb1.get()))
        psswd.set("".join(self.tmp))
        self.txb2.delete(0, END)
        self.txb2.insert(0, psswd.get())
        root.clipboard_clear()
        root.clipboard_append(psswd.get())

    def clrpsswd(self):
        # clears the last password and resets the textbox and clipboard
        self.txb2.delete(0, END)
        self.txb2.insert(0, "--")
        root.clipboard_clear() # didnt clear clipboard but why ?

pg = PswdGui(root)

root.mainloop()
