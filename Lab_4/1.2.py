import tkinter as tk 
win = tk.Tk()

strData =  tk.StringVar()
strData.set("Hello Le Hoang Tam")

varsData = strData.get()

print(varsData)