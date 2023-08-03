#Two major ways to get data from a widget
#1 tkinter variables
#2 get()

#example -- entey has a get method that
# gets whatever the person typed into the box

#wigets can be updated with configure

import tkinter as tk
from tkinter import ttk

#window setup
window = tk.Tk()
window.title("")
window.geometry("500x500")

def button_func():
     label.configure(text = entry.get(), background="red")
     #label['text'] = entry.get()
     button1.configure(state = 'disabled')

def button_func2():
     label.configure(text = "your text will appear here", background="white")
     button1.configure(state = 'enabled')

#widgets
#label
label = ttk.Label(window, text = 'Your entry will appear here')
label.pack()

#entry
entry = ttk.Entry(window)
entry.pack()

#2 buttons
button1 = ttk.Button(window, text = "update text", command = button_func)
button1.pack()

#exercise--- add another button that changes the text back to 'some text' and that enables entry

button2 = ttk.Button(window, text = "reset", command = button_func2)
button2.pack()



#code here



window.mainloop()# make sure this is the last line