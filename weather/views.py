import requests
from django.shortcuts import render


def index(request):
    appid ='b1b72a99f86a510fac7e0177a66cf9ba'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appid

    city = 'Prague'
    res  = requests.get(url.format(city))
    print(res.text)


    return render(request, 'weather/index.html')

# Create your views here.
