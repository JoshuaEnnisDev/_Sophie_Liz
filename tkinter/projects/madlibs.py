import tkinter as tk
from tkinter import ttk

# window setup
window = tk.Tk()
window.title("")
window.geometry("500x500")

verb_label = ttk.Label(window, text="Verb")
verb_entry = ttk.Entry(window)
verb_label.pack(side='left')
verb_entry.pack(side='left')
story = ttk.Label(window)


def go():
    story['text'] = f'''
                I was {verb_entry.get()}ing to the store when\n
                a man came up to me and {verb_entry.get()}
            '''
    story.pack()


go_btn = ttk.Button(window, text='go', command=go)
go_btn.pack()


# make sure this is the last line
window.mainloop()
