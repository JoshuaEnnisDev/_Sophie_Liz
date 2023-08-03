import tkinter as tk
from tkinter import ttk

#window setup
window = tk.Tk()
window.title("Buttons")
window.geometry("500x500")

#code here
def btn_func():
    print(radio_var.get()) 
#make a button

button_label = tk.StringVar(value = "radio value button")
button = ttk.Button(window, text="A button")
button2 = ttk.Button(window, text="A button", command = btn_func, textvariable=button_label)
button.pack()
button2.pack()


#check button
check_var = tk.IntVar(value = 5)
check1 = ttk.Checkbutton(window, 
                        text = "checkbox", 
                        command = lambda: print(check_var.get()), 
                        variable= check_var,
                        onvalue= 5,
                        offvalue= 13
                        )
check1.pack()

#radio button
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window, 
                        text = "cat", 
                        value = "cat", 
                        variable = radio_var,
                        
                        )
radio2 = ttk.Radiobutton(window, text = "5", value = 5, variable= radio_var)

radio1.pack()
radio2.pack()


window.mainloop()# make sure this is the last line