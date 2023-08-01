import random as r
import time
import turtle
t=turtle.Turtle()
words = ["password", "secrete", "phenomenon", "Giraffe", "unconstitutional", "accommodate", "Onomatopoeia", "palindrome", "ridiculous", "obvious", "abstentious"]
secret_word = r.choice(words)
secret_word = secret_word.lower()
secret_list = []
for character in secret_word:
  secret_list.append(character)




# character = "?"
# clue = []
# for q_marks in range(len(secret_list)):
#   clue.append(character)
# print "1", clue 
heart = "❤"
clue = ["?"] * len(secret_list)
q_difficulty = input("Choose a difficulty by entering 1 for Easy, 2 for Normal, 3 for sweaty tryhard \n 1 Easy \n 2 Normal \n 3 Sweaty Try Hard \n")
q_difficulty = int(q_difficulty)
if q_difficulty > 3:
  print ("Enter 1, 2, or 3")
if q_difficulty == 1:
  lives = 12
if q_difficulty == 2:
  lives = 9
if q_difficulty == 3:
  lives = 6
  import turtle as t
  winw = t.Screen()
  winw.setup(700,700)
  winw.addshape("Hanger.png")
  hanger = t.Turtle()
  hanger.hideturtle()
  hanger.shape("Hanger.png")
  hanger.left(90)
  hanger.showturtle()
  
  
word_correct = False

def update_clue(secret_word, clue, l_guess):
  index = 0
  while index < len(secret_word):
    if secret_word[index] == l_guess:
      clue[index] = l_guess
    index = index + 1
  return clue
  

while lives > 0: 
  print (clue)
  print ("Lives Left: ", heart * lives)
  if clue != secret_list:
    guess = input("Guess a letter or the whole word")
    guess = guess.lower()
  if guess == secret_word or clue == secret_list:
    word_correct = True
    break
  elif guess in secret_list:
    clue = update_clue(secret_word, clue, guess) 
  else:
    print ("Guess Incorrect. You loose a life")
    lives = lives - 1
    if q_difficulty == 3:
      if lives == 5 :
        x = 35
        y = 70
        t.penup()
        t.goto(x,y)
        t.ht()
        t.pendown()
        t.color("red")
        t.circle(25)
      if lives == 4:
        t.penup()
        t.seth(270)
        t.pendown()
        t.fd(80)
        t.color("red")
      
      if lives == 3:
        x = 35
        y = 55
        t.goto(x,y)
        t.penup()
        t.seth(360)
        t.pendown()
        t.fd(50)
        t.color("red")
      
      if lives == 2:
        x = 35
        y = 55
        t.goto(x,y)
        t.penup()
        t.seth(180)
        t.pendown()
        t.fd(50)
      
        t.color("red")
      
      if lives == 1:
        t.penup()
        x = 35
        y = -10
        t.goto(x,y)
        t.seth(240)
        t.pendown()
        t.fd(70)
        t.color("red")
      
      if lives == 0:
        x = 35
        y = -10
        t.goto(x,y)
        t.penup()
        t.seth(300)
        t.pendown()
        t.fd(70)
        t.color("red")

import turtle as t      
if word_correct == True:
  print ("You Win! The secret word was %s" %(secret_word))
  t.penup()
  x = 0
  y = 200
  t.goto(x,y)
  t.write("You win! Nice! The Word Was: %s" %(secret_word), False, align = "center", font = ("Arial", 25, "normal"))
if word_correct == False:
  print ("You Loose! The secret word was %s" %(secret_word))
  t.penup()
  x = 0
  y = 250
  t.goto(x,y)
   
  t.write("You Loose!", False, align = "center", font = ("Arial", 25, "normal"))
  for i in range(30):
    x = 0
    y = 200
    t.goto(x,y)
    t.color((r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)))
    t.write("The Secret Word is: %s" %(secret_word), False, align = "center", font = ("Calibri", 25, "normal"))
    time.sleep(0.1
    )
# for index in range(25):
#   guess = input("Guess a letter in the missing word!")
#   clue = update_clue(secret_word, clue, guess)
#   print clue

    