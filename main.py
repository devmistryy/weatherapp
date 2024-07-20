import requests # type: ignore
import compute

#this method is used when changing the city
def reconstruct():
    params['q'] = city
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    data = response.json()

# this is constant
api_key = 'a85705f7101486a2a25e8c36ada14df4'
url = 'https://api.openweathermap.org/data/2.5/weather'

#this is used for the beginning of the program
print("Hello, welcome to the terminal weather app!")

#this gets updated within the while loop
city = input("Please enter city: ")

#these three have to be updated each time the city gets updated
params = {'q' : city,  'appid' : api_key,  'units' : 'metric' }
response = None
data = None

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

except requests.exceptions.HTTPError as http_err:
    pass
except requests.exceptions.ConnectionError as conn_err:
    print('Connection error occurred.')
    #print(f'Connection error occurred: {conn_err}')
except requests.exceptions.Timeout as timeout_err:
    print(f'Timeout error occurred: {timeout_err}')
except requests.exceptions.RequestException as req_err:
    print(f'An error occurred: {req_err}')

if response == None:
    exit()

loop_ran = False

while data['cod'] == '404' or len(city) < 2:
    print("Invalid. Please try again")
    city = input("Enter city: ")
    loop_ran = True

#so if and if the city is inputted wrong then we change the parameters
if loop_ran: reconstruct()

if response.status_code == 200:
    compute.compute(response)
else:
    print("Connection Error.")

# coord, weather, base, main, visibility, wind, clouds, dt, sys, timezone, id, name, cod

