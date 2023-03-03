from doctest import master

import requests
import json
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font, messagebox

window = tk.Tk()
window.title("Weather App")
window.geometry("600x600")

city_label = tk.Label(window, text="", font=("Arial", 12))
city_label.grid(row=0, column=0, padx=10, pady=10, sticky='ne')
# Temperature label
temp_label = tk.Label(window, text="Temperature:", font=("Arial", 16))
temp_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# Humidity label
humidity_label = tk.Label(window, text="Humidity:", font=("Arial", 16))
humidity_label.grid(row=1, column=0, padx=10, pady=10, stick='w')

# Wind speed label
wind_speed_label = tk.Label(window, text="Wind Speed:", font=("Arial", 16))
wind_speed_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')

# Weather description label
description_label = tk.Label(window, text="Weather Description:", font=("Arial", 16))
description_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')

# Temperature value label
temp_value_label = tk.Label(window, text="", font=("Arial", 16))
temp_value_label.grid(row=0, column=1, padx=10, pady=10, stick='e')

# Humidity value label
humidity_value_label = tk.Label(window, text="", font=("Arial", 16))
humidity_value_label.grid(row=1, column=1, padx=10, pady=10, sticky='e')

# Wind speed value label
wind_speed_value_label = tk.Label(window, text="", font=("Arial", 16))
wind_speed_value_label.grid(row=2, column=1, padx=10, pady=10, sticky='e')

# Weather description value label
description_value_label = tk.Label(window, text="", font=("Arial", 16))
description_value_label.grid(row=3, column=1, padx=10, pady=10, sticky='e')

# Zipcode input box
zipcode_entry = tk.Entry(window, font=("Arial", 12))
zipcode_entry.grid(row=4, column=2, padx=10, pady=10, sticky="e")
# Zipcode Label
zipcode_label = tk.Label(window, text="Zipcode:", font=("Arial", 12))
zipcode_label.grid(row=4, column=1, padx=10, pady=10, sticky="s")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)


def get_weather():
    # try:
    api_key = '1ae486b1c81c89b2fcd44c09c7976eb5'
    zipcode = zipcode_entry.get()

    # Get the city name from the zipcode using the Zippopotam API
    city_url = f"https://api.zippopotam.us/us/{zipcode}"
    city_response = requests.get(city_url)
    city_data = json.loads(city_response.text)
    city_name = city_data["places"][0]["place name"]
    city_label.config(text=f'Weather in {city_name}')

    url = f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode},&APPID={api_key}'

    response = requests.get(url)

    weather_data = json.loads(response.content)
    # print(weather_data)

    temperature = round((weather_data['main']['temp'] - 273.15) * (9 / 5) + 32, 2)
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    description = weather_data['weather'][0]['description']

    # if temperature < 60:
    #    bg_image = Image.open("snow1.png")
    #    photo = ImageTk.PhotoImage(bg_image)

    #    background_label = tk.Label(window, image=photo)
    #    background_label.image = photo
    #    background_label.grid(row=0, column=0, rowspan=1, columnspan=1)

    # print(f'Temperature: {temperature}°F')
    # print(f'Humidity: {humidity}%')
    # print(f'Wind Speed: {wind_speed} m/s')
    # print(f'Weather Description: {description}')

    temp_value_label.config(text=f'{temperature} °F')
    humidity_value_label.config(text=f'{humidity}%')
    wind_speed_value_label.config(text=f'{wind_speed} m/s')
    description_value_label.config(text=f'{description.capitalize()}')


# except:
# messagebox.showerror("Error", "Please enter a valid US Zipcode")


# Button to get weather data
get_weather_button = tk.Button(window, text="Get Weather", font=("Arial", 16), command=get_weather)
get_weather_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, stick='w')

window.mainloop()
