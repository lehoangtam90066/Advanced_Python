import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import sleep

win = tk.Tk()
win.title("Lê Hoàng Tâm")

tab_control = ttk.Notebook(win)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Tab 1')

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Tab 2')

tab_control.grid(column=0, row=0, padx=10, pady=10)

label_frame_tab1 = ttk.LabelFrame(tab1, text="Change My Color")
label_frame_tab1.grid(column=0, row=0, padx=10, pady=10)

ttk.Label(tab1, text="Enter a name:").grid(column=0, row=1, padx=5, pady=5)
name = tk.StringVar()
name_entered = ttk.Entry(tab1, width=12, textvariable=name)
name_entered.grid(column=0, row=2, padx=5, pady=5)

ttk.Label(tab1, text="Choose a number:").grid(column=1, row=1, padx=5, pady=5)
number = tk.StringVar()
number_chosen = ttk.Combobox(tab1, width=12, textvariable=number)
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=2, padx=5, pady=5)
number_chosen.current(0)

action = ttk.Button(tab1, text="Hello vvv4")
action.grid(column=2, row=2, padx=5, pady=5)

scroll_w = 30
scroll_h = 3
scrolled_text = scrolledtext.ScrolledText(tab1, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scrolled_text.grid(column=0, row=3, columnspan=3, padx=5, pady=5, sticky='W')

# Checkboxes in tab 2
disabled = tk.IntVar()
checkbox1 = tk.Checkbutton(tab2, text="Disabled", variable=disabled)
checkbox1.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

unchecked = tk.IntVar()
checkbox2 = tk.Checkbutton(tab2, text="Unchecked", variable=unchecked)
checkbox2.grid(column=1, row=0, padx=5, pady=5, sticky=tk.W)

enabled = tk.IntVar(value=1)
checkbox3 = tk.Checkbutton(tab2, text="Enabled", variable=enabled)
checkbox3.grid(column=2, row=0, padx=5, pady=5, sticky=tk.W)

# Spinboxes
def _spin1():
    value = spin1.get()
    print(value)
    scrolled_text.insert(tk.INSERT, value + "\n")

spin1 = Spinbox(tab1, from_=0, to=10, width=5, bd=8, command=_spin1)
spin1.grid(column=0, row=4, padx=5, pady=5)

def _spin2():
    value = spin2.get()
    print(value)
    scrolled_text.insert(tk.INSERT, value + "\n")

spin2 = Spinbox(tab1, values=(0, 50, 100), width=5, bd=20, command=_spin2)
spin2.grid(column=1, row=4, padx=5, pady=5)

# Color changing Radiobuttons
def change_color():
    color = color_var.get()
    if color == "Blue":
        label_frame_tab1.config(background="blue")
    elif color == "Gold":
        label_frame_tab1.config(background="gold")
    elif color == "Red":
        label_frame_tab1.config(background="red")

color_var = tk.StringVar()
radio1 = tk.Radiobutton(tab2, text="Blue", variable=color_var, value="Blue", command=change_color)
radio1.grid(column=0, row=5, padx=5, pady=5, sticky=tk.W)

radio2 = tk.Radiobutton(tab2, text="Gold", variable=color_var, value="Gold", command=change_color)
radio2.grid(column=1, row=5, padx=5, pady=5, sticky=tk.W)

radio3 = tk.Radiobutton(tab2, text="Red", variable=color_var, value="Red", command=change_color)
radio3.grid(column=2, row=5, padx=5, pady=5, sticky=tk.W)

# Progressbar
progress_bar = ttk.Progressbar(tab2, orient="horizontal", length=286, mode="determinate")
progress_bar.grid(column=0, row=3, pady=2, columnspan=3)

def run_progressbar():
    progress_bar["maximum"] = 100
    for i in range(101):
        sleep(0.05)
        progress_bar["value"] = i
        progress_bar.update()

def start_progressbar():
    run_progressbar()

def stop_progressbar():
    progress_bar.stop()

def progress_bar_stop_after(wait_ms=1000):
    win.after(wait_ms, lambda: progress_bar.stop())

buttons_frame = ttk.LabelFrame(tab2, text=' ProgressBar ')
buttons_frame.grid(column=0, row=7, sticky='W', columnspan=3)

ttk.Button(buttons_frame, text="Run Progressbar", command=run_progressbar).grid(column=0, row=0, sticky='W')
ttk.Button(buttons_frame, text="Start Progressbar", command=start_progressbar).grid(column=0, row=1, sticky='W')
ttk.Button(buttons_frame, text="Stop immediately", command=stop_progressbar).grid(column=0, row=2, sticky='W')
ttk.Button(buttons_frame, text="Stop after second", command=lambda: progress_bar_stop_after(1000)).grid(column=0, row=3, sticky='W')

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=2, pady=2)

for child in tab2.winfo_children():
    child.grid_configure(padx=8, pady=2)

# Menu
menu_bar = Menu(win)
win.config(menu=menu_bar)

def on_exit():
    win.quit()

def _msgBox():
    msg.showinfo("Python Message Info Box", "A Python GUI Created using tkinter:\nThe year is 2019.")
    msg.showwarning("Python Message Warning Box", "A Python GUI created using tkinter:\nWarning: There might be a bug in this code.")
    msg.showerror('Python Message Error Box', 'A Python GUI created using tkinter:\nError: Houston ~ we DO have a serious PROBLEM!')
    answer = msg.askyesnocancel("Python Message Multi Choice Box", "Are you sure you really wish to do this?")
    print(answer)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=on_exit)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msgBox)

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

win.mainloop()
