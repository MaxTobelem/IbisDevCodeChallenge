from django.shortcuts import render
import requests, requests_cache
from datetime import timedelta
# Create your views here.


def get_ford_cars(request):
    #Install cache for the request because Cocoche, updates its database every Monday at 3a.m. (only once a week).
    requests_cache.install_cache("ford", backend='sqlite', expire_after=timedelta(days=7))
    #Getting data from external API
    response = requests.get('http://server.cocoche.com.ar/car_listing_presentation?list_length=100')
    carslist = response.json()
    #carsList contains every car from the API
    carslist = carslist['carList']
    if len(carslist) == 0:
        return render(request, 'cars/home.html', {
    })
    #fordList conatins each Ford in the response we got from the API
    fordList = []
    for i in range(0,len(carslist),1):
        if carslist[i]['brandDescription'] == 'FORD':
            fordList.append(carslist[i])
    return render(request, 'cars/home.html', {
        'fordList': fordList,
    })