import customtkinter as ctk
import subprocess as sub
import os
import requests
from AgriMod5 import Weather

ctk.set_default_color_theme("green")

# window
window = ctk.CTk()
window.title('AgriBot')
window.geometry('250x350')
window.configure(fg_color=('#306844', '#395144'))

# widgets
label = ctk.CTkLabel(
    window,
    text='Weather forecast',
    text_color='#AA8B56'
)
label.pack()

entry = ctk.CTkEntry(
    master=window,
    placeholder_text="Type in the town you're at.",
    corner_radius=10
)
entry.pack()


def Weather_click():
    location = entry.get()

    if location == "":
        label.config(text="Please enter a location.")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": "93bb70e0ffa2e77ce47f56b183e98762",
        "units": "metric"
    }
    response = requests.get(url, params=params)

    # Check if API request was successful
    if response.status_code == 200:
        # Parse weather data from API response
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        weather_info = f"Weather forecast for {location} town:\n - {weather}\n - Temperature: {temp} degrees Celsius\n - Feels like: {feels_like} degrees Celsius\n - Humidity: {humidity} percent"

        # Create a label widget to display the weather information
        weather_label = ctk.CTkLabel(
            window,
            text=weather_info,
            text_color="#AA8B56"
        )
        weather_label.pack()
    else:
        label.config(text="Error retrieving weather data.")


button = ctk.CTkButton(
    window,
    text='Forecast the weather (text)',
    fg_color=('#90EE90', '#4E6C50'),
    text_color=('#182c25', '#F0EBCE'),
    hover_color=('#4E6C50,#182c25'),
    corner_radius=10,
    command=Weather_click
)
button.pack()

button = ctk.CTkButton(
    window,
    text='Forecast the weather (audio)',
    fg_color=('#90EE90', '#4E6C50'),
    text_color=('#182c25', '#F0EBCE'),
    hover_color=('#4E6C50,#182c25'),
    corner_radius=10,
    command=Weather
)
button.pack()

button = ctk.CTkButton(
    window,
    text='Light Theme',
    fg_color=('#90EE90', '#4E6C50'),
    text_color=('#182c25', '#F0EBCE'),
    hover_color=('#4E6C50,#182c25'),
    corner_radius=10,

    command=lambda: ctk.set_appearance_mode('light')
)
button.pack()

button = ctk.CTkButton(
    window,
    text='Dark Theme',
    fg_color=('#90EE90','#4E6C50'),
    text_color= ('#182c25','#F0EBCE'),
    hover_color= ('#4E6C50,#182c25'),
    corner_radius=10,

    command= lambda: ctk.set_appearance_mode('dark')
)
button.pack()

# Get the full path of the file
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'main screen.py')
def exit_button_click_event():
    sub.Popen(["python", filename])
    window.withdraw()  # close the current window
button = ctk.CTkButton(
    window,
    text='Return to main screen',
    fg_color=('#90EE90','#4E6C50'),
    text_color= ('#182c25','#F0EBCE'),
    hover_color= ('#4E6C50,#182c25'),
    corner_radius=10,
    command=exit_button_click_event
)
button.pack()

frame = ctk.CTkFrame(
    master=window, 
    width=300, 
    height=300
    )

#run
window.mainloop()
