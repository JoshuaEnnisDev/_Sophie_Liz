import tkinter as tk
from random import randint

cmp_guess = randint(1, 100)
num_guesses = 0


def guess():
    try:
        entry_text.get()
    except tk.TclError:
        label_text.set("Enter a number silly")
        entry_text.set('')
        return

    global num_guesses
    num_guesses += 1
    button_text.set(f"Guesses {num_guesses}")
    # get user guess
    user_guess = entry_text.get()

    # clear entry IntVar
    entry_text.set("")

    if user_guess > cmp_guess:
        label_text.set(f"{user_guess} was too high.")
    elif user_guess < cmp_guess:
        label_text.set(f"{user_guess} was too low.")
    else:
        label_text.set("Correct!")


# window setup
window = tk.Tk()
window.title("number guesser")
window.geometry("500x500")

# widgets
label_text = tk.StringVar(value="Enter a number between 1 and 100")
label = tk.Label(window, textvariable=label_text, font=("Courier", 14))
label.pack(pady=10)

entry_text = tk.IntVar(value='')
entry = tk.Entry(window, font=("Courier", 14), textvariable=entry_text)
entry.pack(pady=10)

button_text = tk.StringVar(value='guess')
button = tk.Button(
    window, 
    textvariable=button_text,
    command=guess,
    font=("Courier", 14, 'bold'),
    foreground='green'
)

button.pack(pady=10)

# make sure this is the last line
window.mainloop()
