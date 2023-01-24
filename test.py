from tkinter import *

root = Tk()
root.title("Money converter")
root.resizable(width=False, height=False)
root.geometry("380x380")

def NewFile():
    print("1")
def OpenFile():
    print("2")
def About():
    print("3")

Label(root, text="Amount : ").grid(row=1)
e1 = Entry(root)
e1.grid(row=1, column=1)

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

root.mainloop()
