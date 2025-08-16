import tkinter as tk 
win = tk.Tk()

strData =  tk.StringVar()
strData.set("Hello Le Hoang Tam")

varsData = strData.get()

print(varsData)

print(tk.IntVar())

print(tk.DoubleVar())
print(tk.BooleanVar())

inData = tk.IntVar()
print(inData)
print(inData.get())

