import os
import requests
from django.core.cache import cache

API_KEY= os.getenv('WEATHER_API_KEY')

class WeatherService:
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

    @staticmethod
    def get_current_weather(city):
        if not API_KEY:
            return {"error":"API_KEY not found"}
        
        cache_key = f"weather:current:{city.lower()}"

        cached_data = cache.get(cache_key)
        if cached_data:
            return cached_data
        
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
            if response.status_code != 200:
                return {"error": data.get("message", "City not found")}
            cache.set(cache_key, data, timeout=600)
            return data

        except requests.RequestException:
            return {"error": "weather service unavailable"}
        
    
    FORECAST_URL = 'https://api.openweathermap.org/data/2.5/forecast'

    @staticmethod
    def get_forecast(city):
        if not API_KEY:
            return {'error':"API_KEY not found"}
        cache_key = f"weather:forecast:{city.lower()}"
        cached_data = cache.get(cache_key)
        if cached_data:
            return cached_data
        
        params = {
            'q':city,
            'appid':API_KEY,
            'units':'metric'
        }
        try:
            response = requests.get(
                WeatherService.FORECAST_URL,
                params=params,
                timeout =5
            )
            return response.json()
        
            if response.status_code != 200:
                return {"error": data.get("message", "City not found")}
            cache.set(cache_key, data, timeout=1800)

            return data
        except requests.RequestException:
            return {"error":"Weather service unavailable"}
        