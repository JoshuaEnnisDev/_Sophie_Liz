import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("")
#window.geometry("500x600")

def button_func():
    print("a button was pressed")

#widgets
#text
text = tk.Text(master = window)
text.pack()

#ttk label
label = ttk.Label(master = window, text = "A label widget")
label.pack()

#ttk entry
entry = ttk.Entry(master = window)
entry.pack()

#exercise label
exe_label = ttk.Label(master = window, text="my label")
exe_label.pack()

#exercise button
exe_button = ttk.Button(master = window, text="Exercise Button", command= lambda:print("hello"))
exe_button.pack()
#ttk button
button = ttk.Button(master = window, text = "My first Button", command = button_func)
button.pack()

#lambda button
button2 = ttk.Button(master = window, 
                    text = "Lambda Button", 
                    command = lambda: print("cool no name function") 
                    )
button2.pack()

#add one more label and a button with a function that prints 'hello'
#the label should say "my label" and be between the entry widget and the button



window.mainloop()# make sure this is the last line