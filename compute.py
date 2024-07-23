def compute(response):
    data = response.json()

    '''
    for i in data:
        print(i, end = ': ')
        print(data[i])
    '''
        
    weather = data['weather'][0]['main']
    description = data['weather'][0]['description']
    temp_c = data['main']['temp']
    temp_f = (temp_c * 1.8) + 32

    weather_plural = ['Clouds']
    weather_single = ['Clear', 'Thunderstorm']
    desc_plural = ['few clouds', 'scattered clouds', 'broken clouds', 'overcast clouds']
    desc_single = ['clear sky', 'thunderstorm']
    
    weather_verb = ""
    desc_verb = ""

    # desc_verb =  description in desc_plural



    print(f"The weather in {data['name']} are '{weather}', mainly '{description}'.")
    # print(f"The temperatue is {round(temp_c)}°C or {round(temp_f)}°F.")

    '''
    lon = data['coord']['lon'] 
    lat = data['coord']['lat']

    lon_dir = 'E' if lon > 0 else 'W'
    lat_dir = 'N' if lat > 0 else 'S'
        
    print(f"The coordinates of {city} are {abs(lat)}° {lat_dir} latitude and {abs(lon)}° {lon_dir} longitude.")
    '''