import requests

def fetchWeather(latitude, longitutde, key):
    baseurl = "https://api.openweathermap.org/data/2.5/weather"

    parameters = {
        "lat" :  latitude,
        "lon" : longitutde,
        "appid" : key,
        "units" : "metric",
    }

    response = requests.get(baseurl,parameters)

    if response.status_code ==  200:
        json = response.json()
        city = json['name']
        country = json['sys']['country']
        temp = json['main']['temp']
        weather = json['weather'][0]['main']
        description = json['weather'][0]['description']
        data = [city, country, temp, weather ,description]
        return data
    else:
        print("Error:", response.status_code)