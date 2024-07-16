import requests # type: ignore

api_key = 'a85705f7101486a2a25e8c36ada14df4'

city = input("Enter city: ")

params = {
    'q' : city,
    'appid' : api_key,
    'units' : 'metric'
}

response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)



if response.status_code == 200:
    data = response.json()
    
    lon = data['coord']['lon'] 
    lat = data['coord']['lat']

    lon_dir = 'E' if lon > 0 else 'W'
    lat_dir = 'N' if lat > 0 else 'S'
        
    print(f"The coordinates of {city} are {abs(lat)}° {lat_dir} latitude and {abs(lon)}° {lon_dir} longitude.")
# coord, weather, base, main, visibility, wind, clouds, dt, sys, timezone, id, name, cod
