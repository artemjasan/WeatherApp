import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    appid ='b1b72a99f86a510fac7e0177a66cf9ba'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    
    if(request.method =='POST'):
        form =CityForm(request.POST)
        form.save()

    form = CityForm()
    
    Cities = City.objects.all()
    all_cities = []

    for city in Cities:
        res  = requests.get(url.format(city.name)).json()

        city_info = {
        'city':city.name,
        'temp': res["main"] ["temp"] ,
        'icon': res["weather"] [0] ["icon"],
        'pres': res["main"]["pressure"]
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)

# Create your views here.
