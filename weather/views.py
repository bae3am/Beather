from django.shortcuts import render
from django.http import HttpResponse
import requests
import config

headers = {
    'Content-Type' : 'application/json; charset=utf-8'
}

def index(request):
    return HttpResponse(getWeather('Seoul'))

def getWeather(cityNm):
    result = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + cityNm +
    "&appid=" + config.owm_app_id, headers=headers)
    return result
