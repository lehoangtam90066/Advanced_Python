import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import messagebox as msg


win = tk.Tk()
win.title("Lê Hoàng Tâm")


tab_control = ttk.Notebook(win)


tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Tab 1')


tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Tab 2')


tab_control.grid(column=0, row=0, padx=10, pady=10)



def _msgBox():
    msg.showinfo("Python Message Info Box", "A Python GUI Created using tkinter:\nThe year is 2019.")
    msg.showwarning("Python Message Warning Box", "A Python GUI created using tkinter:\nWarning: There might be a bug in this code.")
    msg.showerror('Python Message Error Box', 'A Python GUI created  using tkinter:'
'\nError: Houston ~ we DO have a serious PROBLEM!')
answer = msg.askyesnocancel("Python Message Multi Choice Box", "Are  you sure you really wish to do this?")
print(answer)

menu_bar = Menu(win)
win.config(menu=menu_bar)


def on_exit():
    win.quit()

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=on_exit)


help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msgBox)

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)


win.mainloop()
