import tkinter as tk
from tkinter import ttk

# window setup
window = tk.Tk()
window.title("")
window.geometry("300x500")

display_text = tk.StringVar(value=0)
invalid = False


def main():
    display = tk.Label(
        window,
        textvariable=display_text,
        font=('script', 25, 'bold'),
        height=3
    )

    display.pack()
    button_frame = ttk.Frame(window)
    button_frame.pack(expand=True, fill='both')

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

    # third row
    btn4 = ttk.Button(button_frame, text='4', command=lambda: press('4'))
    btn5 = ttk.Button(button_frame, text='5', command=lambda: press('5'))
    btn6 = ttk.Button(button_frame, text='6', command=lambda: press('6'))
    minusBtn = ttk.Button(button_frame, text='-', command=lambda: press('-'))
    
    # fourth row
    btn1 = ttk.Button(button_frame, text='1', command=lambda: press('1'))
    btn2 = ttk.Button(button_frame, text='2', command=lambda: press('2'))
    btn3 = ttk.Button(button_frame, text='3', command=lambda: press('3'))
    multiplyBtn = ttk.Button(button_frame, text='x', command=lambda: press('*'))
    
    # fifth row
    btn0 = ttk.Button(button_frame, text='0', command=lambda: press('0'))
    equalsBtn = ttk.Button(button_frame, text='=', command=calculate)
    divisionBtn = ttk.Button(button_frame, text='÷', command=lambda: press('/'))

    # grid buttons
    clear_btn.grid(column=0, row=0, columnspan=2, sticky='nswe')
    delete_btn.grid(column=2, row=0, columnspan=2, sticky='nswe')

    btn7.grid(column=0, row=1, sticky='nswe')
    btn8.grid(column=1, row=1, sticky='nswe')
    btn9.grid(column=2, row=1, sticky='nswe')
    plus_btn.grid(column=3, row=1, sticky='nswe')

    btn4.grid(column=0, row=2, sticky='nswe')
    btn5.grid(column=1, row=2, sticky='nswe')
    btn6.grid(column=2, row=2, sticky='nswe')
    minusBtn.grid(column=3, row=2, sticky='nswe')

    btn1.grid(column=0, row=3, sticky='nswe')
    btn2.grid(column=1, row=3, sticky='nswe')
    btn3.grid(column=2, row=3, sticky='nswe')
    multiplyBtn.grid(column=3, row=3, sticky='nswe')

    btn0.grid(column=1, row=4, sticky='nswe', columnspan=2)
    equalsBtn.grid(column=0, row=4, sticky='nswe')
    divisionBtn.grid(column=3, row=4, sticky='nswe')

    # make sure this is the last line
    window.mainloop()


def press(i):
    global invalid
    if invalid:
        invalid = False
        display_text.set('')
    expression = display_text.get()
    if expression == '0':
        expression = ''
    expression += i
    display_text.set(expression)


def clear():
    display_text.set('0')


def delete():
    expression = display_text.get()
    display_text.set(expression[0:len(expression) - 1])


def calculate():
    global invalid
    expression = display_text.get()
    try:
        result = eval(expression)
        display_text.set(result)
        invalid = False
    except ZeroDivisionError:
        display_text.set("Cannot divide by 0")
        invalid = True
    except SyntaxError:
        display_text.set("Invalid expression")
        invalid = True

main()
