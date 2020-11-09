import tkinter as tk
from rps_logic import *
import time

button_press = False


root = tk.Tk()
root.counter = -1
root.title("ROCK-PAPER-SCISSORS Game")
canvas = tk.Canvas(root, height = 600, width = 545)
canvas.pack()

picture = tk.PhotoImage(file = "bg_img.png")
picture_label = tk.Label(root, image = picture)
picture_label.place(relheight = 1, relwidth = 1)

frame = tk.Frame(root)
frame.place(rely = 0.23, relx = 0.1, relheight = 0.2, relwidth = 0.8)

lower_frame = tk.Frame(root)
lower_frame.place(rely = 0.6, relx = 0.1, relheight = 0.2, relwidth = 0.8)

RPS_entry = tk.Entry(frame)
RPS_entry.place(relx = 0.03, rely = 0.17, relwidth = 0.55)

label = tk.Label(root, bg = "light blue", text = "Kindly enter a integer")
label.place(relx = 0.15, rely = 0.6, relwidth = 0.7, relheight = 0.2)


score_list = []
def example_invoker():
    round_submition_button.config(state = 'disabled')
    choice_entry_button.config(state = "active")
    label['text'] = "The Game Has Started,Kindly Enter A Choice"

def round_counter():
    example_invoker()
    rounds = RPS_entry.get()
    if (root.counter < int(rounds)):
        choice_entry_logic()
        root.counter += 1
    else:
        label['text'] = score_list
        round_submition_button.config(state = 'active')
        choice_entry_button.config(state = 'disabled')
        root.counter = 0



round_submition_button = tk.Button(frame, text = "Submit Rounds", bg = "#ffc107", command = round_counter)
round_submition_button.place(anchor = "n", relwidth = 0.4, relheight = 0.2, relx = 0.8, rely = 0.15)

score_list = []
def Paper_button_invoker():
    runner = best_of_one("Paper")
    score_list.append(runner[1])
    label['text'] = runner[0]
def Rock_button_invoker():
    runner = best_of_one("Rock")
    score_list.append(runner[1])
    label['text'] = runner[0]

def Scissors_button_invoker():
    runner = best_of_one("Scissors")
    score_list.append(runner[1])
    label['text'] = runner[0]

def printer():
    print(score_list)

def choice_entry_logic():
    choice = choice_entry.get()
    if choice == "Rock" or choice == "rock":
        Rock_button_invoker()
    if choice == "Scissors" or choice == "scissors":
        Scissors_button_invoker()
    if choice == "Paper" or choice == "paper":
        Paper_button_invoker()

choice_entry = tk.Entry(frame)
choice_entry.place(relx = 0.03, rely = 0.67, relwidth = 0.55)

choice_entry_button = tk.Button(frame, text = "Submit Choice", bg = "#ffc107", command = round_counter, state = 'disabled')
choice_entry_button.place(anchor = "n", relwidth = 0.4, relheight = 0.2, relx = 0.8, rely = 0.67)


        
            

root.mainloop()