import os
import requests
GEO_API_KEY = os.environ.get("GEO_API_KEY")
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")


class Weather:
    def __init__(self):
        self.lat = ""
        self.lon = ""
        self.geo_url = "https://ipgeolocation.abstractapi.com/v1"
        self.geo_params = {"api_key": GEO_API_KEY}
        self.weather_url = "https://api.openweathermap.org/data/2.5/weather?"

    def get_weather(self):
        geo_response = requests.get(url=self.geo_url, params=self.geo_params)
        data = geo_response.json()
        self.lon = data["longitude"]
        self.lat = data["latitude"]
        weather_params = {
            "lat": self.lat,
            "lon": self.lon,
            "appid": WEATHER_API_KEY
        }
        weather_response = requests.get(url=self.weather_url, params=weather_params)
        data = weather_response.json()
        print(data)
        main_data = data.get("main", {})
        if not main_data:
            raise KeyError("Key 'main' not found in weather data")

        temperature = main_data.get("temp", "")
        # temperature = data["main"]["temp"]
        condition = data["weather"][0]["main"]
        condition_icon = data["weather"][0]["icon"]
        city = data["name"]
        country = data["sys"]["country"]
        return temperature, condition, condition_icon, city, country
