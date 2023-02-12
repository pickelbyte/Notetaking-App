import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as msg
from tkinter import font
import random
import aboutwin

currentfile = None
issaved = True

def donothing():
    pass

def openfile(x=None):
    global maintxt, root, currentfile
    try:
        try:
            fork = open(fd.askopenfilename(initialdir="~/Documents"), 'r')
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
    global root, maintxt, currentfile, issaved
    if issaved is True:
        pass
    else:
        response = msg.askokcancel(title="Unsaved Changes", message="All unsaved changes will be lost")
        if response is True:
            root.title("Notetaker - New Note")
            maintxt.delete(1.0, tk.END)
            currentfile = None
        else:
            pass
    return x

def save(x=None):
    global maintxt, root, currentfile, issaved
    try:
        txt = maintxt.get(1.0, tk.END)
        name = fd.asksaveasfile(parent=root, title="Save as...", defaultextension=".txt", initialdir="~/Documents")
        with open(name.name, 'w') as f:
            f.write(txt)
        root.title(f"Notetaker - {name.name}")
        currentfile = name.name
        issaved = True
    except AttributeError:
        print("AttributeError")

    return x

def checksaved(x=None):
    global maintxt, root, currentfile, issaved
    entrytxt = maintxt.get(1.0, tk.END)
    try:
        with open(currentfile, 'r') as f:
            filetxt = f.read()

        if entrytxt == filetxt:
            issaved = True
            root.title(f"Notepad - {currentfile}")
        else:
            issaved = False
            root.title(f"*Notepad - {currentfile}*")
    except TypeError:
        pass
    return x

def helpmenu():
    msg.showinfo(message="F1 to save, F2 to open, F3 to create new", title="Help")

def about():
    aboutwin.main()

def getsfont():
    global fontsbox, fsize
    size = 12
    try:
        size = int(fsize.get())
    except ValueError:
        pass
    for x in fontsbox.curselection():
        return (fontsbox.get(x), size)

def changefont():
    global maintxt, root, fonts, fontsbox, fsize
    fontwin = tk.Toplevel(root)
    fontsbox = tk.Listbox(fontwin)
    fontsbox.pack(pady=20, expand=True, fill=tk.BOTH)
    for f in fonts:
        fontsbox.insert(tk.END, f)
    applybtn = ttk.Button(fontwin, text="Apply", command=lambda: maintxt.config(font=(getsfont())))
    fsize = tk.Entry(fontwin)
    fsize.pack()
    applybtn.pack()

root = tk.Tk()
root.geometry("720x480")
root.title("Notetaker - New Note")

fonts = list(font.families())
fonts.sort()
crfont = (random.choice(fonts), 12)

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New F3", command=new)
filemenu.add_command(label="Open F2", command=openfile)
filemenu.add_command(label="Save F1", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

formatmenu = tk.Menu(menubar, tearoff=0)
formatmenu.add_command(label="Change Font", command=changefont)
menubar.add_cascade(label="Format", menu=formatmenu)

aboutmenu = tk.Menu(menubar, tearoff=0)
aboutmenu.add_command(label="About", command=about)
aboutmenu.add_command(label="Help", command=helpmenu)
menubar.add_cascade(label="Info", menu=aboutmenu)

maintxt = tk.Text(root, font=crfont)
maintxt.pack(expand=True, fill=tk.BOTH)

root.bind("<F1>", save)
root.bind("<F2>", openfile)
root.bind("<F3>", new)
root.bind("<KeyRelease>", checksaved)
root.config(menu=menubar)
root.mainloop()