import customtkinter as ctk
import subprocess
import os
from AgriMod5 import wikisearch,start_time,init_bot, main,manual_schedule


ctk.set_default_color_theme("green")
#window
window =ctk.CTk()
window.title('AgriBot')
window.geometry('250x350')
window.configure(fg_color=('#306844','#395144'))

#widgets
label = ctk.CTkLabel(
    window,
    text = 'Main Screen',
    text_color = '#AA8B56'
)
label.pack()
# Get the full path of the file
dirname = os.path.dirname(__file__)
weather_filename = os.path.join(dirname, 'weather forecast screen.py')
def weather_button_click_event():
    subprocess.Popen(["python", weather_filename])
    window.withdraw()  # close the current window
button = ctk.CTkButton(
    window,
    text='Check The Weather',
    fg_color=('#90EE90','#4E6C50'),
    text_color= ('#182c25','#F0EBCE'),
    hover_color= ('#4E6C50,#182c25'),
    corner_radius=10,
    command=weather_button_click_event
)
button.pack()

button = ctk.CTkButton(
    window,
    text='Manual Scheduler',
    fg_color=('#90EE90','#4E6C50'),
    text_color= ('#182c25','#F0EBCE'),
    hover_color= ('#4E6C50,#182c25'),
    corner_radius=10,
    command=manual_schedule
)
button.pack()

button = ctk.CTkButton(
    window,
    text='Speech driven scheduler',
    fg_color=('#90EE90','#4E6C50'),
    text_color= ('#182c25','#F0EBCE'),
    hover_color= ('#4E6C50,#182c25'),
    corner_radius=10,
    command=start_time
)
button.pack()

button = ctk.CTkButton(
    window,
    text='Ask a question',
    fg_color=('#90EE90','#4E6C50'),
    text_color= ('#182c25','#F0EBCE'),
    hover_color= ('#4E6C50,#182c25'),
    corner_radius=10,
    command=wikisearch
)
button.pack()

button = ctk.CTkButton(
    window,
    text='Agribot Commands',
    fg_color=('#90EE90','#4E6C50'),
    text_color= ('#182c25','#F0EBCE'),
    hover_color= ('#4E6C50,#182c25'),
    corner_radius=10,
    command=init_bot
)
button.pack()

button = ctk.CTkButton(
    window,
    text='Agribot Chatbot',
    fg_color=('#90EE90','#4E6C50'),
    text_color= ('#182c25','#F0EBCE'),
    hover_color= ('#4E6C50,#182c25'),
    corner_radius=10,
    command=main
)
button.pack()

button = ctk.CTkButton(
    window,
    text='Light Theme',
    fg_color=('#90EE90','#4E6C50'),
    text_color= ('#182c25','#F0EBCE'),
    hover_color= ('#4E6C50,#182c25'),
    corner_radius=10,
    
    command= lambda: ctk.set_appearance_mode('light')
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

#run
window.mainloop()