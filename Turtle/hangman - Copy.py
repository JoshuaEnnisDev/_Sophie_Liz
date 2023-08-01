import random
import turtle
import time

#pick a word to guess
wordbank = ['epidemiology', 'cat', 'computer']
word = random.choice(wordbank)
letterDrawer = turtle.Turtle()
letterDrawer.speed(0)
letterDrawer.hideturtle()
letterDrawer.penup()
letterDrawer.goto(110,0)
letter_starting_pos = (-175,-200)


hangmanDrawer = turtle.Turtle()
hangmanDrawer.hideturtle()
hangmanDrawer.pensize(5)
hangmanDrawer.speed(0)
hangmanDrawer.penup()
hangmanDrawer.goto(-200,0)
hangmanDrawer.left(90)
hangmanDrawer.pendown()
hangmanDrawer.fd(250)
hangmanDrawer.left(90)
hangmanDrawer.fd(75)
hangmanDrawer.left(90)
hangmanDrawer.fd(50)

turtle.penup()
turtle.hideturtle()
turtle.goto(letter_starting_pos)
for ltr in word:
    turtle.write("_" + " ", True, font=("Courier", 20, 'bold') )


def game():
    
    global word
    num_wrong = 0
    max_wrong = 6
    has_won = False
    #empty list
    c_guesses = []
    i_guesses = []
    #Draw the hanger

    while num_wrong < max_wrong and not has_won:
        letterDrawer.goto(letter_starting_pos)
        
        #letterDrawer.clear()
        # for ltr in word:
        #     if ltr in c_guesses:
        #         letterDrawer.write(ltr + " ", True, font=("Courier", 20, 'bold') )
        #     else:
        #         letterDrawer.write("_" + "  ", True, font=("Courier", 20, 'bold'))
        
        guess = turtle.textinput("", "Guess a letter")
        letterDrawer.clear()
        #loop through the letters in the word
        if guess not in c_guesses:
            for ltr in word:
                if ltr == guess:
                    c_guesses.append(guess)
                elif guess not in word and guess not in i_guesses:
                    i_guesses.append(guess)
                    num_wrong += 1
                    
                print(c_guesses)
                print(i_guesses)
            #check if guess is in the word
        for ltr in word:
        
            if ltr in c_guesses:
                letterDrawer.write(ltr + " ", True, align='center', font=("Courier", 20, 'bold') )
            else:
                letterDrawer.write("_" + " ", True, font=("Courier", 20, 'bold'))
        
                
        #if player has gotten all the letters in the word
        if len(c_guesses) == len(word):
            turtle.goto(-150,300)
            turtle.write("Congrats!!!", font=("Courier", 30))
            has_won = True
        
        #if the amount of wrong guesses is equal to max wrong
        if num_wrong >= max_wrong:
            turtle.write("You lose. Sorry!")
            break
    turtle.mainloop()
    
            
    #questions:
        #how should we track guesses?
        
        #Should we check for already guessed letters?
        

    #-----DRAWING-----
    #blank spaces
    #gallows
    #body parts
    #letters

    #1 word bank
    #pick a random word
    #loop through the word
    #
game()
