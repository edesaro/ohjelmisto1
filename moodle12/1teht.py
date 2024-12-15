import requests

response = requests.get("https://api.chucknorris.io/jokes/random")


if response.status_code == 200:
    joke = response.json().get("value")
    print(f"Chuck Norris -vitsi: {joke}")
else:
    print("Vitsin hakeminen epäonnistui.")