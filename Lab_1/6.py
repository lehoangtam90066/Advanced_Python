import tkinter as tk 
from tkinter import ttk
win = tk.Tk()
win.title("Lê Hoàng Tâm")
def click_me():
    action.configure(text="Hello " + name.get()) 
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
action = ttk.Button(win, text="Click me!", command=click_me)
action.grid(column=1, row=1)
name_entered.focus()
win.mainloop()
