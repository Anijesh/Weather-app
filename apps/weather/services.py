import os
import requests

API_KEY= os.getenv('WEATHER_API_KEY')

class WeatherService:
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

    @staticmethod
    def get_current_weather(city):
        if not API_KEY:
            return {"error":"API_KEY not found"}
        
        params = {
            "q" : city,
            'appid' : API_KEY,
            "units" : "metric"
        }
        try:
            response= requests.get(
                WeatherService.BASE_URL,
                params= params,
                timeout =5
            )
            return response.json()
        except requests.RequestException:
            return {"error": "weather service unavailable"}