import turtle
import random

hangman = turtle.Turtle()
hangman.hideturtle()
letter_drawer = turtle.Turtle()
letter_drawer.ht()
letter_drawer.penup()
letter_drawer.goto(100,-100)

screen = turtle.Screen()

wordbank = ['affix','bagpipes','bandwagon','banjo','buffalo',
            'cobweb','croquet','daiquiri','duplex','dwarves',
            'equip','exodus','fishhook','fixable','galaxy',
            'galvanize','ivy','juicy','kilobyte','megahertz',
            'oxygen','polka','quiz','rhubarb','schizophrenia',
            'unzip','uptown','vodka','whiskey','zombie']

#turtle.hideturtle()
turtle.speed(0)
turtle.pensize(2)
turtle.penup()
turtle.goto(200,0)
turtle.pendown()
turtle.left(90)
turtle.forward(175)
turtle.left(90)
turtle.forward(74)
turtle.left(90)
turtle.forward(35)

#word = random.choice(wordbank)
word = "hangman"
for char in word:
    letter_drawer.write('_ ', True, font=("Courier", 14, "normal"))

wrong = 0
won = False
correct = []

while wrong != 6 and not won:
    letter = turtle.textinput("Hangman", "Choose a letter")
    letter_drawer.goto(100,-100)
    for ch in word:
        if ch == letter:
            letter_drawer.write(letter + " ", True, font=("Courier", 14, "normal"))
            correct += letter
            print(correct)
        else:
            letter_drawer.write('_ ', True, font=("Courier", 14, "normal"))  


screen.mainloop()