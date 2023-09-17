from tkinter import *
import tkinter as tk
from tkinter import messagebox
import geocode
import fetchWeather
import currentlocation

API_KEY = "e7466c7574d23a1349e0929ef77c106e"

def searchWeather():

    city = city_text.get()
    location_info = geocode.generateCordinates(API_KEY, city)
    cordinates = location_info[0]
    latitude = cordinates['lat']
    longitude = cordinates['lon']
    weather = fetchWeather.fetchWeather(latitude, longitude, API_KEY)
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[2])+" °C"
        weather_l['text'] = weather[4].title()
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))


app = tk.Tk()
app.title("Weather App")
app.geometry("400x400")
city_text = tk.StringVar()
city_entry = tk.Entry(app, textvariable=city_text)
city_entry.pack()
Search_button = tk.Button(app, text="Search Weather", width=12, command=searchWeather)
Search_button.pack()
location_lbl = tk.Label(app, text="Location", font=('bold', 20))
location_lbl.pack()
temperature_label = tk.Label(app, text="")
temperature_label.pack()
weather_l = tk.Label(app, text="")
weather_l.pack()
app.mainloop()