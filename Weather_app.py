import tkinter as tk

root = tk.Tk()

root.title("Weather App")

canvas = tk.Canvas(root, height = 350, width = 400)
canvas.pack()

frame = tk.Frame(root, bg = "#80c1ff", bd = 1)
frame.place(relheight = 0.1, relwidth = 0.8, relx = 0.1, rely = 0.03)

# label = tk.Label(frame, text = "Enter A Location", bg = "white")
# label.place(relheight = 0.05, relwidth = 0.3, relx = 0.35, rely = 0.44)

button = tk.Button(frame, text = "Submit Choice", bg = "#ffc107")
button.place(anchor = "n", relwidth = 0.3, relheight = 0.5, relx = 0.75, rely = 0.25)

entry = tk.Entry(frame, fg = "blue")
entry.place(relx = 0.04, relwidth = 0.5, rely = 0.20)


lower_frame = tk.Frame(root, bg = "#80c1ff", bd  = 10)
lower_frame.place(relheight = 0.7, relx = 0.10, rely = 0.2, relwidth = 0.8)
root.mainloop()