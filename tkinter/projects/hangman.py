import tkinter as tk
from random import choice

# global variables
correct = []
words = ["cat"]
word = choice(words)
wrong = 0


def handle_click():
    global correct
    global word
    global wrong

    current_guess = user_guess.get()

    if current_guess not in word:
        wrong += 1
        draw_man(wrong)

    


    # adds the correct letters to the list
    for letter in word:
        if letter == current_guess:
            correct.append(current_guess)

    # recreate the word
    word_state = ""
    for letter in word:
        if letter in correct:
            word_state += letter + " "
        else:
            word_state += "_ "
    word_text.set(word_state)
    user_guess.set('')

    # win condition
    if len(correct) == len(word):
        word_text.set("You win!!!")

    # lose condition
    if wrong == 2:
        print("Hello!!!!!")
        word_text.set("You lose!")


window = tk.Tk()
window.geometry('500x500')

# frames
left_frame = tk.Frame(window, padx=20)
right_frame = tk.Frame(window)
left_frame.pack(side='left', fill='both')
right_frame.pack(side='left', fill='both')

# left widgets
label = tk.Label(left_frame, text="Guess a letter")
label.pack(pady=20)

user_guess = tk.StringVar()
entry = tk.Entry(left_frame, textvariable=user_guess)
entry.pack(pady=20)


def get_blanks():
    tmp = ""
    for letter in word:
        tmp += "_ "
    return tmp


word_text = tk.StringVar(value=get_blanks())
word_label = tk.Label(
    left_frame,
    text="_ _ _ _ _",
    textvariable=word_text,
    font=("Courier", 16)
)
word_label.pack(pady=20)

button = tk.Button(
    left_frame,
    text="Guess",
    font=("Courier", 16),
    command=handle_click
)
button.pack(pady=20)

# right canvas
canvas = tk.Canvas(right_frame, width=250, height=500, relief='sunken', bd=5)
canvas.pack()


def draw_man(num):
    if num == 1:
        canvas.create_oval(100, 50, 150, 100, width=5)
    elif num == 2:
        canvas.create_line(125, 100, 125, 200, width=5)


window.mainloop()
