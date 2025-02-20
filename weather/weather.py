import streamlit as st # type: ignore
import requests # type: ignore

# OpenWeatherMap API Key
API_KEY = "ea815a44ac089b6f28d755bacec67f30"

# Function to get weather data
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Streamlit UI
st.title("🌤️ Weather App")

# User input for city
city = st.text_input("Enter city name", "New York")

if st.button("Get Weather"):
    weather_data = get_weather(city)
    
    if weather_data:
        st.subheader(f"Weather in {city}")
        temp = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"].capitalize()
        icon = weather_data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"

        # Display temperature and weather icon
        col1, col2 = st.columns([2, 1])
        col1.metric("Temperature", f"{temp}°C")
        col1.write(description)
        col2.image(icon_url, caption=description)
    else:
        st.error("City not found! Please try again.")


# Run the app with `streamlit run weather_app.py` command
