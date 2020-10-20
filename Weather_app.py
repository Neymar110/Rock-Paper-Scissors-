import tkinter as tk
from tkinter import font
import requests

def format_response(weather):
    try:
        city = weather['name']
        country = weather['sys']['country']
        description = weather['weather'][0]['description']
        temprature = weather['main']['temp'], "celsius"

        final_string = f"In {city}, {country} its full of {description} with a temprature of {temprature[0]} {temprature[1]}."
    
    except:
        final_string = f"That city is not found, kindly try again."
    return final_string


def get_weather(city):
    weather_key = '1a6280af32973003c0316a5558c7e11b'
    url = 'http://api.openweathermap.org/data/2.5/weather?id=524901&appid=1a6280af32973003c0316a5558c7e11b'
    dictionar = {'appid': weather_key, 'q' : city, 'units': 'metric'}
    response = requests.get(url, params=dictionar)
    weather = response.json()

    label['text'] = format_response(weather)  

root = tk.Tk()

root.title("Weather App")

canvas = tk.Canvas(root, height = 550, width = 700)
canvas.pack()

bgimg = tk.PhotoImage(file = "Landscape.png")
bglabel = tk.Label(root, image = bgimg)
bglabel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

frame = tk.Frame(root, bg = "#80c1ff", bd = 1)
frame.place(relheight = 0.1, relwidth = 0.8, relx = 0.1, rely = 0.03)

button = tk.Button(frame, text = "Submit City", bg = "white", command = lambda: get_weather(entry.get()))
button.place(anchor = "n", relwidth = 0.35, relheight = 0.60, relx = 0.75, rely = 0.15)

entry = tk.Entry(frame, fg = "black")
entry.place(relx = 0.04, relwidth = 0.5, rely = 0.15, relheight = 0.65)


lower_frame = tk.Frame(root, bg = "#80c1ff", bd  = 10)
lower_frame.place(relheight = 0.7, relx = 0.10, rely = 0.2, relwidth = 0.8)


label = tk.Label(lower_frame, bg = "white", font = ("Gotham Bold", 13))
label.place(relheight = 1, relwidth = 1)
print(tk.font.families())
root.mainloop()

# 42b52ccd10420d36a7913c26f4c85c5c

# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}

