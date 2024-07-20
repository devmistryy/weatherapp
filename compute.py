def reconstruct():
    params = {'q' : city,  'appid' : api_key,  'units' : 'metric' }
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    data = response.json()
    print("3")

def compute(response):
    data = response.json()

    print(data['weather'])
    
    '''
    lon = data['coord']['lon'] 
    lat = data['coord']['lat']

    lon_dir = 'E' if lon > 0 else 'W'
    lat_dir = 'N' if lat > 0 else 'S'
        
    print(f"The coordinates of {city} are {abs(lat)}° {lat_dir} latitude and {abs(lon)}° {lon_dir} longitude.")
    '''