import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext

# Tạo cửa sổ chính
win = tk.Tk()
win.title("Tab Example")

# Tạo Tab Control (Notebook)
tab_control = ttk.Notebook(win)

# Tạo Tab1
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Tab 1')

# Tạo Tab2
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Tab 2')

# Hiển thị Tab Control
tab_control.grid(column=0, row=0, padx=10, pady=10)

# ================== Nội dung của Tab1 ==================
# Tạo LabelFrame trong Tab1
label_frame_tab1 = ttk.LabelFrame(tab1, text="Change My Color")
label_frame_tab1.grid(column=0, row=0, padx=10, pady=10)

# Nhập tên trong Tab1
ttk.Label(tab1, text="Enter a name:").grid(column=0, row=1, padx=5, pady=5)
name = tk.StringVar()
name_entered = ttk.Entry(tab1, width=12, textvariable=name)
name_entered.grid(column=0, row=2, padx=5, pady=5)

# Chọn số trong Tab1
ttk.Label(tab1, text="Choose a number:").grid(column=1, row=1, padx=5, pady=5)
number = tk.StringVar()
number_chosen = ttk.Combobox(tab1, width=12, textvariable=number)
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=2, padx=5, pady=5)
number_chosen.current(0)

# Nút hành động trong Tab1
action = ttk.Button(tab1, text="Click Me!")
action.grid(column=2, row=2, padx=5, pady=5)

# ScrolledText trong Tab1
scroll_w = 30
scroll_h = 3
scrolled_text = scrolledtext.ScrolledText(tab1, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scrolled_text.grid(column=0, row=3, columnspan=3, padx=5, pady=5, sticky='W')

# ================== Nội dung của Tab2 ==================
# Checkbox trong Tab2
disabled = tk.IntVar()
checkbox1 = tk.Checkbutton(tab2, text="Disabled", variable=disabled)
checkbox1.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

unchecked = tk.IntVar()
checkbox2 = tk.Checkbutton(tab2, text="Unchecked", variable=unchecked)
checkbox2.grid(column=1, row=0, padx=5, pady=5, sticky=tk.W)

enabled = tk.IntVar(value=1)
checkbox3 = tk.Checkbutton(tab2, text="Enabled", variable=enabled)
checkbox3.grid(column=2, row=0, padx=5, pady=5, sticky=tk.W)

# Radio Button để thay đổi màu sắc LabelFrame trong Tab1
def change_color():
    color = color_var.get()
    if color == "Blue":
        label_frame_tab1.config(background="blue")
    elif color == "Gold":
        label_frame_tab1.config(background="gold")
    elif color == "Red":
        label_frame_tab1.config(background="red")

color_var = tk.StringVar()
radio1 = tk.Radiobutton(tab1, text="Blue", variable=color_var, value="Blue", command=change_color)
radio1.grid(column=0, row=4, padx=5, pady=5, sticky=tk.W)

radio2 = tk.Radiobutton(tab1, text="Gold", variable=color_var, value="Gold", command=change_color)
radio2.grid(column=1, row=4, padx=5, pady=5, sticky=tk.W)

radio3 = tk.Radiobutton(tab1, text="Red", variable=color_var, value="Red", command=change_color)
radio3.grid(column=2, row=4, padx=5, pady=5, sticky=tk.W)

# ================== Menu ==================
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Tạo File menu
def on_exit():
    win.quit()  # Thoát ứng dụng

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()  # Thêm một ngăn cách
file_menu.add_command(label="Exit", command=on_exit)

menu_bar.add_cascade(label="File", menu=file_menu)

# Chạy vòng lặp chính của ứng dụng
win.mainloop()
