from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic-Tac-Toe")
root.iconbitmap('tic-tac-toe_39453.ico')
#root.geometry("1200x700")

#build buttons
def b_click(b):
  pass

def make_button():
  
  btn = Button(
    root, 
    text=" ", 
    font=("Helvetica", 20), 
    height=3, 
    width=6, 
    bg="SystemButtonFace", 
    command=lambda: b_click(btn)
  )
  return btn

btns = [
  [],
  [],
  []
]

for row in range(3):
  for col in range(3):
    btn = make_button()
    btns[row].append(btn)
    btns[row][col].grid(row=row, column=col)

root.mainloop()
  

