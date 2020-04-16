import pkg_resources.py2_warn
from tkinter import filedialog, messagebox
from tkinter import *
import tkinter as tk
from tkcalendar import Calendar, DateEntry
import sys
import os


def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)


def example1():
    def print_sel():
        global selDate
        date = cal.selection_get()
        selDate.set(date)
        top.destroy()

    top = tk.Toplevel(window)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1")
    cal.pack(fill="both", expand=True)
    tk.Button(top, text="ok", command=print_sel).pack()


def create():
    if os.path.exists(folder_path.get()):
        title = e1.get()
        cams = e2.get().split(',')
        dirs = e3.get().split(',')
        if e1.get() == "" or e2.get() == "" or e3.get() == "" or e3.get() == "" or selDate.get() == "":
            messagebox.showerror("Error", "Please fill all the fields")
        else:
            rootPath = folder_path.get()+'/'+selDate.get()+' - '+title
            os.mkdir(rootPath)
            for cam in cams:
                os.mkdir(rootPath+'/'+cam)
                for folder in dirs:
                    os.mkdir(rootPath+'/'+cam+'/'+folder)
            messagebox.showinfo("Success", "Structure was created!")
    else:
        messagebox.showerror("Error", "Directory \"" +
                             folder_path.get() + "\" doesn't exists")


window = tk.Tk()

window.iconbitmap(resource_path('icon.ico'))
window.geometry("700x150")
window.resizable(1, 0)

window.title("Structurizer")

tk.Label(window, text="Select root folder:").grid(row=0)
folder_path = StringVar()
lbl1 = Label(master=window, textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=0, column=3)

tk.Label(window, text="Title").grid(row=1)
tk.Label(window, text="Cameras (comma separated)").grid(row=2)
tk.Label(window, text="Dirs (comma separated)").grid(row=3)
e1 = tk.Entry(window)
e2 = tk.Entry(window)
e3 = tk.Entry(window)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)

tk.Label(window, text="Date").grid(row=4)
tk.Button(window, text='Select date', command=example1).grid(row=4, column=2)
selDate = StringVar()
lbl3 = Label(master=window, textvariable=selDate)
lbl3.grid(row=4, column=1)

tk.Button(text='Create', command=create).grid(row=5, column=1)
window.mainloop()
