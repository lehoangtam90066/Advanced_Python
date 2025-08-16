import tkinter as tk
from tkinter import ttk
from tkinter import Menu


win = tk.Tk()
win.title("Lê Hoàng Tâm")


label_frame = ttk.LabelFrame(win, text="Change My Color")
label_frame.grid(column=0, row=0, padx=10, pady=10)





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
radio1.grid(column=0, row=4, padx=5, pady=5, sticky=tk.W)

radio2 = tk.Radiobutton(win, text="Gold", variable=color_var, value="Gold", command=change_color)
radio2.grid(column=1, row=4, padx=5, pady=5, sticky=tk.W)

radio3 = tk.Radiobutton(win, text="Red", variable=color_var, value="Red", command=change_color)
radio3.grid(column=2, row=4, padx=5, pady=5, sticky=tk.W)


buttons_frame = ttk.LabelFrame(win, text='Labels in a Frame', padding=(5, 5))
buttons_frame.grid(column=0, row=5, columnspan=3, padx=5, pady=5)




win.mainloop()
