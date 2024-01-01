import os
from requests import post,get

GEO_API_KEY = os.environ.get("GEO_API_KEY")
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")


class Weather:
    def __init__(self):
        self.lat = ""
        self.lon = ""
        self.geo_url = "https://ipgeolocation.abstractapi.com/v1"
        self.geo_params = {"api_key": "3e7c686808e24f1f919e392b5020fe80"}
        self.weather_url = "https://api.openweathermap.org/data/2.5/weather?"

    def get_weather(self):
        geo_response = get(url=self.geo_url, params=self.geo_params)
        data = geo_response.json()
        self.lon = data["longitude"]
        self.lat = data["latitude"]
        weather_params = {
            "lat": self.lat,
            "lon": self.lon,
            "appid": WEATHER_API_KEY
        }
        weather_response = get(url=self.weather_url, params=weather_params)
        data = weather_response.json()
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["main"]
        condition_icon = data["weather"][0]["icon"]
        city = data["name"]
        country = data["sys"]["country"]
        return temperature, condition, condition_icon, city, country
