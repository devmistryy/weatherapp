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
    for i in data['weather']:
        print(i)
    weather_description = data['weather']
    print(weather_description)
