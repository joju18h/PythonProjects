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
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)
        return None