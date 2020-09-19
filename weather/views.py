from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests
# Create your views here.
def weather_index(request):
    url="http://api.openweathermap.org/data/2.5/weather?q={}&appid=984187adff3a2f9c195fc9cf17a71a19"
    city="Mumbai"
    r=requests.get(url.format(city)).json()
    temp=int(r["main"]["temp"])-273.15  
    form=CityForm()
    temp=int(r["main"]["temp"])-273.15  


    # ##copy
    context={
    'city':city,
    'temp':round(temp,2),
    'icon':r["weather"][0]["icon"],
    'description':r["weather"][0]["description"],
    'form':form,
}
    # context={
    #     'city':city,
    #     'temp':127,
    #     'icon':'10d',
    #     'description':'slow rain',
    #     'form':form,
    # }

    if request.method=="POST":
        form=CityForm(request.POST)
        if form.is_valid():
            try:
                city=(form.cleaned_data['name'])
                city=str(city).capitalize()
                r=requests.get(url.format(form.cleaned_data['name'])).json()
                temp=int(r["main"]["temp"])-273.15 
                context={
                'city':city,
                'temp':round(temp,2),
                'icon':r["weather"][0]["icon"],
                'description':r["weather"][0]["description"],
                'form':form,
            }
                
                
            except:
                print('Error')


    

    return render(request,'weather/index.html',context)
