import requests

API_KEY = "6668fd1c4ff42058a933716028eb54c7e144b451"

base_url = f"https://api.geocodify.com/v2/geocode?api_key={API_KEY}&q="

r = requests.get(base_url + "1600 Pennsylvania Ave NW, Washington DC")

print(r.json()['response']['features'][0]['geometry']['coordinates'])