

from django.contrib import admin
from django.urls import path
from .views import home,save_favorite,dashboard

urlpatterns = [
    path("",home,name='home'),
    path("dashboard/", dashboard, name="dashboard"),
    path("save/", save_favorite, name="save_favorite"),
]