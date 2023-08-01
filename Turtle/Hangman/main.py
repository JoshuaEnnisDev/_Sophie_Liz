import turtle

drawing = turtle.Turtle()
screen = turtle.Screen()
letters = []
    


def draw_head(t):
    t.penup()
    t.goto(0,200)
    t.pendown()
    t.circle(50)
    
def make_phrase(t):
    phrase = turtle.textinput("Hi", "Enter your phrase")
    t.penup()
    t.goto(0, -200)
    t.pendown()
    for ch in phrase:
        index = 0
        letter = {'index':index, 'letter':ch, "pos":t.xcor() }
        if ch == " ":
            t.penup()
        else:
            t.pendown()
        t.fd(30)
        t.penup()
        t.fd(10)
        t.pendown
        letters.append(letter)
        index += 1
    t.hideturtle()
    return phrase
        
phrase = make_phrase(drawing)

def player_guess():
    letter_guess = turtle.textinput("", "Guess a letter")
    for letter in letters:
        if letter_guess == letter["letter"]:
            print_letter(letter['index'], letter["pos"])
            letters.remove(letter)
    print(letters)
            
    
        
def print_letter(index, pos):
    
    drawing.goto(pos + 10, -200)
    drawing.showturtle()
    drawing.pendown()
    drawing.write(letters[index]['letter'], font=("Arial", 20))

while len(letters) > 0: 
    player_guess()
screen.mainloop()

