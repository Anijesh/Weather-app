from django.shortcuts import render,redirect

from django.http import JsonResponse

from .services import WeatherService

from django.views.decorators.csrf import csrf_exempt # importing for the exempt of csrf in django

from .models import FavoriteCity
from django.contrib.auth.decorators import login_required

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

@login_required
def dashboard(request):
    favorites = FavoriteCity.objects.filter(user=request.user)
    context = {"favorites": favorites}

    city = request.POST.get('city') or request.GET.get('city')

    if city:
        weather_data = WeatherService.get_current_weather(city)
        forcast_weather = WeatherService.get_forecast(city)
        context.update({
            'city': city,
            'weather': weather_data,
            'forecast': forcast_weather
        })
    
    return render(request, "weather/dashboard.html", context)

@login_required
def save_favorite(request):
    if request.method == "POST":
        city = request.POST.get("city")

        FavoriteCity.objects.get_or_create(
            user=request.user,
            city=city
        )

    return redirect("dashboard")