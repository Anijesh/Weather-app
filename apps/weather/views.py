from django.shortcuts import render

from .services import WeatherService

# Create your views here.

def home(request):
    context ={}
    if request.method == "POST":
        city = request.POST.get('city')
        weather_data = WeatherService.get_current_weather(city)
        context={'city':city,
                'weather':weather_data}
    return render(request,'weather/home.html',context)
