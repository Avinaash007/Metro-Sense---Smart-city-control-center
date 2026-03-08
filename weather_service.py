import requests

API_KEY = "c8394d551b22173134e31d35c564ef3a"

LAT = 11.0168
LON = 76.9558

def get_weather_data():

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    rainfall = 0
    if "rain" in data:
        rainfall = data["rain"].get("1h", 0)

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    return rainfall, temperature, humidity