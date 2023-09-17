import geocoder

def get_location():
    location_info = geocoder.ip('me')
    cordinates = location_info.latlng
    return cordinates



