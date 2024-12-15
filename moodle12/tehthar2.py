import requests


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'lang': 'fi'  # Säätilan kuvaus suomeksi
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature_kelvin = data['main']['temp']
        temperature_celsius = kelvin_to_celsius(temperature_kelvin)
        return weather_description, temperature_celsius
    else:
        return None, None



api_key = "95cb8ffa6452ef6b75e12f76180ac231"


city_name = input("Anna paikkakunnan nimi: ")


weather_description, temperature_celsius = get_weather(city_name, api_key)

if weather_description and temperature_celsius:
    print(f"Säätila: {weather_description}")
    print(f"Lämpötila: {temperature_celsius:.2f} °C")
else:
    print("Säätilan hakeminen epäonnistui. Tarkista paikkakunnan nimi ja API-avain.")