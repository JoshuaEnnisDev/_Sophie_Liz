import random
import turtle

#pick a word to guess
wordbank = ['epidemiology', 'cat', 'computer']

l_start_pos = (-100, -150)
letter_drawer = turtle.Turtle()
letter_drawer.penup()
letter_drawer.goto(l_start_pos)
letter_drawer.pensize(5)

#draw hangman hanger

def draw_man(wrong):
    if wrong == 1:


def game():
    
    word = random.choice(wordbank)
    word = "elizabeth"
    num_wrong = 0
    max_wrong = 6
    has_won = False
    #empty list
    c_guesses = []
    i_guesses = []

    for ltr in word:
        letter_drawer.write("_ ", True, font=("Courier", 20))
    

    while num_wrong < max_wrong and not has_won:
        
        letter_drawer.goto(l_start_pos)

        guess = turtle.textinput("", "Guess a letter")

        if guess not in c_guesses: 
            for ltr in word:
                if ltr == guess:
                    c_guesses.append(guess)
                else:
                    num_wrong += 1
                    #draw_man(num_wrong)
                    i_gueeses.append(guess)
                    break

        for ltr in word:
            if ltr in c_guesses:
                letter_drawer.write(ltr + " ", True, font=("Courier", 20))
            else:
                letter_drawer.write("_ ", True, font=("Courier", 20))
                    
        #print(c_guesses)
                
        #if player has gotten all the letters in the word
        if len(c_guesses) == len(word):
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
