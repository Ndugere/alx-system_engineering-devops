import json
import requests

url = input("Kindly write the url to the api you want to communicate to: ")

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

else:
    print("Unable to fetch data from the API")
