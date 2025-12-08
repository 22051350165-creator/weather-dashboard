"""
Weather Dashboard - Tkinter + OpenWeatherMap API

This Python program creates a simple "Weather Dashboard" using a graphical
interface (GUI). The user types a city name (for example: "London"),
and the app shows:
- Temperature (in °C)
- Weather description (e.g., "clear sky")
- Humidity
- Wind speed
- A small emoji that matches the weather (☀️, ☁️, 🌧️, etc.)

The goal of this project is:
- To practice working with an external API (OpenWeatherMap)
- To build a basic GUI using Tkinter
- To write clean and well-documented code so that even beginners can follow it
"""

# Import the Tkinter library for creating the graphical user interface (GUI)
import tkinter as tk

# Import a helper from Tkinter that shows popup windows (for warnings / errors)
from tkinter import messagebox

# Import the "requests" library so we can make HTTP requests to the weather API
import requests 

# ------------------------------------------------------------
# CONFIGURATION SECTION
# Here we define constants and settings that are used in the app
# ------------------------------------------------------------

# Your personal API key from OpenWeatherMap.
# IMPORTANT:
# - You must sign up on https://openweathermap.org/
# - Go to "API keys" in your profile
# - Copy your key and paste it here as a string.
API_KEY = "3b4df9859574eec8280cf4d44ce5faee"

# Base URL for the OpenWeatherMap API endpoint that returns current weather data.
# We will send HTTP GET requests to this URL with some parameters.
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Unit system for temperature:
# - "metric" means Celsius
# - "imperial" means Fahrenheit
# - "standard" means Kelvin
UNITS = "metric"

# A small dictionary that maps general weather types to emojis.
# The API response contains a field called "main" inside "weather"
# (for example: "Clear", "Clouds", "Rain").
# We translate these into small icons to make the dashboard more fun.
WEATHER_EMOJIS = {
    "Thunderstorm": "⛈️",
    "Drizzle": "🌦️",
    "Rain": "🌧️",
    "Snow": "❄️",
    "Clear": "☀️",
    "Clouds": "☁️",
    # Any other weather type will use a default emoji later
}


# ------------------------------------------------------------
# FUNCTION: fetch_weather
# This function talks to the OpenWeather API and gets the weather data.
# ------------------------------------------------------------

def fetch_weather(city_name: str):
    """
    Fetch weather data for a given city from the OpenWeather API.

    Parameters:
        city_name (str): The name of the city entered by the user.

    Returns:
        dict or None:
            - If the request is successful and valid, returns a Python dictionary
              (parsed JSON) containing weather information.
            - If something goes wrong (invalid city, no internet, server issue),
              returns None.
    """

    # Parameters we need to send to the API.
    # These are added to the URL as a query string, for example:
    # ?q=London&appid=YOUR_API_KEY&units=metric&lang=en
    params = {
        "q": city_name,    # The city we want weather for (e.g., "Istanbul")
        "appid": API_KEY,  # Our secret API key so the server knows who we are
        "units": UNITS,    # Whether to use metric (Celsius) or other units
        "lang": "en",      # Language for the weather description text
    }

    try:
        # Send an HTTP GET request to the API.
        # The "timeout" means we will give up if there is no response within 5 seconds.
        response = requests.get(BASE_URL, params=params, timeout=5)

        # If the API returns an HTTP error code (like 404 or 500),
        # this line will raise an exception.
        response.raise_for_status()

        # If we reach this point, the request was successful.
        # The API responds with JSON text. .json() converts that into a Python dictionary.
        return response.json()

    except requests.exceptions.HTTPError:
        # This block runs if the server responded, but with an error status code.
        # For example, if the city is not found (404).
        # We choose to return None so the caller can handle the error.
        return None

    except requests.exceptions.RequestException:
        # This block runs if something goes wrong with the network:
        # - No internet connection
        # - DNS failure
        # - Timeout
        # - Other low-level network issues
        return None


# ------------------------------------------------------------
# FUNCTION: on_get_weather
# This function is called when the user clicks the "Get Weather" button.
# It reads the input, calls the API, and updates the GUI.
# ------------------------------------------------------------

