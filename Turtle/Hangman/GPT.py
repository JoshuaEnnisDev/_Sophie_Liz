import turtle

body_parts = []
# Set up the turtle
turtle.setup(width=800, height=600)
hangman = turtle.Turtle()
hangman.speed(2)
hangman.penup()
hangman.goto(-300, -200)
hangman.pendown()

# Draw the gallows
hangman.forward(100)
hangman.backward(50)
hangman.left(90)
hangman.forward(200)
hangman.right(90)
hangman.forward(100)
hangman.right(90)
hangman.forward(25)

# Function to draw a body part
def draw_body_part(part):
    if part == "head":
        hangman.circle(25)
    elif part == "body":
        hangman.right(90)
        hangman.forward(100)
    elif part == "left_arm":
        hangman.backward(100)
        hangman.left(45)
        hangman.forward(75)
    elif part == "right_arm":
        hangman.backward(75)
        hangman.right(90)
        hangman.forward(75)
    elif part == "left_leg":
        hangman.left(45)
        hangman.forward(75)
    elif part == "right_leg":
        hangman.backward(75)
        hangman.right(90)
        hangman.forward(75)

# Word to be guessed
word = "hangman"
guessed_letters = []

# Function to draw the word spaces
def draw_word_spaces():
    start_x = -300
    start_y = -250
    space_width = 30
    for i in range(len(word)):
        turtle.penup()
        turtle.goto(start_x + i * space_width, start_y)
        turtle.pendown()
        turtle.forward(space_width)

# Function to draw a guessed letter
def draw_guessed_letter(letter):
    start_x = -300
    start_y = -250
    space_width = 30
    for i in range(len(word)):
        if word[i] == letter:
            turtle.penup()
            turtle.goto(start_x + i * space_width + space_width // 2, start_y + 10)
            turtle.pendown()
            turtle.write(letter, align="center", font=("Arial", 14, "normal"))

# Function to handle a correct guess
def handle_correct_guess(letter):
    guessed_letters.append(letter)
    draw_guessed_letter(letter)

# Function to handle an incorrect guess
def handle_incorrect_guess(letter):
    guessed_letters.append(letter)
    body_parts = ["head", "body", "left_arm", "right_arm", "left_leg", "right_leg"]
    draw_body_part(body_parts[len(guessed_letters) - 1])

# Check if the game is won
def is_game_won():
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

# Main game loop
while True:
    guess = turtle.textinput("Hangman", "Enter a letter:")
    if guess is None:
        break
    if len(guess) != 1 or not guess.isalpha():
        continue
    if guess in guessed_letters:
        continue
    if guess in word:
        handle_correct_guess(guess)
        if is_game_won():
            turtle.goto(-150, 0)
            turtle.write("Congratulations, you won!", align="center", font=("Arial", 20, "normal"))
            break
    else:
        handle_incorrect_guess(guess)
        if len(guessed_letters) == len(body_parts):
            turtle.goto(-150, 0)
            turtle.write("Game over. You lost!", align="center", font=("Arial", 20, "normal"))
            break

turtle.done()
