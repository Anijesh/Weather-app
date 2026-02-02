from django.shortcuts import render

from django.http import JsonResponse

from .services import WeatherService

from django.views.decorators.csrf import csrf_exempt # importing for the exempt of csrf in django

# Create your views here.

# this is used for exmpet csrf token of django "@csrf_exempt"
def home(request):
    context ={}
    if request.method == "POST":
        city = request.POST.get('city')
        weather_data = WeatherService.get_current_weather(city)
        forcast_weather = WeatherService.get_forecast(city)
        context={'city':city,
                'weather':weather_data,
                'forecast':forcast_weather}
    return render(request,'weather/home.html',context)
