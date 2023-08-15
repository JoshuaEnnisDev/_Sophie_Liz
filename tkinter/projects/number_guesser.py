import tkinter as tk


def guess():
    pass


# window setup
window = tk.Tk()
window.title("number guesser")
window.geometry("500x500")

# widgets
label_text = tk.StringVar(value="Enter a number between 1 and 100")
label = tk.Label(window, textvariable=label_text, font=("Courier", 14))
label.pack(pady=10)

entry = tk.Entry(window, font=("Courier", 14))
entry.pack(pady=10)

button_text = tk.StringVar(value='guess')
button = tk.Button(window, textvariable=button_text, command=guess)
button.pack(pady=10)

# make sure this is the last line
window.mainloop()
