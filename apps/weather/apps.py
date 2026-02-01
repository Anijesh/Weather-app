from django.apps import AppConfig


class WeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' 
    name = 'apps.weather'  # name = 'weathet' changed to name = 'apps.weather' as the weather is inside the apps