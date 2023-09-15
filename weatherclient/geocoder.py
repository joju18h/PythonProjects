import requests
def generateCordinates(key, location):
    baseurl = "http://api.openweathermap.org/geo/1.0"

    parameters = {
        "q" : location,
        "appid" : key,
    }

    response = requests.get(baseurl + "/direct", params=parameters)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)
        return None