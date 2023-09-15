import geocoder as geocoder
import fetchWeather as fetchWeather

def main():
    API_KEY = "e7466c7574d23a1349e0929ef77c106e"
    user_location = input("enter a location ")
    data = geocoder.generateCordinates(API_KEY, user_location)

    location_data = data[0]

    latitude = location_data['lat']
    longitude = location_data['lon']
    
    weather_data = fetchWeather.fetchWeather(latitude, longitude, API_KEY)

    if weather_data:
        print(f"Weather in {user_location}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")

if __name__ == "__main__":
    main()