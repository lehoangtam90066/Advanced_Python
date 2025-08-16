import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext  
from tkinter import Menu



win = tk.Tk()
win.title("Lê Hoàng Tâm")

from tkinter import Menu


win = tk.Tk()
win.title("Menu Example")


menu_bar = Menu(win)
win.config(menu=menu_bar)  


file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator() 
file_menu.add_command(label="Exit", command=win.quit)  


menu_bar.add_cascade(label="File", menu=file_menu)   




mighty = ttk.LabelFrame(win, text=" Mighty Python")
mighty.grid(column=0, row=0, padx=8, pady=4)

# a_label =ttk.Label(mighty, text= "Enter a name: ")
# a_label.grid(column=0, row=0)

buttons_frame = ttk.Labelframe(mighty, text="Labels in a Frame")
buttons_frame.grid(column=0, row=7)

ttk.Label(mighty, text="Enter a name:").grid(column=0, row=0, padx=5, pady=5)
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, padx=5, pady=5)


ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0, padx=5, pady=5)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number)
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1, padx=5, pady=5)
number_chosen.current(0)


action = ttk.Button(mighty, text="Click Me!")
action.grid(column=2, row=1, padx=5, pady=5)


scroll_w = 30
scroll_h = 3
scrolled_text = scrolledtext.ScrolledText(mighty, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scrolled_text.grid(column=0, row=2, columnspan=3, padx=5, pady=5, sticky='W')


disabled = tk.IntVar()
checkbox1 = tk.Checkbutton(mighty, text="Disabled", variable=disabled)
checkbox1.grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)

unchecked = tk.IntVar()
checkbox2 = tk.Checkbutton(mighty, text="Unchecked", variable=unchecked)
checkbox2.grid(column=1, row=3, padx=5, pady=5, sticky=tk.W)

enabled = tk.IntVar(value=1)
checkbox3 = tk.Checkbutton(mighty, text="Enabled", variable=enabled)
checkbox3.grid(column=2, row=3, padx=5, pady=5, sticky=tk.W)


def change_color():
    color = color_var.get()
    if color == "Blue":
        win.configure(background="blue")
    elif color == "Gold":
        win.configure(background="gold")
    elif color == "Red":
        win.configure(background="red")


color_var = tk.StringVar()
radio1 = tk.Radiobutton(mighty, text="Blue", variable=color_var, value="Blue", command=change_color)
radio1.grid(column=0, row=4, padx=5, pady=5, sticky=tk.W)

radio2 = tk.Radiobutton(mighty, text="Gold", variable=color_var, value="Gold", command=change_color)
radio2.grid(column=1, row=4, padx=5, pady=5, sticky=tk.W)

radio3 = tk.Radiobutton(mighty, text="Red", variable=color_var, value="Red", command=change_color)
radio3.grid(column=2, row=4, padx=5, pady=5, sticky=tk.W)


buttons_frame = ttk.LabelFrame(mighty, text='Labels in a Frame', padding=(5, 5))
buttons_frame.grid(column=0, row=5, columnspan=3, padx=5, pady=5)

ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, padx=5, pady=5, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, padx=5, pady=5, sticky=tk.W)

# name_entered.focus()


win.mainloop()
