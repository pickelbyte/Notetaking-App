import tkinter as tk
import webbrowser

font = ("Trebuchet MS", 12)

def opengh():
    webbrowser.open("https://github.com/pickelbyte")

def main():
    global font
    root = tk.Tk()
    root.geometry("360x200")
    root.title("Info")
    root.resizable(False, False)

    info = tk.Label(root, font=font, text="""
    Note taking app by pickelbyte
    I am still bad at python
    so please excuse the low quality
    """).pack()

    ghlink = tk.Button(root, font=font, text="My github", command=opengh).pack()

if __name__ == "__main__":
    main()