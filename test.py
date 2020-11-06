import tkinter as tk
import time

limit = 5

# run = False


def testFunc(limit):
    # count = 0
    # button_press = False
    # for run in range(0,limit):
    #     # while not button_press:
    #     #     time.sleep(1)
    #     label['text'] = str(run)
    #     # button_press = False
    #     time.sleep(3)
    if (root.count < limit):
        label['text'] = root.count
        root.count += 1
    else:
        pass
        
    
def apple():
    for num in range(0, 6):
        print(num)
        time.sleep(1)
    # try:
    #     if (count < limit):
    #         label['text'] = count
    #     count += 1
    # except UnboundLocalError:
    #     label['text'] = "error"
        

def example():
    testFunc(limit)
root = tk.Tk()

root.count = 0

root.title("Weather App")

canvas = tk.Canvas(root, height = 550, width = 700)
canvas.pack()

frame = tk.Frame(root, bg = "#80c1ff", bd = 1)
frame.place(relheight = 0.1, relwidth = 0.8, relx = 0.1, rely = 0.03)



lower_frame = tk.Frame(root, bg = "#80c1ff", bd  = 10)
lower_frame.place(relheight = 0.7, relx = 0.10, rely = 0.2, relwidth = 0.8)


label = tk.Label(lower_frame, bg = "white", font = ("Gotham Bold", 13))
label.pack()

button = tk.Button(frame, text = "Submit City", bg = "white", command = example)
button.place(anchor = "n", relwidth = 0.35, relheight = 0.60, relx = 0.75, rely = 0.15)
root.mainloop()