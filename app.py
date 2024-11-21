import tkinter as tk
import requests

def getWeather():

    #get the city name from textField
    city = textField.get()
    
    api_key = "b46858fe7fc961c370ee3779093cc8b1"
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


    try: 

        #fetch weather data
        response = requests.get(api_url)
        data = response.json()

        if response.status_code == 200:

            #extract weather details
            weather_condition = data['weather'][0]['description'].capitalize()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']

             # Update labels with the retrieved information
            label1.config(text=f"Weather: {weather_condition}, {temperature}°C")
            label2.config(text=f"Humidity: {humidity}%")

        else:
            label1.config(text="City not found! Please try again.")
            label2.config(text="")

    except Exception as e:
        label1.config(text="Error retrieving data!")
        label2.config(text="")


# Set up the GUI
root = tk.Tk()
root.title("Weather App")

canvas = tk.Canvas(root, height=300, width=400)
canvas.pack()

# Entry widget for city input
textField = tk.Entry(root, justify="center", font=("poppins", 15), width=20)
textField.pack(pady=20)

# Button to trigger weather retrieval
button = tk.Button(root, text="Get Weather", command=getWeather)
button.pack(pady=10)

# Labels to display weather information
label1 = tk.Label(root, font=("poppins", 15), text="")
label1.pack(pady=10)

label2 = tk.Label(root, font=("poppins", 15), text="")
label2.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()        

