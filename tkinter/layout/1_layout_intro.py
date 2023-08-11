# three major methods to put widgets on the screen

# pack -- defualt top to bottom
# grid -- grid over the entire window
# place -- place them with a position

import tkinter as tk
from tkinter import ttk

# window setup
window = tk.Tk()
window.title("")
window.geometry("500x500")

label1 = ttk.Label(window, text='label1', background='red')
label2 = ttk.Label(window, text='label2', background='blue')
label3 = ttk.Label(window, text='label3', background='green')


# #pack
# label1.pack(side='top', expand = True, fill = 'both', padx=10, pady=10)
# label2.pack(side='top', expand = True, fill= 'both', padx = 10, pady=10)
# label3.pack(side='top', expand = True, fill= 'both', padx = 10, pady=10)

# grid
# define the grid
# window.columnconfigure(0, weight = 1)
# window.columnconfigure(1, weight = 1)
# window.columnconfigure(2, weight = 2)
# window.columnconfigure(4, weight = 1)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)

# place widgets with grid
# label1.grid(row = 0, column = 0, columnspan = 1, sticky='nsew', padx=10, pady=10)
# label2.grid(row = 1, column = 1, columnspan = 2, sticky='nsew')
# label3.grid(row = 0, column = 2, sticky='nsew')

# place
# label1.place(x=0, y=100, width=300, height=200)

# make sure this is the last line
window.mainloop()