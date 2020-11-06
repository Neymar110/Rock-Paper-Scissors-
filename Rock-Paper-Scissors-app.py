import tkinter as tk
from rps_logic import *
root = tk.Tk()

canvas = tk.Canvas(root, height = 550, width = 700)
canvas.pack()

frame = tk.Frame(root)
frame.place(relheight = 1, relwidth = 1)

picture = tk.PhotoImage(file = "bg_img.png")
picture_label = tk.Label(root, image = picture)
picture_label.place(relheight = 1, relwidth = 1)

rounds_entry = tk.Entry(frame)
rounds_entry.place(relx = 0.35, relwidth = 0.3, rely = 0.3)



rps_entry = tk.Entry(frame)
rps_entry.place(relx = 0.35, relwidth = 0.3, rely = 0.5)

button = tk.Button(frame, text = "Submit Rounds Choice", bg = "#ffc107", command = lambda: initiation_func(rounds_entry.get()))
button.place(anchor = "n", relwidth = 0.3, relheight = 0.05, relx = 0.5, rely = 0.54)

root.mainloop()