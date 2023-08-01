#Tkinter has built in variables that are designed to work with widgets
#They are automatically updated by the widget and they update the widget

import tkinter as tk
from tkinter import ttk

#window setup
window = tk.Tk()
window.title("")
window.geometry("500x500")


#tkintervariable
string_var = tk.StringVar(value = "start value")

#widgets
label = ttk.Label(window, textvariable= string_var)
label.pack()

entry = ttk.Entry(window, textvariable=string_var)
entry.pack()



window.mainloop()# make sure this is the last line