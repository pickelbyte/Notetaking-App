import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as msg
import os
from typing import TextIO
import webbrowser
import aboutwin

font = ("Arial", 12)
currentfile = None

def donothing():
    pass

def openfile(x=None):
    global maintxt, root, currentfile
    try:
        try:
            fork = open(fd.askopenfilename(), 'r')
            maintxt.delete(1.0, tk.END)
            maintxt.insert(tk.END, fork.read())
            root.title(f"Notetaker - {fork.name}")
            currentfile = fork.name
        except FileNotFoundError:
            pass
    except AttributeError:
        pass
    return x

def new(x=None):
    global root, maintxt, currentfile
    root.title("Notetaker - New Note")
    maintxt.delete(1.0, tk.END)
    currentfile = None
    return x

def save(x=None):
    global maintxt, root, currentfile
    try:
        txt = maintxt.get(1.0, tk.END)
        name = fd.asksaveasfile(parent=root, title="Save as...", defaultextension=".txt")
        with open(name.name, 'w') as f:
            f.write(txt)
        root.title(f"Notetaker - {name.name}")
        currentfile = name.name
    except AttributeError:
        print("AttributeError")

    return x

def checksaved(x=None):
    global maintxt, root, currentfile
    entrytxt = maintxt.get(1.0, tk.END)
    try:
        with open(currentfile, 'r') as f:
            filetxt = f.read()

        if entrytxt == filetxt:
            root.title(f"Notepad - {currentfile}")
        else:
            root.title(f"*Notepad - {currentfile}*")
    except TypeError:
        pass
    return x

def helpmenu():
    msg.showinfo(message="F1 to save, F2 to open, F3 to create new", title="Help")

def about():
    aboutwin.main()

root = tk.Tk()
root.geometry("720x480")
root.title("Notetaker")

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New F3", command=new)
filemenu.add_command(label="Open F2", command=openfile)
filemenu.add_command(label="Save F1", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

aboutmenu = tk.Menu(menubar, tearoff=0)
aboutmenu.add_command(label="About", command=about)
aboutmenu.add_command(label="Help", command=helpmenu)
menubar.add_cascade(label="Info", menu=aboutmenu)

maintxt = tk.Text(root, font=font)
maintxt.pack(expand=True, fill=tk.BOTH)

root.bind("<F1>", save)
root.bind("<F2>", openfile)
root.bind("<F3>", new)
root.bind("<KeyRelease>", checksaved)
root.config(menu=menubar)
root.mainloop()
