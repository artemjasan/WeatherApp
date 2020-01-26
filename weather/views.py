import requests
from django.shortcuts import render


def index(request):
    appid ='b1b72a99f86a510fac7e0177a66cf9ba'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = 'Prague'
    res  = requests.get(url.format(city)).json()
    
    city_info = {
        'city':city,
        'temp': res["main"] ["temp"] ,
        'icon': res["weather"] [0] ["icon"],
        'pres': res["main"]["pressure"]
    }

    context = {'info': city_info}

    return render(request, 'weather/index.html', context)

# Create your views here.
