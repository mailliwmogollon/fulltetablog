from django.urls import path
from . import views
from os import name

app_name = "BLOG"
urlpatterns = [
    path('', views.index, name="index"),
    path('lactancia', views.lactancia, name="lactancia"),
    path('salud', views.salud, name="salud"),
    path('motricidad', views.motricidad, name="motricidad"),
    path('rincon', views.rincon, name="rincon"),
    path('busqueda', views.busqueda, name="busqueda")
]