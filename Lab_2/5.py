import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Lê Hoàng Tâm")

ttk.Label(win, text="Enter a name:").grid(column=0, row=0)
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number)
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0) 

action = ttk.Button(win, text="Click Me!")
action.grid(column=2, row=1)

disabled = tk.IntVar()
checkbox1 = tk.Checkbutton(win, text="Disabled", variable=disabled)
checkbox1.grid(column=0, row=2, sticky=tk.W)

unchecked = tk.IntVar()
checkbox2 = tk.Checkbutton(win, text="UnChecked", variable=unchecked)
checkbox2.grid(column=1, row=2, sticky=tk.W)

enabled = tk.IntVar(value=1)
checkbox3 = tk.Checkbutton(win, text="Enabled", variable=enabled)
checkbox3.grid(column=2, row=2, sticky=tk.W)

def change_color():
    color = color_var.get()
    if color == "Blue":
        win.configure(background="blue")
    elif color == "Gold":
        win.configure(background="gold")
    elif color == "Red":
        win.configure(background="red")

color_var = tk.StringVar()
radio1 = tk.Radiobutton(win, text="Blue", variable=color_var, value="Blue", command=change_color)
radio1.grid(column=0, row=3, sticky=tk.W)
radio2 = tk.Radiobutton(win, text="Gold", variable=color_var, value="Gold", command=change_color)
radio2.grid(column=1, row=3, sticky=tk.W)
radio3 = tk.Radiobutton(win, text="Red", variable=color_var, value="Red", command=change_color)
radio3.grid(column=2, row=3, sticky=tk.W)

buttons_frame = ttk.LabelFrame(win, text='Labels in a Frame')
buttons_frame.grid(column=0, row=4, columnspan=3, padx=10, pady=10)

ttk.Label(buttons_frame, text="Label1 -- sooooo much loooonger...").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=0, row=1, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=0, row=2, sticky=tk.W)

name_entered.focus()

win.mainloop()
