from weather import temp, wind_speed, humidity, pressure, header
import tkinter as tk
from tkinter import *
bg_color = '#226ba3'
window = tk.Tk()
window.geometry('500x400')
frame = tk.Frame(master=window, bg=bg_color)
frame.pack(fill=tk.BOTH, expand=True)

header_label = tk.Label(master=frame, text=header, bg=bg_color)
header_label.config(font=("Tahoma", 15))
header_label.pack(pady=20, anchor='n')

temp_label = tk.Label(master=frame, text=f"{temp} F", bg=bg_color)
temp_label.config(font=("Tahoma", 45))
temp_label.pack(pady=10)

windSpeed_label = tk.Label(master=frame, text=f"Wind Speed: {wind_speed} mph", bg=bg_color)
windSpeed_label.config(font=("Tahoma", 15))
windSpeed_label.pack(pady=10)

humidity_label = tk.Label(master=frame, text=f"Humidity: {humidity}", bg=bg_color)
humidity_label.config(font=("Tahoma", 15))
humidity_label.pack(pady=10)

pressure_label = tk.Label(master=frame, text=f"Pressure: {pressure}", bg=bg_color)
pressure_label.config(font=("Tahoma", 15))
pressure_label.pack(pady=10)



window.mainloop()
