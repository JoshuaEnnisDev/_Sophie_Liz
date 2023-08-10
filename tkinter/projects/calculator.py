import tkinter as tk
from tkinter import ttk

# window setup
window = tk.Tk()
window.title("")
window.geometry("300x500")

display_text = tk.StringVar(value=0)


def main():
    display = ttk.Label(
        window,
        textvariable=display_text,
        font=('script', 25, 'bold')
    )
    display.pack()

    button_frame = ttk.Frame(window)
    button_frame.pack()

    button_frame.columnconfigure((0, 1, 2, 3), weight=1)
    button_frame.rowconfigure((0, 1, 2, 3, 4), weight=1)

    # top row
    clear_btn = ttk.Button(button_frame, text='C', command=clear)
    delete_btn = ttk.Button(button_frame, text='DEL', command=delete)

    # second row
    btn7 = ttk.Button(button_frame, text='7', command=lambda: press('7'))
    btn8 = ttk.Button(button_frame, text='8', command=lambda: press('8'))
    btn9 = ttk.Button(button_frame, text='9', command=lambda: press('9'))
    plus_btn = ttk.Button(button_frame, text='+', command=lambda: press('+'))

    # grid buttons
    clear_btn.grid(column=0, row=0, columnspan=2, sticky='nswe')
    delete_btn.grid(column=2, row=0, columnspan=2, sticky='nswe')

    btn7.grid(column=0, row=1, sticky='nswe')
    btn8.grid(column=1, row=1, sticky='nswe')
    btn9.grid(column=2, row=1, sticky='nswe')
    plus_btn.grid(column=3, row=1, sticky='nswe')

    # make sure this is the last line
    window.mainloop()


def press(i):
    expression = display_text.get()
    if expression == '0':
        expression = ''
    expression += i
    display_text.set(expression)


def clear():
    display_text.set('0')


def delete():
    pass
    # get the expression
    # get rid of last thing in the expression
    # set to new expression


def calculate():
    expression = display_text.get()
    result = eval(expression)
    display_text.set(result)


main()
