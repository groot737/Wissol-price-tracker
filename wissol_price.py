import json
import requests
# name = str(input("enter superhero name: "))
url = 'http://wissol.ge/adminarea/api/ajaxapi/get_fuel_prices?lang=eng'
response = requests.get(url)
response.raise_for_status()
data = json.loads(response.text)

for i in range(len(data)):
    print(f'{data[i]["fuel_name"]} - {data[i]["fuel_price"]}')
