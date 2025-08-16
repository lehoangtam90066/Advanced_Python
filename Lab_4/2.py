
import tkinter as tk


def get_spin_value():
    value = spinbox.get()  
    print(f"Spinbox value: {value}") 
    scrol.insert(tk.INSERT, value + '\n')  


win = tk.Tk()
win.title("Lê Hoàng Tâm")

spinbox = tk.Spinbox(win, from_=0, to=10, width=5)
spinbox.pack(pady=10)


scrol = tk.Text(win, width=20, height=5, wrap=tk.WORD)
scrol.pack(pady=10)


btn = tk.Button(win, text="Get", command=get_spin_value)
btn.pack(pady=10)


win.mainloop()