def on_get_weather():
    """
    Handle the "Get Weather" button click.

    Steps:
    1. Read the city name from the input field.
    2. Validate that the user entered something.
    3. Call the fetch_weather() function to get data from the API.
    4. If there is an error, show a popup message.
    5. If everything is OK, extract useful data and update the labels in the window.
    """

    # Get the text from the entry box.
    # .get() returns the string, .strip() removes extra spaces at the beginning/end.
    city = city_entry.get().strip()

    # If the user clicked the button without entering a city,
    # we show a warning and stop the function.
    if not city:
        messagebox.showwarning("Input Required", "Please enter a city name.")
        return  # Exit the function early

    # Call our function that talks to the API.
    data = fetch_weather(city)

    # If data is None (network error or city not found),
    # OR if the API returned a "cod" (code) that is not 200 (not OK),
    # we show an error message.
    if data is None or data.get("cod") != 200:
        messagebox.showerror(
            "Error",
            "Could not fetch weather data.\n"
            "Please check the city name or your internet connection."
        )
        return

    # --------------------------------------------------------
    # If we reach here, we have valid data from the API.
    # Now we extract specific values that we want to show.
    # --------------------------------------------------------

    # "main" is a nested dictionary that usually contains:
    # - "temp" (temperature)
    # - "humidity"
    main = data.get("main", {})

    # "wind" is another dictionary:
    # - "speed" (wind speed)
    wind = data.get("wind", {})

    # "weather" is a list containing at least one dictionary with:
    # - "main" (e.g., "Clear", "Clouds")
    # - "description" (e.g., "clear sky")
    weather_list = data.get("weather", [])

    # Get the values we need from the dictionaries.
    # .get() is used instead of direct indexing to avoid crashes if the key is missing.
    temp = main.get("temp")
    humidity = main.get("humidity")
    wind_speed = wind.get("speed")

    # Default values in case "weather" is empty or doesn't have expected fields.
    if weather_list:
        weather_main = weather_list[0].get("main", "")
        # Description is a more detailed text. We use .title() to capitalize nicely.
        description = weather_list[0].get("description", "").title()
    else:
        weather_main = ""
        description = "Unknown"

    # Use our emoji dictionary to choose an icon.
    # If the weather type is not in the dictionary, we use a default globe emoji.
    emoji = WEATHER_EMOJIS.get(weather_main, "🌍")

    # --------------------------------------------------------
    # Finally, update the labels in the GUI so the user can see the data.
    # Each label displays one piece of information.
    # --------------------------------------------------------

    # Show the city name at the top, capitalized (e.g., "london" -> "London")
    city_result_label.config(text=f"{city.title()}")

    # Show the temperature as a floating-point number with 1 decimal place.
    # Example: 21.347 → "21.3 °C"
    temp_label.config(text=f"Temperature: {temp:.1f} °C")

    # Show the weather description followed by the emoji.
    desc_label.config(text=f"Weather: {description} {emoji}")

    # Show humidity as a percentage.
    humidity_label.config(text=f"Humidity: {humidity}%")

    # Show wind speed in meters per second.
    wind_label.config(text=f"Wind Speed: {wind_speed} m/s")


# ------------------------------------------------------------
# TKINTER UI SETUP
# In this section we build the window and place all widgets.
# Widgets are elements like labels, buttons, and text boxes.
# ------------------------------------------------------------

# Create the main application window.
# "root" will contain everything (labels, buttons, etc.).
root = tk.Tk()

# Set the window title (this text appears in the title bar).
root.title("Weather Dashboard")

# Disable manual resizing.
# This helps keep the layout simple and consistent.
root.resizable(True, True)

# Create a main container frame with padding around the content.
# "padx" and "pady" add space around the inside of the frame.
container = tk.Frame(root, padx=20, pady=20)

# Place the container into the window.
# .pack() is one of Tkinter's layout managers.
container.pack()

# ----------------- TITLE LABEL -----------------

# Create a label widget for the application title.
title_label = tk.Label(
    container,
    text="Weather Dashboard",        # Text displayed
    font=("Helvetica", 18, "bold")   # Font: (family, size, style)
)

# Place the title at grid row 0, column 0 and span across 2 columns.
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 15))

# ----------------- CITY INPUT (LABEL + ENTRY) -----------------

# Label that says "City:"
city_label = tk.Label(container, text="City:", font=("Helvetica", 11))

# Place the city label in the first column of row 1.
# "sticky='e'" aligns it to the right (east) inside its grid cell.
city_label.grid(row=1, column=0, sticky="e", padx=(0, 5))

# Entry widget where the user types the city name.
city_entry = tk.Entry(container, width=25, font=("Helvetica", 11))

# Place the entry box in the second column of row 1.
# "sticky='w'" aligns it to the left (west).
city_entry.grid(row=1, column=1, pady=5, sticky="w")

# Put the text cursor in the city entry box when the app starts.
city_entry.focus()

# ----------------- "GET WEATHER" BUTTON -----------------

# Create a button that the user clicks to fetch the weather.
get_btn = tk.Button(
    container,
    text="Get Weather",             # Text displayed on the button
    font=("Helvetica", 11, "bold"), # Button font
    command=on_get_weather          # Function to call when clicked
)

# Place the button on row 2, spanning both columns.
get_btn.grid(row=2, column=0, columnspan=2, pady=10)

# ----------------- RESULT LABELS -----------------

# This label shows the city name after a successful search.
city_result_label = tk.Label(
    container,
    text="",                        # Initially empty
    font=("Helvetica", 14, "bold")
)
city_result_label.grid(row=3, column=0, columnspan=2, pady=(10, 5))

# Label for temperature
temp_label = tk.Label(container, text="", font=("Helvetica", 11))
temp_label.grid(row=4, column=0, columnspan=2, sticky="w")

# Label for weather description + emoji
desc_label = tk.Label(container, text="", font=("Helvetica", 11))
desc_label.grid(row=5, column=0, columnspan=2, sticky="w")

# Label for humidity
humidity_label = tk.Label(container, text="", font=("Helvetica", 11))
humidity_label.grid(row=6, column=0, columnspan=2, sticky="w")

# Label for wind speed
wind_label = tk.Label(container, text="", font=("Helvetica", 11))
wind_label.grid(row=7, column=0, columnspan=2, sticky="w")

# ------------------------------------------------------------
# START THE APPLICATION
# This line starts Tkinter's event loop and keeps the window open.
# The program will keep running until the user closes the window.
# ------------------------------------------------------------
root.mainloop()
