import requests
import json


data = json.loads(requests.get('https://swapi.dev/api/starships/10/').text)

with open('json_sw.json', 'w') as file:
    pilots_list = list()
    for link in data['pilots']:
        pilots_data = json.loads(requests.get(str(link)).text)
        homeworld_data = json.loads(requests.get(str(pilots_data['homeworld'])).text)
        pilots_list.append({'name': pilots_data['name'], 'height': pilots_data['height'],
                            'mass': pilots_data['mass'], 'homeworld': homeworld_data['name'],
                            'homeworld_url': pilots_data['homeworld']})

    json.dump({'name': data['name'],
               'max_atmosphering_speed': data['max_atmosphering_speed'],
               'starship_class': data['starship_class'],
               'pilots': pilots_list}, file, indent=4)

with open('json_sw.json', 'r') as file:
    text = file.read()
    print(text)

