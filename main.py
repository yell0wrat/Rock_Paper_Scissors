import random
import tkinter as tk
#a complete rework of my program, now with a basic gui and interactive buttons.
root = tk.Tk()
root.geometry('250x250') #window size
root.title('Rock Paper Scissors')
label= tk.Label(root, text='pick one.', font=('Arial', 18))
label.pack()

computer_choices = {
    '0': 'rock',
    '1': 'paper',
    '2': 'scissors'
} #this lets the computer have choice once given the randint function

def player_rock():
    com = computer_choices[str(random.randint(0,2))] #makes the int turn into a string
    if com == 'rock':
        match_results = 'draw!'
    elif com == 'paper':
        match_results = 'computer wins!'
    else:
        match_results = 'player wins!' #save an extra few bytes instead of doing another elif because there is no more other options, i am smart.
    results.config(text=match_results)

def player_paper():
    com = computer_choices[str(random.randint(0, 2))]
    if com == 'rock':
        match_results = 'player wins!'
    elif com == 'paper':
        match_results = 'draw!'
    else:
        match_results = 'computer wins!'
    results.config(text=match_results)

def player_scissors():
    com = computer_choices[str(random.randint(0, 2))]
    if com == 'rock':
        match_results = 'computer wins!'
    elif com == 'paper':
        match_results = 'player wins!'
    else:
        match_results = 'draw!'
    results.config(text=match_results)

results = tk.Label(root, text='', font=('Arial', 15))
results.pack(pady=10) #centers the text to be above the buttons, yet below the title

rock_button = tk.Button(root, text='rock', font=('Arial',17))
rock_button.config(command=player_rock)
rock_button.pack(side=tk.LEFT)

paper_button = tk.Button(root, text='paper', font=('Arial',17))
paper_button.config(command=player_paper)
paper_button.pack(side=tk.LEFT)

scissors_button = tk.Button(root, text='scissors', font=('Arial',17))
scissors_button.config(command=player_scissors)
scissors_button.pack(side=tk.LEFT)


root.mainloop()



