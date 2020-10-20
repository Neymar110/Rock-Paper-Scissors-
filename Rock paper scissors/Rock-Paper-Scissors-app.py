import tkinter as tk
import logic.py
root = tk.Tk()

canvas = tk.Canvas(root, height = 700, width = 800, bg = "red")
canvas.pack()

frame = tk.Frame(root, bg = "black")
frame.place(relheight = 1, relwidth = 1)

label = tk.Label(frame, text = "Rock, Paper or Scissors?", bg = "white")
label.place(relheight = 0.1, relwidth = 0.3, relx = 0.35, rely = 0.38)

button = tk.Button(frame, text = "Submit Choice", bg = "#ffc107")
button.place(anchor = "n", relwidth = 0.3, relheight = 0.05, relx = 0.5, rely = 0.54)

entry = tk.Entry(frame)
entry.place(relx = 0.35, relwidth = 0.3, rely = 0.5)

root.mainloop()